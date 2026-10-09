# CicadaPort TASK 8 — Joint 8.8 + 8.9 stable source preparation

**Contract:** `SRP-CICADAPORT-TASK-8-001` (`1.0-CANDIDATE`).
**Frozen predecessor:** `SUBTASK_8_7=COMPLETED_CONSOLIDATED_CLOSED_FROZEN`.
**Authorized baseline:** `main@9f854be4919832b0d40c06321e3dd5bf9254f56d`.
**Branch:** `feat/task-8-8-9-stable-release`.
**Scope of this change:** consistent stable **source candidate**, not publication.

## 1. Boundaries and release identity

The source version and built-package identity are prepared as `3.0.0`
(PEP 440 / SemVer) while CI and pull-request validation remain mandatory.
The distribution is still **unpublished**, so changing the project version
and development classifier must not be presented as a completed stable GO.

- Linux x86_64 on Ubuntu 22.04 and 24.04 only, Python 3.10–3.13.
- Rust 1.97.1 and Go 1.26.9; legacy **check name** `Go 1.26.8` retained
  under protected-main ruleset `20137979` until separately migrated.
- No public JSONL contract changes or new reconnaissance capabilities.
- Historical RC2 and RC3 attestations, source snapshots and contracts are
  preserved, not renamed as stable evidence.

## 2. Subtask 8.8 — explicit stable GO/NO-GO gate

All eleven contractual conditions must be validated on the final signed,
merged, exact-source SHA: `DEPENDENCY_BACKLOG`, `RESOURCE_HYGIENE`,
`TEST_BASELINE`, `QUALITY_GATES`, `DOCUMENTATION`, `SERVICE_READINESS`,
`FINAL_RC`, `ENTERPRISE_ACCEPTANCE`, `SECURITY_GATES`, `SUPPLY_CHAIN`, and
`OPEN_BLOCKERS=0`. Passing ordinary CI is not a substitute for this decision.

**Known hold:** CodeQL alert #2 `go/disabled-certificate-check` is OPEN/HIGH.
Subtask 8.7 accepted unauthenticated TLS only for credential-free authorized
observation at the **source milestone**. This acceptance cannot be silently
extended to a shipped stable product. It must receive a distinct documented
stable-distribution decision, with the threat boundary and mitigation verified.
The 10 bounded synthetic soak iterations are NOT evidence of production-length
endurance. No production endurance claim or SLO is implied.

Native Dependabot, CodeQL and secret scanning inventories must be checked
with explicit, successful, nonempty parseable responses; a zero exit status
without an observed numeric count is not evidence of zero alerts.

## 3. Subtask 8.9 — staged publication contract (NOT EXECUTED)

After protected integration, exact-main CI, risk review and independent stable
GO, a **separate human release authorization** must precede any:

1. Immutable, signed annotated `v3.0.0` tag bound to the approved release SHA.
2. GitHub Release publication (not a draft or unverified CI artifact).
3. Delivery of Linux wheel, sdist, manifest, SHA-256 sums, CycloneDX SBOM,
   attestation/provenance and verification against downloaded assets.
4. Installation/smoke outside the checkout on the declared support matrix.
5. Post-release validation and a separate final TASK 8 closure decision.

No `gh release create`, tag signing, pushing tags, package upload, merge,
protected-rule bypass or external scanning is performed by this change.

## 4. Status at preparation cutoff

```text
TASK_8=IN_IMPLEMENTATION
SUBTASK_8_7=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
SUBTASK_8_8=JOINT_IMPLEMENTATION_AUTHORIZED_GO_PENDING
SUBTASK_8_9=JOINT_PREPARATION_AUTHORIZED_PUBLICATION_BLOCKED
SOURCE_VERSION=3.0.0
STABLE_GO_NO_GO=NOT_AUTHORIZED
OPEN_BLOCKERS=NOT_CLEARED_FOR_STABLE
CODEQL_ALERT_2=OPEN_HIGH
PRODUCTION_DURATION_SOAK=NOT_DEMONSTRATED
STABLE_TAG=NOT_CREATED
STABLE_PUBLICATION=NOT_AUTHORIZED
RC3_PUBLICATION=NOT_AUTHORIZED
TASK_8_FINAL_CLOSURE=PENDING
```
