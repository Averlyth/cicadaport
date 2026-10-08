# CicadaPort 3.0.0-rc.3 — release candidate under validation

**Evidence cut-off (2026-10-08, Stage G precommit):** The dependency candidate was not committed when this snapshot was produced. Exact-commit and publication decisions remain separate subsequent gates.

**Status:** source integrated via PR #37; postmerge main CI verified.
Post-baseline security dependency reconciliation is locally validated
but pending signed commit and exact-commit CI. No RC3 tag or release
has been authorized or published.

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


## Stage G: reconciled PR37 and dependency-candidate provenance

The source `3.0.0-rc.3` was integrated into `main` at
`c27d13a0e7643f1ee6cc6fd4a20e3dce14643176` via PR #37. Postmerge
GitHub Actions run `37813550182` passed all 28 jobs, including installed
artifact matrix and push-only attestation verification. This does not create
an RC3 Git tag or GitHub Release.

Security dependency updates from Dependabot #32–#36 are being combined into
a separate uncommitted candidate. The lock is stable under the canonical
Python 3.13 compiler and has SHA-256
`c1daa8a206b5835db96b7188629f1e3f95405bd93f44f0c744bce60310035cc8`.
Full local gates and Python/Rust/Go vulnerability scanners passed, with
22 changed package versions in the release lock. On the new commit, the
wheel/sdist build, reproducibility, artifact installation and CI attestation
gates must be repeated. No published artifacts should be inferred from
this preparatory candidate.

## Stage L — post-commit candidate validation (2026-10-08)

The Stage G observations above describe a precommit snapshot. The proposed
security dependency reconciliations were subsequently committed, signed and
validated as `c0a1ace88cea37a4ad59303ff9d40c54b49b4788` (tree
`ed00bebc0ca4897f127a2e21ea7d1bcf681bbeaf`). The release lock retains
SHA-256 `c1daa8a206b5835db96b7188629f1e3f95405bd93f44f0c744bce60310035cc8`.

The local exact-commit release build passed reproducibility, signed-source
identity checks, installed wheel/sdist smoke tests, hash verification, manifest
and CycloneDX inventory verification. Both branch `push` runs, `37822525656`
and `37823691270`, passed all 28 jobs including OIDC-backed attestation build
and artifact provenance verification. The permanent branch was advanced by
fast-forward, without rebase, history rewrite or a merge to `main`.

**Release barrier:** this candidate is not a published GitHub Release, and its
dependency changes are not yet integrated into `main`. No RC3 tag or artifact
publication is authorized. A future documentation commit or other change
creates a *new* source SHA and requires its own relevant quality, release and
remote acceptance evidence before any protected merge or release decision.
