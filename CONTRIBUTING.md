# Contributing to CicadaPort

Thank you for contributing to CicadaPort.

CicadaPort is maintained by **Averlyth** as part of the **Obscuryx Security Platform**.

Contributions must preserve accurate results, safe defaults, explicit authorization boundaries, reproducible behavior, historical provenance, and the specialized Python, Rust, and Go architecture.

## Safety and Authorization

Network tests must be limited to:

- `127.0.0.1` and other controlled loopback fixtures;
- systems you own;
- controlled laboratories;
- systems or networks for which you have explicit authorization.

Do not introduce CI tests that depend on arbitrary public targets.

Security vulnerabilities must follow [SECURITY.md](SECURITY.md) and must not be disclosed through a public pull request or public issue.

## Repository Governance

The canonical repository is owned by **Averlyth**.

Technical ownership is defined through `.github/CODEOWNERS`.

The protected `main` branch is governed through repository rules and required CI checks.

Contributions targeting `main` must:

- use a pull request;
- preserve a reviewable and auditable commit history;
- satisfy all required status checks;
- avoid non-fast-forward history rewriting;
- preserve applicable signed commits, tags, release records, and historical engineering evidence;
- use the repository's permitted merge strategy;
- avoid unrelated changes in the same integration unit.

Historical contracts, acceptance records, signed tags, manifests, and engineering documents describe the state that existed when they were created and must not be rewritten merely to make older records appear current.

## Development Setup

Required toolchains:

- Python 3.10, 3.11, 3.12, or 3.13;
- Rust 1.97.1 with `rustfmt` and Clippy;
- Go 1.26.8;
- Linux x86_64;
- Bash;
- ShellCheck.

Create an isolated environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Build the native engines:

```bash
./scripts/build_all.sh
```

## Architecture Boundaries

The public execution architecture is:

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
Python consolidation and presentation
```

The responsibility boundaries must remain explicit.

### Python

Python owns orchestration, validation, CLI/TUI behavior, sessions, reporting, configuration, and native-engine integration.

### Rust

Rust is the mandatory public TCP scanning engine.

### Go

Go is the mandatory service-evidence engine when banner collection is enabled.

Presentation layers must not duplicate network-scanning logic.

## Specialized Public Interface

The public CLI does not expose native-engine selectors.

Contributions must preserve these invariants:

- Rust remains the mandatory public TCP engine;
- Go remains the mandatory banner engine when `--banner-grab` is enabled;
- `--engine` and `--banner-engine` are not accepted public options;
- legacy selector arguments fail through `argparse` with exit code `2`;
- failures occur before target resolution, binary execution, network activity, or report creation where required by the contract;
- internal programmatic requests use the canonical engine identities `rust` and `go`;
- incompatible internal engine values fail before network activity;
- there is no silent fallback to the internal Python implementations;
- CLI, TUI, events, and reports preserve effective engine metadata.

A change to these invariants requires corresponding tests and explicit technical review.

## Native Process Interface

The native binaries accept one operational process interface:

```text
rust-core --request-stdin
go-banner --request-stdin
```

`--help` is the only additional informational operation.

Historical arguments, unknown arguments, positional arguments, an empty invocation, and incompatible mixed invocations must fail before network activity.

Exit-code semantics must remain explicit:

```text
0 = successful contract execution or help
1 = contract or execution failure
2 = invalid process invocation
```

Native protocol rules:

- the complete versioned request travels through `stdin`;
- `stdout` contains JSONL contract records only during execution;
- diagnostics are written to `stderr`;
- Python invokes native binaries through the canonical `--request-stdin` interface;
- Rust preserves incremental `port_result` streaming;
- Rust flushes results as required by the streaming contract;
- Go emits an explicit `banner_result` for each requested open port;
- historical fragmented-argument or aggregate-output contracts must not be silently reintroduced.

Any native process-interface change requires corresponding Rust, Go, Python bridge, and integration tests.

## Result Contract

The following behavioral guarantees must be preserved:

- CLI and TUI consume `ScanOrchestrator`;
- presentation code does not independently implement target parsing, resolution, concurrency, TCP scanning, banner collection, or report persistence;
- single-target TUI sessions use the common orchestration path;
- multi-target TUI sessions use the common batch orchestration path;
- requested target and resolved endpoint identity remain distinguishable;
- partial multi-target failures remain isolated and visible;
- `safe`, `standard`, `deep`, and `custom` remain deterministic;
- cancellation propagates to active Python workers and native subprocesses;
- internal results preserve their canonical port state;
- reportable results are derived from canonical state rather than an independent compatibility flag;
- `is_open` remains a compatibility projection of canonical state;
- TXT, JSON, CSV, and HTML use consistent reportability rules;
- automatic reports do not silently overwrite existing reports;
- TCP scanning does not send application payloads unless banner collection is explicitly enabled;
- banner collection follows the common TLS, probing, sanitization, and output-length policies;
- HTML output escapes untrusted target and service content;
- CSV output neutralizes formula cells.

Any change to these contracts requires tests in the same commit.

## Multi-Target and Concurrency Guarantees

Contributions affecting orchestration must preserve:

- deterministic target expansion;
- target deduplication;
- explicit exclusions;
- bounded target concurrency;
- bounded port concurrency;
- the global semantics of `--threads`;
- endpoint identity;
- partial-failure isolation;
- cooperative cancellation;
- reproducible reporting.

Concurrency limits must not be silently multiplied per target.

## Session and Artifact Guarantees

Changes affecting persistence or artifacts must preserve the applicable security guarantees for:

- Session Store v2;
- resumable sessions;
- immutable execution plans;
- checkpoints;
- migration behavior;
- secure artifact creation;
- restrictive filesystem permissions;
- atomic replacement;
- symlink rejection;
- non-overwrite behavior;
- output sanitization.

Historical source data used for migration or audit must not be destructively modified without explicit authorization.

## Required Validation

Before committing a functional change, run the applicable local validation:

```bash
./scripts/build_all.sh
./scripts/test_all.sh
bash -n scripts/*.sh
shellcheck scripts/*.sh
```

Python:

```bash
python -m pytest -v --cov=src --cov-report=term-missing
```

Rust:

```bash
cargo fmt --manifest-path rust-core/Cargo.toml -- --check

cargo clippy \
  --manifest-path rust-core/Cargo.toml \
  --all-targets \
  --all-features \
  -- -D warnings

cargo test --manifest-path rust-core/Cargo.toml
```

Go commands are executed from `go-banner/`:

```bash
go test -race ./...
```

Release-candidate or release-related changes additionally require the applicable release validation:

```bash
python -m pip install -r requirements-release.txt
./scripts/build_release_artifacts.sh
./scripts/test_release_artifacts.sh dist
./scripts/audit_dependencies.sh
```

A change must not be integrated while a required validation check is failing.

## Tests

Every behavior-changing defect correction should include an appropriate regression test.

Changes to contracts, parsers, bridges, native engines, persistence, output formats, security controls, or orchestration should update the corresponding tests in the same commit.

Network tests should prefer deterministic loopback fixtures.

Do not make CI depend on uncontrolled external infrastructure.

## Security-Sensitive Changes

Changes that affect any of the following require explicit review:

- network behavior;
- target expansion;
- protocol probing;
- native process execution;
- privilege requirements;
- file permissions;
- artifact paths;
- session persistence;
- secrets or credentials;
- dependency or supply-chain controls;
- release workflows;
- output sanitization;
- public contracts.

A contribution must not silently expand CicadaPort into vulnerability detection, exploitation, raw scanning, unrestricted discovery, destructive testing, or arbitrary offensive scripting.

## Dependencies and Supply Chain

Dependency changes must be deliberate and reviewable.

Do not:

- remove integrity controls without justification;
- weaken pinned or hashed release dependencies without review;
- replace pinned GitHub Actions with floating references;
- bypass dependency auditing;
- disable secret scanning or security analysis to make CI pass;
- commit vendored binaries or generated artifacts without an approved reason.

Release and supply-chain controls are part of the project's security boundary.

## Commits

Keep commits:

- atomic;
- focused;
- reviewable;
- reproducible;
- appropriately tested.

Do not commit:

- generated scan reports;
- build directories;
- native build outputs;
- virtual environments;
- caches;
- local credentials;
- secrets;
- access tokens;
- recovery codes;
- private evidence;
- unrelated temporary files.

Use clear Conventional Commit-style messages where practical.

Examples:

```text
fix(scanner): preserve canonical result state
test(integration): verify native localhost parity
docs(security): align vulnerability reporting policy
chore(governance): update repository ownership metadata
```

## Pull Requests

A pull request should explain:

- the problem or requirement;
- the behavior before the change;
- the behavior after the change;
- affected components;
- security implications;
- compatibility implications;
- validation performed.

Do not merge while required CI checks are failing.

Keep unrelated implementation, documentation, release, and governance changes separate whenever practical.

## Historical Provenance

CicadaPort preserves historical authorship and engineering evidence.

Organizational migration to Averlyth does not rewrite:

- Git authorship;
- signed commits;
- signed tags;
- release records;
- historical contracts;
- audit evidence;
- engineering baselines.

Older documentation may contain lifecycle states that were valid at the time of creation. Such evidence should remain historically accurate rather than being retroactively rewritten.

## License

By contributing, you agree that your contribution may be distributed under the project's [MIT License](LICENSE.md).
