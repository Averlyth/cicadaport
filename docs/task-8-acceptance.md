# TASK 8 — Enterprise acceptance and GO/NO-GO evidence ledger

**Evidence cut-off (2026-10-08, Stage G precommit):** Pending commit, CI and publication statements describe the state at evidence capture. Later results must be recorded separately without retroactively changing this snapshot.

**State:** PR #37 source CI and main integration verified; dependency
reconciliation is locally validated and not yet committed.
RC3 tagging/publication and stable release are not authorized.

## Historical local implementation evidence (pre-PR37 snapshot)

- Python 3.13: 531 passed, 2 skipped, 72 subtests; 82% coverage.
- Resource hygiene: 53 tests, 14 subtests; no SQLite warning reproduced.
- Black, Flake8, Mypy full-source: passed after remediation.
- TASK 6 plus runtime/session subset: 282 passed.
- Dependency backlog PR #19 closed as superseded; PR #31 merged at
  `67b900b4c378d766b8829231b3e9e930baceac71` with post-merge CI
  `37698558022` successful.

## RC3 source acceptance — PR37 remote CI verified, publication pending

- [x] Signed implementation commit and all premerge CI jobs successful.
- [x] Python 3.10–3.13 on Ubuntu 22.04/24.04 with coverage floor.
- [x] Black/Flake8/Mypy/resource-warning gates.
- [x] Rust fmt, Clippy, tests and release build.
- [x] Go formatting, vet, race tests and build.
- [x] ShellCheck, Gitleaks, Bandit and dependency audits.
- [x] Release-lock, action SHA pins and reproducible wheel/sdist build.
- [x] Installed-artifact/CLI/TUI smoke on every supported target.
- [x] Configuration, health/readiness, session recovery and cancellation.
- [x] Bounded-resource synthetic soak in ten independent repetitions.
- [x] SLSA provenance and CycloneDX SBOM signed with OIDC on `push`.
- [x] `gh attestation verify` and delivery hash checks on exact commit.
- [x] Protected merge and exact `main` post-merge CI pass.
- [ ] Independent RC3 tag / prerelease authorization and publication.
- [ ] Review of outstanding security/service blockers before stable GO.

**Decision:** RC3 acceptance remains pending. Stable v3.0.0 is NO-GO
until all applicable boxes have been verified and the architect
explicitly authorizes publication.

## New Dependabot proposals opened after the baseline

At RC3 source preparation, GitHub reports 5 new open proposals (PRs #32, #33, #34, #35, #36). They are **not** part of the previously closed initial dependency backlog. A separate security, affected-code-path and compatibility assessment must precede final stable GO/NO-GO, especially for wheel advisory `GHSA-vgq5-9859-3mmw`. RC3 publication remains unapproved.


## Stage G: reconciled PR37 source and local security validation

PR #37 (signed implementation commit `5eb2ebfaaa4f701871b787a1c1420863b03cb36c`)
was merged into `main` as `c27d13a0e7643f1ee6cc6fd4a20e3dce14643176`.
Premerge push CI `37788101220`, pull-request CI `37788678813` and
postmerge main CI `37813550182` passed; the last run completed 28/28 jobs,
including the push-only verification of artifact signatures and provenance.
Local GPG verification of the GitHub merge signature succeeded with the
explicitly checked official web-flow public key fingerprint.

The subsequent security update is not yet committed or present in `main`.
Its proposed direct source changes are `tokio 1.53.2`, `wheel 0.48.0`,
`setuptools 84.0.0` build compatibility, `black >=26.10.0,<27`, and
`build 1.6.1`. The regenerated release lock also changes 19 transitive
versions (22 version changes total). `filelock` moves from 3.32.2 to 4.0.12;
its release-toolchain behavior still requires exact-commit package validation.

Local Stage D: pinned source changes and generated locks validated. Stage E:
16/16 source-quality, Python, Rust, Go, shell and structural checks passed.
Stage F: hash-locked Python installation, `pip check`, `pip-audit --strict`,
RustSec `cargo audit`, `govulncheck v1.1.4` and Python build dependency
specifier checks passed. Scanners did not report known vulnerabilities.
These observations are local and do **not** certify the modified candidate
against remote CI or artifact reproducibility.

```text
PR37_SOURCE_ACCEPTANCE=PASS
PR37_POSTMERGE_MAIN_CI=37813550182_PASS_28_OF_28
POST_BASELINE_DEPENDENCY_INTAKE=LOCALLY_RECONCILED_UNCOMMITTED
POST_BASELINE_DEPENDENCY_RELEASE_LOCK_DELTAS=22
DEPENDENCY_LOCAL_SECURITY_CHECKS=PASS
DEPENDENCY_REMOTE_CI=PENDING_COMMIT_AND_PR
DEPENDENCY_WHEEL_SDIST_REPRODUCIBILITY=PENDING_EXACT_COMMIT
DEPENDABOT_PRS_32_TO_36=OPEN_PENDING_SOURCE_PR_RESOLUTION
RC3_TAG=NOT_CREATED
RC3_PUBLICATION=NOT_AUTHORIZED
STABLE_GO_NO_GO=NOT_EXECUTED
STABLE_PUBLICATION=NOT_AUTHORIZED
```

The PR37 source-level checklist is complete except the independent
publication and final stable security/operational review decisions above.
Those decisions must not be inferred from local Stage D–F results.

## Stage L — later evidence and unresolved acceptance gates (2026-10-08)

This addendum supersedes Stage G **only as a current snapshot**; it does not
rewrite or invalidate that historical precommit evidence.

- Signed dependency commit: `c0a1ace88cea37a4ad59303ff9d40c54b49b4788`;
  GitHub verifies its SSH signature (`verified=true`, `reason=valid`).
- Local Stage I: reproducible release artifact set (7 compared files), clean
  wheel/sdist installation and smoke tests outside the checkout, checked hashes,
  CycloneDX SBOM, release manifest and exact committed-tree identity.
- Reconciliation branch `push` CI: [37822525656](https://github.com/Averlyth/cicadaport/actions/runs/37822525656),
  28/28 jobs successful on the exact signed commit.
- Permanent productization branch `push` CI:
  [37823691270](https://github.com/Averlyth/cicadaport/actions/runs/37823691270),
  28/28 jobs successful on the same SHA. The attestation-build and verification
  jobs succeeded in both workflows.
- The CI contract executes 10 separate iterations of the synthetic
  TASK 6.5 resilience test. This is not evidence of a production-length soak.
- Dependabot PRs #32, #33, #34, #35 and #36 remain open, pending independent
  superseded-resolution **after** the equivalent updates enter `main`.

**Acceptance boundary:** the source candidate's technical gates have passed on
signed branch pushes. However, the new dependency source is not merged to
`main`, PR-level checks for the future consolidated PR have not run, and no
post-merge CI attests to this updated `main` state. Final closure of SUBTASK 8.7,
independent RC3 publication, and SUBTASK 8.8 stable GO/NO-GO remain pending.

```text
STAGE_L_DEPENDENCY_RECONCILIATION=TECHNICALLY_VALIDATED_ON_BRANCH
STAGE_L_FINAL_8_7_ACCEPTANCE=PENDING_FORMAL_DECISION_AND_INTEGRATION
STAGE_L_SECOND_PR=PREPARATION_ONLY_NOT_CREATED
STAGE_L_DEPENDABOT_SUPERSESSION=PENDING_MAIN_INTEGRATION
STAGE_L_RC3_TAG_AND_PUBLICATION=NOT_AUTHORIZED
STAGE_L_STABLE_GO_NO_GO=NOT_EXECUTED
STAGE_L_STABLE_PUBLICATION=NOT_AUTHORIZED
```
