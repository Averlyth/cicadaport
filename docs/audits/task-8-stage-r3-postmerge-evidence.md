# CicadaPort TASK 8 — Stage R.3 postmerge evidence and 8.7 disposition review

**Evidence cutoff:** 2026-10-09 UTC (2026-10-08 Bolivia).
**Document state:** PROPOSED; requires an independently signed documentary
commit, source-branch CI, PR CI, protected merge and exact-main postmerge CI.
**Scope:** verified source on protected main; not a published RC3 or stable release.
**Decision authority:** project architect. No acceptance is implied by this file.

## Signed lineage and immutable evidence

| Control | Verified record | Outcome |
| --- | --- | --- |
| Prior protected main | `b57a3f011f88fe917323a2eb8c9d12c7fcedaeee` | SIGNED VERIFIED |
| Stage R.2 documentation | `4ef7d5d2bdd96645138a93f19fe49423ad20c8a0` | SIGNED VERIFIED |
| Stage R.3 security source | `08d3d76a4e3873d786bb13eeecc31aacfcc62dc2` | SIGNED VERIFIED |
| PR #39 | <https://github.com/Averlyth/cicadaport/pull/39> | MERGED, merge method |
| Protected-main merge | `71afe74e5872f69218f149828103cf041e3079dc` | GITHUB SIGNATURE VALID |
| Merge parents | `b57a3f011f88fe917323a2eb8c9d12c7fcedaeee`, `08d3d76a4e3873d786bb13eeecc31aacfcc62dc2` | VERIFIED |
| Exact candidate tree | `1137273d3b74aa00f6520d14c963904b531f85bc` | VERIFIED |
| Branch push CI | <https://github.com/Averlyth/cicadaport/actions/runs/37866204381> | 28/28 PASS |
| PR CI | <https://github.com/Averlyth/cicadaport/actions/runs/37866864489> | 27 PASS, 1 expected SKIP; SUCCESS |
| Main postmerge CI | <https://github.com/Averlyth/cicadaport/actions/runs/37867530902> | 28/28 PASS |
| Ruleset | `20137979` | ACTIVE, 25 required contexts |

## Security regression and remediated state

Stage R.2 branch CI `37856976966` failed the **Dependency audits** gate:
`govulncheck` found reachable `GO-2026-6607` in Go 1.26.8 standard-library
`crypto/tls`, exercised via Go banner connection/read/write paths. This
negative evidence is retained; it must not be overwritten as a passing run.

Stage R.3 pinned **Go 1.26.9** in all five CI setup-go steps, `.go-version`,
`setup.py`, tooling validation, audit policy and active documentation.
The fix was verified by independent local security tests and exact-main
`37867530902` dependency audits and Go checks. Tests, coverage, reproducible
wheel/sdist builds, installed-artifact matrix, Python/Rust/Go security audits,
SAST, ShellCheck, Rust fmt/Clippy, Go race, SLSA/CycloneDX provenance and
signature verification all passed their applicable CI jobs.

The CI job is still named `Go 1.26.8` because ruleset `20137979` requires
that status **label**. The job verifies the real Go runtime equals
`go1.26.9`. Do not rename the check without a separate authorized and
validated ruleset migration.

Local Stage R.3 check: 535 passed, 2 skipped, 72 subtests passed; Python
coverage 82.25%. These checks validate the stated matrix and controls;
no assertion of exhaustive vulnerability freedom or production endurance
is made.

## Residual risks requiring explicit architect disposition

| Risk ID | Verified or bounded observation | Required decision |
| --- | --- | --- |
| `R-SEC-NATIVE-01` | GitHub-native Dependabot/security alert inventories disabled or unavailable; code scanning lacked analysis at earlier review. CI audits, Bandit and Gitleaks passed. | Establish native inventory/coverage or explicitly accept compensating controls and limits |
| `R-OPS-SOAK-01` | Ten synthetic bounded-resource soak repetitions passed. No production-duration soak or production workload claim. | Accept bounded validation as sufficient for current source milestone or require endurance evidence |
| `R-DOC-STATE-01` | Source and current-version docs corrections are merged in PR #39. This postmerge audit is only proposed at creation. | Approve documentary consistency only after this record passes a separate protected PR/postmerge gate |
| `R-SEC-BLOCKERS-01` | Successful scanners and zero open GitHub issue/PR counts cannot prove no remaining security/operational blockers. | Independently enumerate/classify blocking risks and explicitly decide acceptance or remediation |

## Final acceptance checklist — intentionally unsigned and undecided

- [x] Stage R.3 source remediated: Go 1.26.9, reachable old TLS advisory resolved
  for the audited candidate.
- [x] Original signed source history and exact merged tree verified.
- [x] Main CI 28/28; reproducible package, signed provenance and SBOM verified.
- [x] Protected main ruleset and mandatory status contexts preserved.
- [ ] This new documentary evidence has been merged through protected PR and
  passed exact-main postmerge CI.
- [ ] `R-SEC-NATIVE-01` assigned an explicit decision and rationale.
- [ ] `R-OPS-SOAK-01` assigned an explicit decision and rationale.
- [ ] `R-DOC-STATE-01` closed through an independently verified document merge.
- [ ] `R-SEC-BLOCKERS-01` blocking-risk inventory and disposition approved.
- [ ] Architect has approved final SUBTASK 8.7 acceptance, with explicit
  limits and evidence binding.

## Formal state at evidence cutoff

```text
STAGE_Q=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
STAGE_R3_SOURCE=MERGED_SIGNED_VERIFIED
STAGE_R3_EXACT_MAIN=71afe74e5872f69218f149828103cf041e3079dc
STAGE_R3_EXACT_MAIN_CI=37867530902_PASS_28_OF_28
STAGE_R3_DOCUMENTATION_GATE=PREPARED_PENDING_INTEGRATION
STAGE_R3_GO_SECURITY=REMEDIATED_AND_AUDITED
STAGE_R3_NATIVE_ALERTS=UNVERIFIED
STAGE_R3_PRODUCTION_DURATION_SOAK=NOT_DEMONSTRATED
STAGE_R3_RESIDUAL_RISK_DECISION=PENDING_ARCHITECT
SUBTASK_8_7=FINAL_ACCEPTANCE_PENDING
SUBTASK_8_8=BLOCKED
SUBTASK_8_9=BLOCKED
RC3_TAG=NOT_CREATED
RC3_PUBLICATION=NOT_AUTHORIZED
STABLE_RELEASE=NO_GO
```

No generated CI artifact is a published GitHub Release, and a source RC3
candidate is not evidence of authorization for stable distribution.
