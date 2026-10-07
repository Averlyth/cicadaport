# CicadaPort

![Python](https://img.shields.io/badge/Python-3.10--3.13-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20x86_64-lightgrey.svg)
![Source Version](https://img.shields.io/badge/Source-3.0.0--rc.2-orange.svg)
![Published Prerelease](https://img.shields.io/badge/Published-v3.0.0--rc.1-informational.svg)

**Specialized TCP reconnaissance platform for authorized security assessments.**

CicadaPort is developed and maintained by [Averlyth](https://github.com/Averlyth) as part of the **Obscuryx Security Platform**.

The platform separates orchestration, TCP reconnaissance, and service-evidence collection across Python, Rust, and Go while preserving explicit contracts, reproducible execution, controlled resource usage, and security-oriented defaults.

CicadaPort is intended exclusively for systems, networks, laboratories, and environments for which the operator has explicit authorization.

---

## Project Status

The current source tree identifies the application as:

| Item | Current state |
| --- | --- |
| Product | CicadaPort |
| Organization | Averlyth |
| Ecosystem | Obscuryx Security Platform |
| Python distribution | `portscanner-pro` |
| Source version | `3.0.0-rc.2` |
| Python version identifier | `3.0.0rc2` |
| Latest published prerelease | `v3.0.0-rc.1` |
| Stable release | Not published |
| Primary platform | Linux x86_64 |

`3.0.0-rc.2` is the current source-level release candidate. It is **not currently a published GitHub Release**.

The latest published prerelease remains [v3.0.0-rc.1](https://github.com/Averlyth/port-scanner/releases/tag/v3.0.0-rc.1).

Development state and published-release state are intentionally treated as separate concerns.

---

## Architecture

CicadaPort uses a specialized multi-language architecture with explicit responsibility boundaries.

### Python

Python provides the orchestration layer and coordinates:

- CLI and TUI execution;
- target parsing and normalization;
- hostname and address resolution;
- execution planning;
- multi-target orchestration;
- session management;
- result validation;
- event processing;
- reporting;
- profile management;
- native-engine integration.

### Rust

Rust provides the mandatory public TCP scanning engine.

The engine performs authorized TCP-connect reconnaissance with bounded concurrency, incremental result streaming, explicit cancellation, controlled resource usage, and versioned JSON Lines contracts.

### Go

Go provides service and banner evidence collection.

It operates only when banner collection is explicitly enabled and processes confirmed open ports provided by the orchestration layer.

The Go engine supports bounded reads, passive banner collection, controlled HTTP `HEAD` probing where permitted, TLS observation, output sanitization, and structured evidence.

---

## Execution Flow

The public execution flow is:

```text
Python
  |
  v
Rust TCP Engine
  |
  v
Python validation and normalization
  |
  v
Go Service Evidence Engine
  |
  v
Python consolidation, reporting and presentation
```

Operationally:

1. Python validates the request and authorized target specification.
2. Python resolves and normalizes the target.
3. Rust performs the TCP-connect scan.
4. Rust streams results through JSONL.
5. Python validates each native result.
6. Go receives confirmed open ports when `--banner-grab` is enabled.
7. Python validates and integrates service evidence.
8. Results are consolidated and presented through CLI, TUI, events, and reports.

Rust is the mandatory TCP engine for the public interface.

Go is the mandatory service-evidence engine when banner collection is enabled.

There is no silent fallback to internal Python implementations.

---

## Core Capabilities

CicadaPort currently provides:

- TCP-connect reconnaissance through the Rust engine;
- single-target and multi-target execution;
- IPv4 and IPv6 resolution;
- hostname, IP, CIDR, range, list, and target-file input;
- bounded target and port concurrency;
- reproducible scan profiles;
- cooperative cancellation;
- streaming native results;
- explicit Go-based banner collection;
- structured service evidence;
- CLI and terminal-based TUI operation;
- resumable sessions;
- transactional session persistence;
- TXT, JSON, CSV, and HTML reports;
- secure artifact creation;
- native-engine observability;
- release and supply-chain verification tooling.

CicadaPort is a reconnaissance platform. It is **not** a general-purpose vulnerability scanner or exploitation framework.

---

## Supported Environment

The currently verified support matrix is:

```text
Operating system:       Linux
Architecture:           x86_64
Validated distributions:
  - Ubuntu 22.04
  - Ubuntu 24.04

Python:
  - 3.10
  - 3.11
  - 3.12
  - 3.13

Rust:
  - 1.97.1

Go:
  - 1.26.8
```

The following environments are not currently part of the verified support matrix:

```text
Windows
macOS
ARM64
Python 3.14
```

Observing successful execution on an unvalidated platform does not automatically extend the supported-platform declaration.

---

## Installation from Source

Clone the current organization repository:

```bash
git clone https://github.com/Averlyth/port-scanner.git
cd port-scanner
```

Create an isolated Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
```

Build the required native engines:

```bash
./scripts/build_all.sh
```

Verify the installed CLI:

```bash
cicadaport --help
cicadaport --version
```

The legacy `portscanner` entry point remains available for compatibility, while `cicadaport` is the canonical public command.

---

## Basic Usage

A basic authorized TCP scan:

```bash
cicadaport 127.0.0.1
```

Select a port range:

```bash
cicadaport 127.0.0.1 -p 1-1000
```

Use a predefined profile:

```bash
cicadaport 127.0.0.1 --profile safe
```

Enable explicit banner collection:

```bash
cicadaport 127.0.0.1 --banner-grab
```

Open the terminal interface:

```bash
cicadaport 127.0.0.1 --profile standard --tui
```

All target specifications must remain inside an authorized assessment scope.

---

## Profiles

CicadaPort provides reproducible execution profiles:

```text
safe
standard
deep
custom
```

Profiles define controlled defaults for coverage, concurrency, timeouts, banner collection, and reporting.

Explicit CLI options take precedence over profile defaults.

The `deep` profile increases TCP coverage but does not transform CicadaPort into a host-discovery, UDP, SYN, operating-system fingerprinting, vulnerability-detection, or scripting framework.

---

## Multi-Target Orchestration

The positional target may contain:

- a single IP address;
- a hostname;
- a CIDR;
- an IP range;
- a comma-separated list.

Additional target specifications may be provided with `--target`.

Target files are supported through:

```bash
cicadaport --target-file targets.txt
```

Targets can be excluded before resolution:

```bash
cicadaport 127.0.0.1-127.0.0.4 \
  --exclude 127.0.0.3 \
  -p 20-25
```

Multiple targets can execute concurrently:

```bash
cicadaport 127.0.0.1 \
  --target 127.0.0.2 \
  -p 20-25 \
  --threads 8 \
  --target-workers 2
```

`--threads` represents a global concurrency budget. It is not silently multiplied for every active target.

Each resolved endpoint preserves its requested target, resolved address, execution state, evidence, results, and report identity.

Partial failures remain isolated so valid results from other targets are preserved.

---

## Terminal User Interface

The TUI is a terminal-based operational monitor built over the same orchestration layer used by the CLI.

It does not duplicate target parsing, network scanning, concurrency, banner collection, or report persistence.

Single-target sessions use the same orchestration path as the CLI, and multi-target sessions use the common batch runtime.

Example:

```bash
cicadaport 127.0.0.1 --profile standard --tui
```

The interface exposes live operational information including:

- execution progress;
- active and completed targets;
- open endpoints;
- engine activity;
- timing and throughput;
- evidence state;
- report paths;
- execution events.

Available shortcuts:

| Key | Action |
| --- | --- |
| `F1` | Display operational context |
| `F5` | Repeat the validated immutable request |
| `Ctrl+X` | Request cooperative cancellation |
| `Ctrl+L` | Clear the event view |
| `Q` / `F10` | Exit the interface |

The interface reports state produced by the orchestration and native engines; it does not synthesize fictitious progress or scan results.

---

## Native JSONL Contracts

CicadaPort uses versioned JSON Lines contracts between Python and the native engines.

### Rust request

Python sends a complete `scan_request` through standard input:

```json
{"contract_version":1,"record_type":"scan_request","target":"127.0.0.1","ports":[22,80,443],"timeout_ms":2000,"workers":3}
```

Rust is invoked through:

```text
rust-core --request-stdin
```

A result is emitted for each processed port:

```json
{"contract_version":1,"record_type":"port_result","target":"127.0.0.1","address":"127.0.0.1","address_family":"ipv4","host_state":"up","port":80,"protocol":"tcp","state":"open","reason":"connection_accepted","technique":"tcp_connect","service":"HTTP","banner":null,"response_time":0.001,"is_open":true,"evidence":{"reason":"connection_accepted","source":"rust","errno":0}}
```

### Go request

Go receives a complete `banner_request`:

```json
{"contract_version":1,"record_type":"banner_request","target":"127.0.0.1","ports":[80,443],"timeout_ms":3000}
```

The engine is invoked through:

```text
go-banner --request-stdin
```

Each requested port produces an explicit result:

```json
{"contract_version":1,"record_type":"banner_result","target":"127.0.0.1","port":80,"status":"captured","service":"HTTP","banner":"HTTP/1.0 200 OK","error":null,"source":"go"}
```

A banner result explicitly reports `captured`, `empty`, or `error`; missing evidence is not silently converted into success.

---

## Native Interface Guarantees

`--request-stdin` is the only operational process interface accepted by the Rust and Go native binaries.

`--help` is the only additional informational operation.

Unknown, positional, legacy, or mixed native arguments terminate before network activity.

During contract execution:

```text
stdin   -> complete versioned request
stdout  -> JSONL contract records only
stderr  -> diagnostics only
```

Python validates native data before incorporating it into the application state.

Validation includes:

- contract version;
- record type;
- required fields;
- unexpected fields;
- requested targets;
- requested ports;
- duplicate records;
- incomplete streams;
- state consistency;
- evidence consistency.

---

## Legacy Native Invocation Migration

Historical direct native interfaces are no longer supported.

Examples of removed invocation forms include:

```bash
rust-core --host 127.0.0.1 --ports 80,443
rust-core --host 127.0.0.1 --ports-stdin --timeout 1 --workers 2
go-banner --host 127.0.0.1 --ports 80,443 --timeout 1
```

Native integrations must use the versioned standard-input contract:

```bash
printf '%s\n' \
  '{"contract_version":1,"record_type":"scan_request","target":"127.0.0.1","ports":[80,443],"timeout_ms":1000,"workers":2}' |
  rust-core --request-stdin
```

The public interface remains the `cicadaport` command rather than direct native-engine invocation.

---

## Service and Banner Evidence

TCP reconnaissance does not send application payloads by default.

Banner collection must be explicitly enabled:

```bash
cicadaport localhost --banner-grab
```

It can also be disabled when enabled by a profile:

```bash
cicadaport localhost --profile standard --no-banner-grab
```

The Go engine can perform controlled service evidence collection using the currently permitted probes, including:

```text
passive-banner@1
http-head@1
```

TLS observation and HTTP probing remain bounded and explicitly controlled.

CicadaPort does not enable vulnerability detection, exploitation, unrestricted active probing, or arbitrary application payload execution through this mechanism.

---

## Session Persistence

CicadaPort uses Session Store v2 with SQLite WAL for current session persistence.

Observed results are persisted through normalized transactional operations.

The persistence model supports:

- bounded transaction batches;
- checkpoints;
- resumable execution;
- immutable execution plans;
- integrity history;
- recovery from interrupted sessions;
- migration from version-1 session data.

Version-1 source session files are preserved during migration for audit and rollback purposes.

---

## Secure Artifacts

Reports, event streams, and export bundles use security-oriented filesystem controls.

The implementation includes:

```text
Private directories: 0700
Private files:       0600
Exclusive creation
Atomic replacement
Same-filesystem temporary files
fsync confirmation
Symlink rejection
No overwrite by default
```

Human-readable outputs also sanitize potentially dangerous terminal and Unicode control data before presentation.

---

## Results and Reports

CicadaPort supports:

```text
TXT
JSON
CSV
HTML
```

A standard scan automatically creates a report:

```bash
cicadaport localhost -p 1-1000
```

Select JSON output:

```bash
cicadaport localhost -p 1-1000 --format json
```

Specify a report name:

```bash
cicadaport localhost \
  -p 1-1000 \
  --output audit \
  --format html
```

Select a report directory:

```bash
cicadaport localhost \
  -p 1-1000 \
  --report-dir results
```

Use an explicit output path:

```bash
cicadaport localhost \
  -p 1-1000 \
  --output results/customer/report.csv \
  --format csv
```

Automatic report names do not silently overwrite an existing report.

Reports preserve available technical context including target identity, resolved address, state, reason, service evidence, technique, and effective native engines.

HTML output escapes target and service data.

CSV output neutralizes formula cells.

---

## Security Model

CicadaPort is designed around conservative operational boundaries.

The project does not currently expose the following capabilities through its supported public reconnaissance workflow:

- unauthorized third-party scanning;
- raw-socket scanning;
- SYN scanning;
- UDP scanning;
- unrestricted host discovery;
- vulnerability detection;
- exploit execution;
- destructive testing;
- arbitrary offensive scripting.

The absence of these capabilities is intentional.

Contributions must not silently expand the network or offensive-security surface.

See [SECURITY.md](SECURITY.md) for vulnerability-reporting requirements.

---

## Supply-Chain and Release Integrity

The release process includes controls for software and artifact provenance.

Current mechanisms include:

- external GitHub Actions pinned to reviewed commit SHAs;
- dependency verification;
- Python release locks with hashes;
- Rust and Go dependency checks;
- Bandit analysis;
- Gitleaks secret scanning;
- CycloneDX 1.6 SBOM generation;
- artifact manifests;
- SHA-256 integrity records;
- reproducibility checks;
- isolated wheel and source-distribution tests;
- GitHub attestations;
- Sigstore/SLSA-oriented verification.

Release-candidate artifacts produced by CI do not automatically become public releases.

Tag creation, published GitHub Releases, source versioning, and candidate validation remain distinct lifecycle operations.

---

## Building Release Artifacts

Install the release dependencies:

```bash
python -m pip install -r requirements-release.txt
```

Build the artifacts:

```bash
./scripts/build_release_artifacts.sh
```

Validate them in isolation:

```bash
./scripts/test_release_artifacts.sh dist
```

Run dependency auditing:

```bash
./scripts/audit_dependencies.sh
```

---

## Development Validation

Development requires the supported Python, Rust, Go, Bash, and Linux toolchains.

The primary validation flow is:

```bash
./scripts/build_all.sh
./scripts/test_all.sh
bash -n scripts/*.sh
shellcheck scripts/*.sh
```

Focused checks include:

```bash
python -m pytest -v --cov=src --cov-report=term-missing

cargo fmt \
  --manifest-path rust-core/Cargo.toml \
  -- --check

cargo clippy \
  --manifest-path rust-core/Cargo.toml \
  --all-targets \
  --all-features \
  -- -D warnings

cargo test \
  --manifest-path rust-core/Cargo.toml
```

Go validation is run from `go-banner/`:

```bash
go test -race ./...
```

A change should not be integrated while a required validation check is failing.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the complete contribution contract.

---

## Engineering History and Provenance

CicadaPort preserves its technical and Git history across organizational migration.

Historical engineering documents under `docs/`, signed commits, signed tags, acceptance records, contracts, manifests, and audit evidence may contain state labels that describe a project gate **at the time that evidence was created**.

Those historical values are intentionally preserved for traceability and must not be interpreted as the current repository state without considering subsequent integration commits.

Organizational ownership by Averlyth does not rewrite historical authorship or provenance.

Original development history remains attributed to its original authors.

---

## Governance

The canonical repository owner is **Averlyth**.

Technical ownership is declared through `.github/CODEOWNERS`.

Repository changes are expected to remain:

- atomic;
- reviewable;
- signed where required;
- reproducible;
- traceable;
- compatible with applicable contracts;
- green under required CI controls.

Security-sensitive functionality must not be introduced implicitly through unrelated changes.

---

## Responsible Use

CicadaPort must only be used against:

- systems you own;
- controlled laboratories;
- systems or networks for which you have explicit authorization.

Users are responsible for ensuring that every target specification, expanded range, CIDR, hostname, address, and target-file entry remains within the authorized assessment scope.

Unauthorized scanning or activity against third-party infrastructure is outside the intended use of this project.

---

## License

CicadaPort is distributed under the [MIT License](LICENSE.md).

---

## Organization

**Averlyth**
Cybersecurity Engineering · Security Research · Security Tooling

CicadaPort is maintained as part of the **Obscuryx Security Platform**.

Organization: [github.com/Averlyth](https://github.com/Averlyth)

Repository: [github.com/Averlyth/port-scanner](https://github.com/Averlyth/port-scanner)
