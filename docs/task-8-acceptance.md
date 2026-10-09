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

## Stage R — Post-Stage-Q enterprise acceptance review

**Evidence date:** 2026-10-08.

**Scope:** source candidate `3.0.0-rc.3` integrated into
`main@b57a3f011f88fe917323a2eb8c9d12c7fcedaeee`.
This is not a published release.

### Integration and CI evidence

- PR #37: source RC3 integrated and verified.
- PR #38: security dependency reconciliation and Stage L
  acceptance evidence integrated through a verified signed merge.
- Postmerge CI run `37850121564`: 28/28 jobs successful.
- Repository governance: 25 required status contexts.
- Dependabot PRs #32–#36: closed as superseded, without individual
  merges; their original branch SHAs were restored and verified.
- Original signed source and merge histories remain preserved.

### Technical control matrix

| Area | Verified result | Acceptance interpretation |
| --- | --- | --- |
| Python supported matrix | PASS | Ubuntu 22.04/24.04; Python 3.10–3.13 |
| Rust tests, fmt, Clippy and build | PASS | Exact-main CI |
| Go tests, vet, race and build | PASS | Exact-main CI |
| Python quality and resource hygiene | PASS | Black, Flake8, Mypy and warnings gate |
| Python coverage | PASS | Required floor >=82% enforced |
| Integration and installed artifacts | PASS | Supported-platform CI matrix |
| Dependency audits and SAST | PASS | CI controls, not an absolute safety guarantee |
| Secret scanning | PASS | Gitleaks CI job; not native GitHub alert coverage |
| Release lock and reproducibility | PASS | Exact-main build workflow |
| CycloneDX SBOM and attestations | PASS | CI signing and verification steps |
| Bounded synthetic soak | PASS | Ten iterations, not production endurance |
| Native GitHub alerts | NOT VERIFIED | Disabled or no analysis registered |
| Documentary current state | REMEDIATION IN PROGRESS | Requires protected integration |
| Residual risk acceptance | PENDING | Requires explicit architect disposition |

### Open risk and decision register

**R-SEC-NATIVE-01:** Native Dependabot alerts and secret-scanning
alerts are disabled; Code Scanning reports no analysis. The
repository's CI provides existing compensating controls, but
unavailable native inventories cannot be represented as empty.
Enabling native security features is a separate governance decision.

**R-OPS-SOAK-01:** Ten repeated synthetic bounded-resource tests
passed. No production-duration endurance evidence has been
established from those runs. Acceptance of this limited scope
requires an explicit decision; no production soak is inferred.

**R-DOC-STATE-01:** Current-version references in SECURITY.md
and ROADMAP.md required correction. Historical RC2 and TASK 4
records remain preserved. Document compliance requires review
and protected integration of the corrective changes.

**R-SEC-BLOCKERS-01:** Zero open GitHub issues or pull requests
does not prove `OPEN_BLOCKERS=0`. Final security and operational
risk classification remains a human acceptance gate.

### Formal boundary

```text
STAGE_Q=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
STAGE_R=ACCEPTANCE_REVIEW_IN_PROGRESS
STAGE_R_TECHNICAL_CI=PASS_28_OF_28
STAGE_R_NATIVE_SECURITY_INVENTORY=UNVERIFIED
STAGE_R_DOCUMENTARY_RECONCILIATION=PENDING_INTEGRATION
STAGE_R_RISK_DISPOSITION=PENDING
SUBTASK_8_7=FINAL_ACCEPTANCE_PENDING
SUBTASK_8_8=BLOCKED
SUBTASK_8_9=BLOCKED
RC3_PUBLICATION=NOT_AUTHORIZED
STABLE_RELEASE=NO_GO
```

The remaining gates must not be marked successful merely because
this audit record has been created.

## Stage R.3 — New reachable Go standard-library advisory

The `push` CI associated with source commit
`4ef7d5d2bdd96645138a93f19fe49423ad20c8a0`
failed the **Dependency audits** job. The remaining passing jobs do
not override that failure. `govulncheck` reported `GO-2026-6607`:
reachable `crypto/tls` standard-library logic in Go 1.26.8.
The affected call paths include the Go banner engine's TLS
connection, incremental read and complete write operations.

Security remediation candidate: Go 1.26.9, exact-pinned across
`.go-version`, all five CI Go installations, `setup.py`,
`scripts/check_tools.sh`, `scripts/build_all.sh`, and audit policy.
The release candidate number is unchanged; artifacts must be
rebuilt and revalidated at the new signed commit SHA.

The GitHub main ruleset still requires status context `Go 1.26.8`;
that **job label** is temporarily preserved. It is not the runtime
version, which must be 1.26.9. Renaming the check without updating
ruleset 20137979 would prevent protected integration.

```text
STAGE_R3_VULNERABILITY=GO-2026-6607_REACHABLE_GO_1_26_8
STAGE_R3_FIXED_TOOLCHAIN_CANDIDATE=GO_1_26_9
STAGE_R3_SECURITY_AUDIT=PENDING_NEW_CI
STAGE_R3_BUILD_AND_ATTESTATIONS=PENDING_NEW_CI
STAGE_R3_RULESET_LEGACY_CONTEXT=PRESERVED
SUBTASK_8_7=FINAL_ACCEPTANCE_PENDING
SUBTASK_8_8=BLOCKED
SUBTASK_8_9=BLOCKED
STABLE_RELEASE=NO_GO
```

This is prospective remediation evidence, **not** proof of a
successful new audit, zero security blockers or production endurance.


## Stage R.3 — Postmerge technical-evidence verification (2026-10-09 UTC)

The earlier R.3 section is an immutable prospective snapshot. Subsequent
verified facts supersede its pending statuses **only for the later evidence
cutoff**, without altering the failed Stage R.2 run.

- PR #39 protected-merged the signed Stage R.2 and R.3 commits into
  `main@71afe74e5872f69218f149828103cf041e3079dc`.
  The GitHub merge signature and both merge parents are verified; candidate
  tree: `1137273d3b74aa00f6520d14c963904b531f85bc`.
- Branch push CI `37866204381`: 28/28 successful jobs.
- PR CI `37866864489`: successful; 27 jobs passed and the push-only
  attestation-verification job was skipped, without a failed job.
- Exact-main postmerge CI `37867530902`: 28/28 successful jobs. The
  reproducibility, installed-artifact matrix, signed SLSA and CycloneDX
  attestation generation, delivery verification, security audits, SAST,
  operational synthetic soak and integration jobs passed.
- Local Stage R.3 evidence: Python 3.13, 535 passed, 2 skipped,
  72 subtests passed, coverage 82.25%; Black, Flake8, Mypy, Rust, Go race,
  ShellCheck and Python/Rust/Go dependency audits passed.
- Go `1.26.9` fixes the previously reachable Go `1.26.8` TLS advisory
  `GO-2026-6607` for the validated candidate; CI and dependency audit
  verified that patched toolchain. The protected status check still carries
  the legacy label `Go 1.26.8` pending governed migration.

### Risks retained for explicit human disposition

| Risk | Evidenced observation | Gate decision |
| --- | --- | --- |
| `R-SEC-NATIVE-01` | Native GitHub alert inventories unavailable/not verified; CI compensating controls pass | PENDING: verify or explicitly accept limited visibility |
| `R-OPS-SOAK-01` | Ten bounded synthetic iterations pass; no production-duration endurance proof | PENDING: explicitly accept limits or demand further evidence |
| `R-DOC-STATE-01` | Current source/docs corrections integrated in PR #39; this final evidence record not yet merged | PENDING: independently integrate documentation with CI |
| `R-SEC-BLOCKERS-01` | Scanner PASS and issue/PR counts alone do not demonstrate zero residual blockers | PENDING: classify and approve final blocking-risk inventory |

**Disposition:** technical source validation is PASS. The four decisions
above and final SUBTASK 8.7 sign-off remain **PENDING**, not waived by CI.
SUBTASK 8.8, SUBTASK 8.9, RC3 publication and stable release remain blocked
or unauthorized. No tag or GitHub Release is created by this documentation.

Full evidence and decision fields:
[`docs/audits/task-8-stage-r3-postmerge-evidence.md`](audits/task-8-stage-r3-postmerge-evidence.md).
