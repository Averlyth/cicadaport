// P0-A.5: integration SHADOW only. This example does NOT modify CicadaPort TCP v1.
// All network addresses are hardcoded IPv4 loopback, and the request contract is bounded.
use serde::Serialize;
use std::io::{self, Read, Write};
use std::net::{IpAddr, Ipv4Addr, SocketAddr};
use std::time::{Duration, Instant};
use tokio::net::UdpSocket;
use tokio::task::JoinSet;
use tokio::time;
#[path = "rust_udp_capabilities/mod.rs"]
mod p0a5_udp_capabilities_shadow;

mod validated_contract {
    #![allow(dead_code)] // Include the already-validated v2 contract without changing its bytes.
    pub(super) fn request(raw: &str) -> Result<(Vec<u16>, u64, usize), String> {
        let v = validate_request(raw)?;
        Ok((v.ports, v.timeout_ms, v.workers))
    }

    include!("rust_udp_contract/mod.rs");
}

const PROBE: &[u8] = b"CICADAPORT_P0A5_LOOPBACK_PROBE_V1";
const MAX_REQUEST_BYTES: u64 = 8192;

#[derive(Debug, Serialize)]
struct Observation {
    contract_version: u8,
    record_type: &'static str,
    target: &'static str,
    protocol: &'static str,
    port: u16,
    probe_profile: &'static str,
    status: &'static str,
    evidence_source: &'static str,
    elapsed_ms: u64,
    operational_go: bool,
}

async fn udp_probe(port: u16, timeout_ms: u64) -> Observation {
    let start = Instant::now();
    let bind_addr = SocketAddr::new(IpAddr::V4(Ipv4Addr::LOCALHOST), 0);
    let destination = SocketAddr::new(IpAddr::V4(Ipv4Addr::LOCALHOST), port);
    let status = match UdpSocket::bind(bind_addr).await {
        Err(_) => "io_error_indeterminate",
        Ok(socket) => match socket.connect(destination).await {
            Err(_) => "io_error_indeterminate",
            Ok(()) => match socket.send(PROBE).await {
                Err(error) if error.kind() == io::ErrorKind::ConnectionRefused => {
                    "closed_os_reported"
                }
                Err(_) => "io_error_indeterminate",
                Ok(written) if written != PROBE.len() => "io_error_indeterminate",
                Ok(_) => {
                    let mut response = [0u8; 512];
                    match time::timeout(
                        Duration::from_millis(timeout_ms),
                        socket.recv(&mut response),
                    )
                    .await
                    {
                        Err(_) => "no_response_indeterminate",
                        Ok(Err(error)) if error.kind() == io::ErrorKind::ConnectionRefused => {
                            "closed_os_reported"
                        }
                        Ok(Err(_)) => "io_error_indeterminate",
                        Ok(Ok(n)) if &response[..n] == PROBE => "echo_verified",
                        Ok(Ok(_)) => "response_unverified",
                    }
                }
            },
        },
    };
    Observation {
        contract_version: 2,
        record_type: "udp_observation",
        target: "127.0.0.1",
        protocol: "udp",
        port,
        probe_profile: "loopback_echo_v1",
        status,
        evidence_source: "rust_loopback_udp_probe",
        elapsed_ms: start.elapsed().as_millis().try_into().unwrap_or(u64::MAX),
        operational_go: false,
    }
}

fn emit<W: Write>(writer: &mut W, obs: &Observation) -> Result<(), String> {
    let mut line = serde_json::to_vec(obs).map_err(|_| "json_serialization_error")?;
    line.push(b'\n');
    writer.write_all(&line).map_err(|_| "jsonl_output_error")?;
    writer.flush().map_err(|_| "jsonl_flush_error")?;
    Ok(())
}

async fn abort_and_drain(set: &mut JoinSet<Observation>) {
    set.abort_all();
    while set.join_next().await.is_some() {}
}

async fn scan<W: Write>(
    ports: Vec<u16>,
    timeout_ms: u64,
    workers: usize,
    out: &mut W,
) -> Result<(), String> {
    if ports.is_empty() || ports.len() > 32 || workers == 0 || workers > 16 || workers > ports.len()
    {
        return Err("invalid_scheduler_limits".into());
    }
    let mut set = JoinSet::new();
    let mut next = 0usize;
    let mut emitted = 0usize;
    let total = ports.len();
    while next < total && set.len() < workers {
        let port = ports[next];
        set.spawn(udp_probe(port, timeout_ms));
        next += 1;
    }
    while let Some(joined) = set.join_next().await {
        let observation = match joined {
            Ok(result) => result,
            Err(_) => {
                abort_and_drain(&mut set).await;
                return Err("udp_task_join_failure".into());
            }
        };
        if let Err(error) = emit(out, &observation) {
            abort_and_drain(&mut set).await;
            return Err(error);
        }
        emitted += 1;
        if next < total {
            let port = ports[next];
            set.spawn(udp_probe(port, timeout_ms));
            next += 1;
        }
    }
    if emitted != total {
        return Err("udp_incomplete_result_stream".into());
    }
    Ok(())
}

fn run() -> Result<(), String> {
    let args: Vec<String> = std::env::args().skip(1).collect();
    if args.len() == 1 && args[0] == "--udp-capabilities-json" {
        return p0a5_udp_capabilities_shadow::emit_stdout();
    }
    if args.len() != 1 || args[0] != "--udp-request-stdin" {
        return Err("only_--udp-request-stdin_allowed".into());
    }
    let mut raw = Vec::new();
    io::stdin()
        .take(MAX_REQUEST_BYTES + 1)
        .read_to_end(&mut raw)
        .map_err(|_| "stdin_read_error")?;
    if raw.len() > MAX_REQUEST_BYTES as usize {
        return Err("request_too_large".into());
    }
    let text = String::from_utf8(raw).map_err(|_| "non_utf8_request")?;
    let (ports, timeout_ms, workers) = validated_contract::request(&text)?;
    let runtime = tokio::runtime::Builder::new_current_thread()
        .enable_io()
        .enable_time()
        .build()
        .map_err(|_| "udp_runtime_build_error")?;
    let mut stdout = io::stdout();
    runtime.block_on(scan(ports, timeout_ms, workers, &mut stdout))
}

fn main() {
    if let Err(error) = run() {
        eprintln!("P0A5_UDP_ENGINE=STOP:{error}");
        std::process::exit(1);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn rejects_scheduler_outside_limits_without_network() {
        let rt = tokio::runtime::Builder::new_current_thread()
            .enable_all()
            .build()
            .unwrap();
        for (ports, workers) in [(vec![], 1), (vec![1], 0), (vec![1], 2), (vec![1], 17)] {
            let mut output = Vec::new();
            assert!(rt.block_on(scan(ports, 5, workers, &mut output)).is_err());
            assert!(output.is_empty());
        }
    }

    #[test]
    fn jsonl_wire_observation_is_v2_and_never_tcp() {
        let x = Observation {
            contract_version: 2,
            record_type: "udp_observation",
            target: "127.0.0.1",
            protocol: "udp",
            port: 45000,
            probe_profile: "loopback_echo_v1",
            status: "no_response_indeterminate",
            evidence_source: "rust_loopback_udp_probe",
            elapsed_ms: 1,
            operational_go: false,
        };
        let mut bytes = Vec::new();
        emit(&mut bytes, &x).unwrap();
        assert_eq!(bytes.iter().filter(|&&b| b == b'\n').count(), 1);
        let doc: serde_json::Value = serde_json::from_slice(bytes.trim_ascii()).unwrap();
        assert_eq!(doc["contract_version"], 2);
        assert_eq!(doc["record_type"], "udp_observation");
        assert_eq!(doc["protocol"], "udp");
        assert_eq!(doc["status"], "no_response_indeterminate");
        assert_eq!(doc["operational_go"], false);
    }

    #[test]
    fn failing_writer_is_reported() {
        struct Failed;
        impl Write for Failed {
            fn write(&mut self, _: &[u8]) -> io::Result<usize> {
                Err(io::Error::new(io::ErrorKind::BrokenPipe, "test"))
            }
            fn flush(&mut self) -> io::Result<()> {
                Ok(())
            }
        }
        let item = Observation {
            contract_version: 2,
            record_type: "udp_observation",
            target: "127.0.0.1",
            protocol: "udp",
            port: 45000,
            probe_profile: "loopback_echo_v1",
            status: "response_unverified",
            evidence_source: "rust_loopback_udp_probe",
            elapsed_ms: 1,
            operational_go: false,
        };
        assert_eq!(emit(&mut Failed, &item), Err("jsonl_output_error".into()));
    }

    #[test]
    fn format_and_api_bounds_are_fixed() {
        assert_eq!(PROBE, b"CICADAPORT_P0A5_LOOPBACK_PROBE_V1");
        assert_eq!(MAX_REQUEST_BYTES, 8192);
    }
}
