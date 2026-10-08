# TASK 8 — Enterprise acceptance and GO/NO-GO evidence ledger

**State:** candidate definition; no publication authorized.

## Local implementation evidence

- Python 3.13: 531 passed, 2 skipped, 72 subtests; 82% coverage.
- Resource hygiene: 53 tests, 14 subtests; no SQLite warning reproduced.
- Black, Flake8, Mypy full-source: passed after remediation.
- TASK 6 plus runtime/session subset: 282 passed.
- Dependency backlog PR #19 closed as superseded; PR #31 merged at
  `67b900b4c378d766b8829231b3e9e930baceac71` with post-merge CI
  `37698558022` successful.

## RC3-specific acceptance — pending remote evidence

- [ ] Signed implementation commit and all premerge CI jobs successful.
- [ ] Python 3.10–3.13 on Ubuntu 22.04/24.04 with coverage floor.
- [ ] Black/Flake8/Mypy/resource-warning gates.
- [ ] Rust fmt, Clippy, tests and release build.
- [ ] Go formatting, vet, race tests and build.
- [ ] ShellCheck, Gitleaks, Bandit and dependency audits.
- [ ] Release-lock, action SHA pins and reproducible wheel/sdist build.
- [ ] Installed-artifact/CLI/TUI smoke on every supported target.
- [ ] Configuration, health/readiness, session recovery and cancellation.
- [ ] Bounded-resource synthetic soak in ten independent repetitions.
- [ ] SLSA provenance and CycloneDX SBOM signed with OIDC on `push`.
- [ ] `gh attestation verify` and delivery hash checks on exact commit.
- [ ] Protected merge and exact `main` post-merge CI pass.
- [ ] Independent RC3 tag / prerelease authorization and publication.
- [ ] Review of outstanding security/service blockers before stable GO.

**Decision:** RC3 acceptance remains pending. Stable v3.0.0 is NO-GO
until all applicable boxes have been verified and the architect
explicitly authorizes publication.

## New Dependabot proposals opened after the baseline

At RC3 source preparation, GitHub reports 5 new open proposals (PRs #32, #33, #34, #35, #36). They are **not** part of the previously closed initial dependency backlog. A separate security, affected-code-path and compatibility assessment must precede final stable GO/NO-GO, especially for wheel advisory `GHSA-vgq5-9859-3mmw`. RC3 publication remains unapproved.
