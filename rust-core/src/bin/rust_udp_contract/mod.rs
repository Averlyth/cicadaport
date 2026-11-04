// P0-A.5 UDP contract v2 CANDIDATE, test-only. No sockets, no real scans, no v1 change.
use serde::{Deserialize, Serialize};
use serde_json::json;
use std::io::{self, Read};

#[cfg(test)]
const PROBE: &[u8] = b"CICADAPORT_P0A5_LOOPBACK_PROBE_V1";
const MAX_INPUT: u64 = 8192;
const MAX_PORTS: usize = 32;
const MAX_WORKERS: usize = 16;
const MAX_TIMEOUT_MS: u64 = 500;

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct UdpRequest {
    contract_version: u8,
    record_type: String,
    target: String,
    protocol: String,
    ports: Vec<u16>,
    timeout_ms: u64,
    workers: usize,
    probe_profile: String,
}

#[derive(Debug, Serialize)]
struct ValidatedRequest {
    contract_version: u8,
    record_type: &'static str,
    target: &'static str,
    protocol: &'static str,
    ports: Vec<u16>,
    timeout_ms: u64,
    workers: usize,
    probe_profile: &'static str,
    network_permitted: bool,
}

#[cfg(test)]
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize)]
#[serde(rename_all = "snake_case")]
enum UdpObservationStatus {
    EchoVerified,
    ResponseUnverified,
    NoResponseIndeterminate,
    ClosedOsReported,
    IoErrorIndeterminate,
}

#[cfg(test)]
fn classify_response(bytes: &[u8]) -> UdpObservationStatus {
    if bytes == PROBE {
        UdpObservationStatus::EchoVerified
    } else {
        UdpObservationStatus::ResponseUnverified
    }
}

#[cfg(test)]
fn classify_receive_error(kind: io::ErrorKind) -> UdpObservationStatus {
    if kind == io::ErrorKind::ConnectionRefused {
        UdpObservationStatus::ClosedOsReported
    } else {
        UdpObservationStatus::IoErrorIndeterminate
    }
}

fn validate_request(raw: &str) -> Result<ValidatedRequest, String> {
    if raw.len() > MAX_INPUT as usize {
        return Err("request_too_large".into());
    }
    let request: UdpRequest =
        serde_json::from_str(raw).map_err(|_| "invalid_request_json_or_unknown_field")?;
    if request.contract_version != 2 || request.record_type != "udp_scan_request" {
        return Err("unsupported_contract_header".into());
    }
    if request.target != "127.0.0.1" || request.protocol != "udp" {
        return Err("loopback_udp_only".into());
    }
    if request.probe_profile != "loopback_echo_v1" {
        return Err("unsupported_probe_profile".into());
    }
    if request.ports.is_empty() || request.ports.len() > MAX_PORTS || request.ports.contains(&0) {
        return Err("invalid_ports_or_port_count".into());
    }
    if !(1..=MAX_TIMEOUT_MS).contains(&request.timeout_ms) {
        return Err("invalid_timeout".into());
    }
    let mut ports = request.ports;
    ports.sort_unstable();
    ports.dedup();
    if request.workers == 0 || request.workers > MAX_WORKERS || request.workers > ports.len() {
        return Err("invalid_workers".into());
    }
    Ok(ValidatedRequest {
        contract_version: 2,
        record_type: "udp_contract_validated",
        target: "127.0.0.1",
        protocol: "udp",
        ports,
        timeout_ms: request.timeout_ms,
        workers: request.workers,
        probe_profile: "loopback_echo_v1",
        network_permitted: false,
    })
}

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    if args.len() != 1 || args[0] != "--request-stdin" {
        eprintln!("P0A5_CV2=STOP:only_--request-stdin_allowed");
        std::process::exit(2);
    }
    let mut bytes = Vec::new();
    if io::stdin()
        .take(MAX_INPUT + 1)
        .read_to_end(&mut bytes)
        .is_err()
        || bytes.len() > MAX_INPUT as usize
    {
        eprintln!("P0A5_CV2=STOP:stdin_unreadable_or_too_large");
        std::process::exit(1);
    }
    let raw = String::from_utf8(bytes).unwrap_or_else(|_| {
        eprintln!("P0A5_CV2=STOP:non_utf8");
        std::process::exit(1)
    });
    let value = validate_request(&raw).unwrap_or_else(|error| {
        eprintln!("P0A5_CV2=STOP:{error}");
        std::process::exit(1)
    });
    println!("{}", json!(value));
}

#[cfg(test)]
mod tests {
    use super::*;
    fn valid() -> &'static str {
        r#"{"contract_version":2,"record_type":"udp_scan_request","target":"127.0.0.1","protocol":"udp","ports":[45001,45000,45001],"timeout_ms":120,"workers":2,"probe_profile":"loopback_echo_v1"}"#
    }
    #[test]
    fn v2_validated_without_network() {
        let item = validate_request(valid()).unwrap();
        assert_eq!(item.ports, vec![45000, 45001]);
        assert_eq!(item.workers, 2);
        assert!(!item.network_permitted);
        let value = serde_json::to_value(&item).unwrap();
        assert_eq!(value["record_type"], "udp_contract_validated");
        assert_eq!(value["protocol"], "udp");
    }
    #[test]
    fn rejects_legacy_v1_header() {
        assert!(validate_request(
            &valid().replace("\"contract_version\":2", "\"contract_version\":1")
        )
        .is_err());
        assert!(validate_request(&valid().replace("udp_scan_request", "scan_request")).is_err());
    }
    #[test]
    fn rejects_remote_targets_and_tcp() {
        for bad in ["8.8.8.8", "localhost", "::1", "127.0.0.2"] {
            assert!(validate_request(&valid().replace("127.0.0.1", bad)).is_err());
        }
        assert!(
            validate_request(&valid().replace("\"protocol\":\"udp\"", "\"protocol\":\"tcp\""))
                .is_err()
        );
    }
    #[test]
    fn rejects_unknown_fields_and_profiles() {
        assert!(validate_request(
            &valid().replace("\"workers\":2", "\"workers\":2,\"payload\":\"evil\"")
        )
        .is_err());
        assert!(
            validate_request(&valid().replace("loopback_echo_v1", "arbitrary_payload")).is_err()
        );
    }
    #[test]
    fn rejects_zero_and_excess_timeout() {
        for ms in [0, 501, 10000] {
            assert!(validate_request(
                &valid().replace("\"timeout_ms\":120", &format!("\"timeout_ms\":{ms}"))
            )
            .is_err());
        }
    }
    #[test]
    fn rejects_bad_worker_bounds() {
        for workers in [0, 3, 17, 512] {
            assert!(validate_request(
                &valid().replace("\"workers\":2", &format!("\"workers\":{workers}"))
            )
            .is_err());
        }
    }
    #[test]
    fn rejects_zero_and_oversized_ports() {
        assert!(validate_request(&valid().replace("45001,45000,45001", "0")).is_err());
        let many = (1..=33)
            .map(|v| v.to_string())
            .collect::<Vec<_>>()
            .join(",");
        assert!(validate_request(&valid().replace("45001,45000,45001", &many)).is_err());
    }
    #[test]
    fn exact_echo_only() {
        assert_eq!(classify_response(PROBE), UdpObservationStatus::EchoVerified);
        assert_eq!(
            classify_response(b"unexpected"),
            UdpObservationStatus::ResponseUnverified
        );
        assert_eq!(
            classify_response(b""),
            UdpObservationStatus::ResponseUnverified
        );
    }
    #[test]
    fn silence_and_os_errors_remain_distinct() {
        assert_eq!(
            serde_json::to_string(&UdpObservationStatus::NoResponseIndeterminate).unwrap(),
            "\"no_response_indeterminate\""
        );
        assert_eq!(
            classify_receive_error(io::ErrorKind::ConnectionRefused),
            UdpObservationStatus::ClosedOsReported
        );
        assert_eq!(
            classify_receive_error(io::ErrorKind::TimedOut),
            UdpObservationStatus::IoErrorIndeterminate
        );
    }
    #[test]
    fn classification_wire_values_not_legacy_tcp_state() {
        let expected = [
            (UdpObservationStatus::EchoVerified, "echo_verified"),
            (
                UdpObservationStatus::ResponseUnverified,
                "response_unverified",
            ),
            (
                UdpObservationStatus::NoResponseIndeterminate,
                "no_response_indeterminate",
            ),
            (UdpObservationStatus::ClosedOsReported, "closed_os_reported"),
            (
                UdpObservationStatus::IoErrorIndeterminate,
                "io_error_indeterminate",
            ),
        ];
        for (status, name) in expected {
            assert_eq!(
                serde_json::to_string(&status).unwrap(),
                format!("\"{name}\"")
            );
        }
    }
}
