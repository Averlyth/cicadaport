use crate::cancel::CancellationToken;
use crate::contract::ScanResult;
use crate::error::EngineError;
use crate::events::NativeEventEmitter;
use std::io::Write;
use tokio::sync::mpsc::Receiver;

const JSONL_SCRATCH_INITIAL_CAPACITY: usize = 512;

fn write_jsonl_record_with_buffer_mode<W: Write>(
    writer: &mut W,
    result: &ScanResult,
    scratch: &mut Vec<u8>,
    one_write: bool,
) -> Result<(), String> {
    scratch.clear();
    serde_json::to_writer(&mut *scratch, result)
        .map_err(|error| format!("Error generando JSONL: {error}"))?;
    if one_write {
        scratch.push(b'\n');
        writer
            .write_all(scratch)
            .map_err(|error| format!("Error escribiendo JSONL: {error}"))?;
    } else {
        writer
            .write_all(scratch)
            .map_err(|error| format!("Error escribiendo JSONL: {error}"))?;
        writer
            .write_all(b"\n")
            .map_err(|error| format!("Error escribiendo JSONL: {error}"))?;
    }
    writer
        .flush()
        .map_err(|error| format!("Error vaciando JSONL: {error}"))
}

fn write_jsonl_record_with_buffer<W: Write>(
    writer: &mut W,
    result: &ScanResult,
    scratch: &mut Vec<u8>,
) -> Result<(), String> {
    write_jsonl_record_with_buffer_mode(writer, result, scratch, false)
}

pub(crate) fn write_jsonl_record_stdout<W: Write>(
    writer: &mut W,
    result: &ScanResult,
) -> Result<(), String> {
    let mut scratch = Vec::with_capacity(JSONL_SCRATCH_INITIAL_CAPACITY);
    write_jsonl_record_with_buffer_mode(writer, result, &mut scratch, true)
}

pub(crate) fn write_jsonl_record<W: Write>(
    writer: &mut W,
    result: &ScanResult,
) -> Result<(), String> {
    let mut scratch = Vec::with_capacity(JSONL_SCRATCH_INITIAL_CAPACITY);
    write_jsonl_record_with_buffer(writer, result, &mut scratch)
}

pub(crate) fn run_writer<W: Write>(
    writer: &mut W,
    receiver: Receiver<ScanResult>,
    events: NativeEventEmitter,
    cancellation: CancellationToken,
    expected_results: usize,
) -> Result<(), EngineError> {
    run_writer_with_mode(
        writer,
        receiver,
        events,
        cancellation,
        expected_results,
        false,
    )
}

pub(crate) fn run_writer_stdout<W: Write>(
    writer: &mut W,
    receiver: Receiver<ScanResult>,
    events: NativeEventEmitter,
    cancellation: CancellationToken,
    expected_results: usize,
) -> Result<(), EngineError> {
    run_writer_with_mode(
        writer,
        receiver,
        events,
        cancellation,
        expected_results,
        true,
    )
}

fn run_writer_with_mode<W: Write>(
    writer: &mut W,
    mut receiver: Receiver<ScanResult>,
    mut events: NativeEventEmitter,
    cancellation: CancellationToken,
    expected_results: usize,
    one_write: bool,
) -> Result<(), EngineError> {
    let mut emitted_results = 0;
    let mut scratch = Vec::with_capacity(JSONL_SCRATCH_INITIAL_CAPACITY);

    while emitted_results < expected_results {
        let result = match receiver.blocking_recv() {
            Some(result) => result,
            None => break,
        };

        if let Err(error) =
            write_jsonl_record_with_buffer_mode(writer, &result, &mut scratch, one_write)
        {
            cancellation.cancel();
            return Err(EngineError::Output(error));
        }

        emitted_results += 1;
        if let Err(error) = events.emit(
            "port_completed",
            result.state,
            Some(result.port),
            emitted_results,
        ) {
            cancellation.cancel();
            return Err(EngineError::Output(error));
        }
    }

    if emitted_results != expected_results {
        cancellation.cancel();
        return Err(EngineError::Incomplete {
            emitted: emitted_results,
            expected: expected_results,
        });
    }

    if let Err(error) = events.emit("engine_completed", "success", None, emitted_results) {
        cancellation.cancel();
        return Err(EngineError::Output(error));
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::{
        run_writer, run_writer_stdout, write_jsonl_record, write_jsonl_record_with_buffer_mode,
    };
    use crate::cancel::CancellationToken;
    use crate::contract::{AppConfig, ScanEvidence, ScanResult, CONTRACT_VERSION};
    use crate::error::EngineError;
    use crate::events::NativeEventEmitter;
    use std::io::{self, Write};
    use tokio::sync::mpsc;

    fn config(total: usize) -> AppConfig {
        AppConfig {
            host: "127.0.0.1".to_string(),
            ports: (1..=total)
                .map(|port| u16::try_from(port).expect("puerto de prueba"))
                .collect(),
            timeout_ms: 10,
            workers: total.max(1),
        }
    }

    fn result(port: u16) -> ScanResult {
        ScanResult {
            contract_version: CONTRACT_VERSION,
            record_type: "port_result",
            target: "127.0.0.1".into(),
            address: "127.0.0.1".into(),
            address_family: Some("ipv4"),
            host_state: "up",
            port,
            protocol: "tcp",
            state: "closed",
            reason: "connection_refused",
            technique: "tcp_connect",
            service: String::new(),
            banner: None,
            response_time: 0.001,
            is_open: Some(false),
            evidence: ScanEvidence {
                reason: "connection_refused",
                source: "rust",
                detail: Some("connection refused".to_string()),
                errno: Some(111),
            },
        }
    }

    fn receiver_with_results(ports: &[u16]) -> mpsc::Receiver<ScanResult> {
        let (sender, receiver) = mpsc::channel(ports.len().max(1));
        for port in ports {
            sender
                .blocking_send(result(*port))
                .expect("canal de prueba abierto");
        }
        drop(sender);
        receiver
    }

    struct AlwaysFailWrite;

    impl Write for AlwaysFailWrite {
        fn write(&mut self, _buffer: &[u8]) -> io::Result<usize> {
            Err(io::Error::new(
                io::ErrorKind::BrokenPipe,
                "forced write failure",
            ))
        }

        fn flush(&mut self) -> io::Result<()> {
            Ok(())
        }
    }

    #[derive(Default)]
    struct FlushFailWriter {
        bytes: Vec<u8>,
    }

    impl Write for FlushFailWriter {
        fn write(&mut self, buffer: &[u8]) -> io::Result<usize> {
            self.bytes.extend_from_slice(buffer);
            Ok(buffer.len())
        }

        fn flush(&mut self) -> io::Result<()> {
            Err(io::Error::new(
                io::ErrorKind::BrokenPipe,
                "forced flush failure",
            ))
        }
    }

    #[derive(Default)]
    struct RecordLimitWriter {
        bytes: Vec<u8>,
        records: usize,
        limit: usize,
    }

    impl Write for RecordLimitWriter {
        fn write(&mut self, buffer: &[u8]) -> io::Result<usize> {
            if buffer == b"\n" {
                if self.records >= self.limit {
                    return Err(io::Error::new(
                        io::ErrorKind::BrokenPipe,
                        "forced record limit",
                    ));
                }
                self.records += 1;
            }
            self.bytes.extend_from_slice(buffer);
            Ok(buffer.len())
        }

        fn flush(&mut self) -> io::Result<()> {
            Ok(())
        }
    }

    #[test]
    fn serializes_one_contract_record_per_line() {
        let mut output = Vec::new();

        write_jsonl_record(&mut output, &result(80)).expect("JSONL válido");

        let text = String::from_utf8(output).expect("UTF-8 válido");
        assert!(text.ends_with('\n'));
        let payload: serde_json::Value = serde_json::from_str(text.trim()).expect("registro JSON");
        assert_eq!(payload["contract_version"], CONTRACT_VERSION);
        assert_eq!(payload["record_type"], "port_result");
        assert_eq!(payload["evidence"]["reason"], "connection_refused");
    }

    #[derive(Default)]
    struct CountingWriter {
        bytes: Vec<u8>,
        writes: usize,
        flushes: usize,
    }

    impl Write for CountingWriter {
        fn write(&mut self, buffer: &[u8]) -> io::Result<usize> {
            self.writes += 1;
            self.bytes.extend_from_slice(buffer);
            Ok(buffer.len())
        }

        fn flush(&mut self) -> io::Result<()> {
            self.flushes += 1;
            Ok(())
        }
    }

    #[test]
    fn p0a3_stdout_bytes_and_write_calls_are_scoped() {
        let record = result(443);
        let mut generic = CountingWriter::default();
        let mut stdout = CountingWriter::default();
        let mut a = Vec::with_capacity(512);
        let mut b = Vec::with_capacity(512);
        write_jsonl_record_with_buffer_mode(&mut generic, &record, &mut a, false)
            .expect("baseline JSONL");
        write_jsonl_record_with_buffer_mode(&mut stdout, &record, &mut b, true)
            .expect("stdout JSONL");
        assert_eq!(generic.bytes, stdout.bytes, "JSONL wire bytes unchanged");
        assert_eq!(generic.writes, 2, "generic Write remains two writes");
        assert_eq!(stdout.writes, 1, "stdout uses one write");
        assert_eq!(generic.flushes, 1);
        assert_eq!(stdout.flushes, 1);
    }

    #[test]
    fn p0a3_stdout_run_writer_preserves_jsonl_and_per_record_flush() {
        let cfg = config(3);
        let mut baseline = CountingWriter::default();
        let mut stdout = CountingWriter::default();
        run_writer(
            &mut baseline,
            receiver_with_results(&[1, 2, 3]),
            NativeEventEmitter::disabled_for_test(&cfg),
            CancellationToken::new(),
            3,
        )
        .expect("generic complete");
        run_writer_stdout(
            &mut stdout,
            receiver_with_results(&[1, 2, 3]),
            NativeEventEmitter::disabled_for_test(&cfg),
            CancellationToken::new(),
            3,
        )
        .expect("stdout complete");
        assert_eq!(stdout.bytes, baseline.bytes);
        assert_eq!(baseline.writes, 6);
        assert_eq!(stdout.writes, 3);
        assert_eq!(baseline.flushes, 3);
        assert_eq!(stdout.flushes, 3);
    }

    struct ShortThenBrokenPipe {
        calls: usize,
    }
    impl Write for ShortThenBrokenPipe {
        fn write(&mut self, buffer: &[u8]) -> io::Result<usize> {
            self.calls += 1;
            if self.calls == 1 {
                assert!(!buffer.is_empty());
                Ok(1)
            } else {
                Err(io::Error::new(io::ErrorKind::BrokenPipe, "partial output"))
            }
        }
        fn flush(&mut self) -> io::Result<()> {
            Ok(())
        }
    }

    #[test]
    fn p0a3_stdout_partial_write_error_cancels() {
        let cfg = config(1);
        for stdout_mode in [false, true] {
            let mut sink = ShortThenBrokenPipe { calls: 0 };
            let token = CancellationToken::new();
            let writer = NativeEventEmitter::disabled_for_test(&cfg);
            let output = if stdout_mode {
                run_writer_stdout(
                    &mut sink,
                    receiver_with_results(&[1]),
                    writer,
                    token.clone(),
                    1,
                )
            } else {
                run_writer(
                    &mut sink,
                    receiver_with_results(&[1]),
                    writer,
                    token.clone(),
                    1,
                )
            };
            let error = output.expect_err("partial output must not succeed");
            assert!(matches!(error, EngineError::Output(_)));
            assert!(token.is_cancelled());
            assert_eq!(sink.calls, 2);
        }
    }

    #[test]
    fn jsonl_record_is_two_writes_and_one_flush() {
        let mut writer = CountingWriter::default();
        write_jsonl_record(&mut writer, &result(80)).expect("registro");
        assert_eq!(writer.writes, 2);
        assert_eq!(writer.flushes, 1);
        let jsonl = String::from_utf8(writer.bytes).expect("UTF-8");
        assert_eq!(jsonl.lines().count(), 1);
        assert!(jsonl.ends_with('\n'));
        let record: serde_json::Value = serde_json::from_str(jsonl.trim()).expect("JSON");
        assert_eq!(record["port"], 80);
    }

    #[test]
    fn streaming_output_stays_record_granular_with_reused_scratch() {
        let cfg = config(3);
        let cancellation = CancellationToken::new();
        let mut writer = CountingWriter::default();
        run_writer(
            &mut writer,
            receiver_with_results(&[1, 2, 3]),
            NativeEventEmitter::disabled_for_test(&cfg),
            cancellation.clone(),
            3,
        )
        .expect("stream completo");

        assert!(!cancellation.is_cancelled());
        assert_eq!(writer.writes, 6);
        assert_eq!(writer.flushes, 3);
        let jsonl = String::from_utf8(writer.bytes).expect("UTF-8");
        let ports: Vec<u64> = jsonl
            .lines()
            .map(|line| {
                let record: serde_json::Value = serde_json::from_str(line).expect("JSONL");
                record["port"].as_u64().expect("port")
            })
            .collect();
        assert_eq!(ports, vec![1, 2, 3]);
    }

    #[test]
    fn first_write_failure_cancels_immediately() {
        let cfg = config(1);
        let cancellation = CancellationToken::new();
        let mut writer = AlwaysFailWrite;
        let error = run_writer(
            &mut writer,
            receiver_with_results(&[1]),
            NativeEventEmitter::disabled_for_test(&cfg),
            cancellation.clone(),
            1,
        )
        .expect_err("fallo de escritura");

        assert!(matches!(error, EngineError::Output(_)));
        assert!(error.to_string().contains("JSONL"));
        assert!(cancellation.is_cancelled());
    }

    #[test]
    fn flush_failure_cancels_and_is_propagated() {
        let cfg = config(1);
        let cancellation = CancellationToken::new();
        let mut writer = FlushFailWriter::default();
        let error = run_writer(
            &mut writer,
            receiver_with_results(&[1]),
            NativeEventEmitter::disabled_for_test(&cfg),
            cancellation.clone(),
            1,
        )
        .expect_err("fallo de flush");

        assert!(matches!(error, EngineError::Output(_)));
        assert!(error.to_string().contains("vaciando JSONL"));
        assert!(cancellation.is_cancelled());
    }

    #[test]
    fn failure_after_one_record_cancels_without_successful_completion() {
        let cfg = config(2);
        let cancellation = CancellationToken::new();
        let mut writer = RecordLimitWriter {
            limit: 1,
            ..RecordLimitWriter::default()
        };
        let error = run_writer(
            &mut writer,
            receiver_with_results(&[1, 2]),
            NativeEventEmitter::disabled_for_test(&cfg),
            cancellation.clone(),
            2,
        )
        .expect_err("fallo después de un registro");

        assert!(matches!(error, EngineError::Output(_)));
        assert_eq!(writer.records, 1);
        assert!(cancellation.is_cancelled());
    }

    #[test]
    fn early_channel_close_is_reported_as_incomplete() {
        let cfg = config(2);
        let cancellation = CancellationToken::new();
        let mut writer = Vec::new();
        let error = run_writer(
            &mut writer,
            receiver_with_results(&[1]),
            NativeEventEmitter::disabled_for_test(&cfg),
            cancellation.clone(),
            2,
        )
        .expect_err("stream incompleto");

        assert_eq!(
            error,
            EngineError::Incomplete {
                emitted: 1,
                expected: 2,
            }
        );
        assert!(cancellation.is_cancelled());
    }
}
