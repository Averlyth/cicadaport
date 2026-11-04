// P0-A.5 S5 — capability metadata for an external Rust example only.
// No network traffic, public selector, product release, or operational authorization.
use serde_json::{json, Value};
use std::io::{self, Write};

pub(crate) fn document() -> Value {
    json!({
        "schema": "cicadaport_udp_shadow_capabilities_v1",
        "record_type": "udp_capabilities",
        "engine": "cicadaport_udp_p0a5_shadow",
        "repository_head": "2cd2f5a03451ce91cfe34780e8c4cd63b0c08071",
        "protocol": "udp",
        "contract_version": 2,
        "supported_invocations": ["--udp-request-stdin", "--udp-capabilities-json"],
        "probe_profiles": ["loopback_echo_v1"],
        "address_scope": "ipv4_loopback_only",
        "allowed_target": "127.0.0.1",
        "max_ports_per_request": 32,
        "max_workers": 16,
        "max_timeout_ms": 500,
        "max_request_bytes": 8192,
        "service_detection": false,
        "public_api": false,
        "operational_go": false,
        "g8_live": "NO_GO_OPERACIONAL",
        "distribution_identity": "NOT_VERIFIED",
        "status": "SHADOW_EXPERIMENT_ONLY"
    })
}

pub(crate) fn emit_stdout() -> Result<(), String> {
    let mut data =
        serde_json::to_vec(&document()).map_err(|_| "capabilities_serialization_error")?;
    data.push(b'\n');
    let mut stdout = io::stdout().lock();
    stdout
        .write_all(&data)
        .map_err(|_| "capabilities_stdout_error")?;
    stdout.flush().map_err(|_| "capabilities_flush_error")?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn capabilities_are_explicitly_nonoperational() {
        let value = document();
        assert_eq!(value["protocol"], "udp");
        assert_eq!(value["contract_version"], 2);
        assert_eq!(value["public_api"], false);
        assert_eq!(value["operational_go"], false);
        assert_eq!(value["g8_live"], "NO_GO_OPERACIONAL");
        assert_eq!(value["address_scope"], "ipv4_loopback_only");
        assert_eq!(value["distribution_identity"], "NOT_VERIFIED");
    }

    #[test]
    fn capabilities_match_bounded_v2_limits() {
        let value = document();
        assert_eq!(value["max_ports_per_request"], 32);
        assert_eq!(value["max_workers"], 16);
        assert_eq!(value["max_timeout_ms"], 500);
        assert_eq!(value["max_request_bytes"], 8192);
        assert_eq!(value["service_detection"], false);
    }
}
