# CicadaPort 3.0.0-rc.3 — release candidate under validation

**Status:** source-prepared, not yet published or tagged.

| Component | Supported or required |
| --- | --- |
| Linux | x86_64, Ubuntu 22.04 and 24.04 |
| Python | 3.10, 3.11, 3.12 and 3.13 |
| Rust | 1.97.1, mandatory TCP Connect engine |
| Go | 1.26.8, mandatory when banner evidence is enabled |
| Distribution | wheel and sdist verified outside checkout |
| Network validation | loopback and explicitly authorized targets |
| Public contracts | JSONL v1, service evidence v2 |

Windows, macOS, ARM64 and Python 3.14 are not supported in RC3.

The required candidate gates include full Python/Rust/Go tests, Black,
Flake8, full-source Mypy, a minimum 82% Python coverage, release-lock
integrity, ShellCheck, secret scanning, SAST, vulnerability audits,
cross-matrix wheel/sdist installation, reproducibility, CycloneDX SBOM
and OIDC-backed SLSA/Sigstore attestation generation and verification.

TASK 6 operational surfaces are revalidated: configuration, local
health/readiness, diagnostics, secure artifacts, recovery, cancellation,
update/rollback plans, sessions and bounded-resource synthetic soak.

Successful PR checks do not prove live OIDC attestation verification;
that requires a successful `push` workflow bound to the exact
candidate commit, and again after merge on `main`.

RC3 tag creation and GitHub Release publication are independent gates.
The old TASK 5.6 RC2 scripts, contracts, and reports remain historical
evidence; they are not relabeled as RC3 acceptance.
