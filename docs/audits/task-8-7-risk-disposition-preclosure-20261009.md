# CicadaPort TASK 8 — SUBTASK 8.7 residual-risk disposition and preclosure record

**Record:** `RD-CICADAPORT-8.7-20261009-001`
**Evidence cutoff:** 2026-10-09 UTC, after PR #41 and its exact-main postmerge controls.
**Contract context:** `SRP-CICADAPORT-TASK-8-001`, `1.0-CANDIDATE`.
**Record state at creation:** `ARCHITECT_DISPOSITION_AUTHORIZED; DOCUMENTARY_PR_PENDING`.
**SUBTASK 8.7:** `FINAL_ACCEPTANCE_PENDING` — this document does not close it.
**Decision authority:** project architect. This is a *bounded source-milestone risk disposition*, not permission to publish or declare production readiness.

## 1. Immutable integration and technical verification

| Verified surface | Evidence | Disposition |
| --- | --- | --- |
| Stage R.3 Go standard-library fix | [PR #39](https://github.com/Averlyth/cicadaport/pull/39), main `71afe74e5872f69218f149828103cf041e3079dc`, CI [37867530902](https://github.com/Averlyth/cicadaport/actions/runs/37867530902) | Signed integrated change; Go 1.26.9 replaces vulnerable Go 1.26.8 runtime |
| Documentary source reconciliation | [PR #40](https://github.com/Averlyth/cicadaport/pull/40), main `bec9cf819f58bd1514e1cc42ebfe0d74eb41e4bb`, CI [37874547848](https://github.com/Averlyth/cicadaport/actions/runs/37874547848) | Signed, protected integration and 28/28 postmerge checks |
| CodeQL security correction | [PR #41](https://github.com/Averlyth/cicadaport/pull/41), signed source `029441be952fee456f86876460c146a920acfc93` | Four files only; +151 / -1; no release/tag |
| Protected merge #41 | Main `3812d08add81e11dd65cae4bef9e9e66d41c27b7`; parents `bec9cf819f58bd1514e1cc42ebfe0d74eb41e4bb` and `029441be952fee456f86876460c146a920acfc93` | Valid GitHub merge signature; tree `a1ef133bd9fa782cfb3ae47fb603d0d72c967965` |
| Exact-main push CI | [37947441267](https://github.com/Averlyth/cicadaport/actions/runs/37947441267) | 28/28 jobs SUCCESS; release artefact checks, attestation verification, audits, test matrix |
| Exact-main native CodeQL | [37947442615](https://github.com/Averlyth/cicadaport/actions/runs/37947442615) | 4/4 analyzers SUCCESS: Go, Python, Rust and GitHub Actions |
| Branch governance | Ruleset `20137979` | Active; 25 required checks; strict validation and PR-only integration |

The historical audits `docs/audits/task-8-stage-l-acceptance-review.md`,
`docs/audits/task-8-stage-r3-postmerge-evidence.md`, and historical subsections
of `docs/task-8-acceptance.md` are evidence snapshots. Their earlier
`PENDING` and `UNVERIFIED` statements are preserved at their own cutoffs,
not silently rewritten. This record adds the later verified disposition.

## 2. Classification and architect-authorized bounded dispositions

| Risk ID | Classified evidence and residual exposure | Architect disposition for **source milestone only** |
| --- | --- | --- |
| `R-DOC-STATE-01` | Document repairs in protected PR #40, valid signature and 28/28 main CI. Older audit snapshots remain historical. | **Technical remediation verified.** Administrative closure may be recorded only after this document is protected-merged, exact-main postmerge CI passes and the architect formally closes SUBTASK 8.7. |
| `R-SEC-NATIVE-01` | Dependabot alerts enabled; Dependabot security updates deliberately disabled. Secret Scanning and Push Protection enabled; CodeQL default setup scans four analyzers. Latest verified native open alert inventory: fixed Python #1, open HIGH TLS #2; Dependabot and secret scanning previously reported zero open alerts. GitHub SBOM observed 92 PURL packages, 81 versioned and 11 unversioned. | **Coverage operational with bounded visibility; limitations classified for source review, not independently accepted as exhaustive.** Zero alerts do not prove no vulnerabilities; 11 unversioned entries do not constitute exhaustive dependency inventory. Retain native scanning and review new alerts. |
| `R-OPS-SOAK-01` | Ten CI repetitions of bounded-resource synthetic TASK 6.5 soak succeeded, including exact-main CI. No production-duration or production-workload endurance test has been demonstrated. | **Explicitly ACCEPTED for current source milestone only.** No production endurance, SLO attainment, sustained workload or stable-release readiness is inferred. Reevaluate for deployment/release decisions. |
| `R-SEC-BLOCKERS-01` | Source CI, security audits, installed artefacts, and CodeQL execution pass. One specifically identified CodeQL HIGH remains open: #2. No statement that all security/operational blockers in all environments are absent is supportable. | **Bounded source acceptance of known TLS exposure only**, subject to the controls below; new critical/high findings or violations of the trust boundary require fresh blocking-risk review. `OPEN_BLOCKERS=0` for stable GO is **NOT** certified. |

## 3. Residual TLS risk — explicitly bounded acceptance

**Finding:** [CodeQL alert #2](https://github.com/Averlyth/cicadaport/security/code-scanning/2), rule
`go/disabled-certificate-check`, HIGH, `go-banner/main.go`; `state=OPEN` at
this cutoff. The use of `tls.Config{InsecureSkipVerify: true}` is a real failure
to authenticate the remote endpoint, **not a false positive**. Active MITM,
endpoint impersonation, and untrusted banners/HTTP headers remain possible.

The architect **authorizes acceptance only in the Go engine's intentionally
unauthenticated reconnaissance path** under all of these enforceable limits:

1. Operator must own or have explicit permission to assess each target; no
   expansion of scope, privilege or offensive capabilities is authorized.
2. Transport is exclusively passive banner observation or canonical,
   credential-free `HEAD / HTTP/1.0`; the pre-dial plan guard rejects
   disallowed descriptors and noncanonical payloads.
3. No credentials, tokens, cookies, authenticated HTTP calls, privileged
   actions, software updates, release verification or trusted client APIs
   can use this unverified TLS connection. Minimum TLS version is 1.2.
4. Results must represent `certificate_verified=false` and
   `verification_not_performed_observation_mode`; collected identity and
   service evidence is **untrusted observational evidence**, not proof of
   endpoint authenticity.
5. Any reuse outside this boundary or any regression in these invariants
   invalidates the present risk acceptance and requires review and remediation.

**CodeQL disposition:** Keep alert #2 OPEN as HIGH; **do not dismiss**, suppress,
relabel as false positive or treat passing analysis as remediation. The
bounded acceptance is a documented architectural decision, not a scanner
exception or a certificate-verification claim. Alert #1 `py/bad-tag-filter`
was **FIXED** at `2026-10-09T14:53:38Z`; no dismissal was needed.

## 4. Supporting control limits and evidence ownership

- Local remediated branch: Go 1.26.9 race tests and `go vet` PASS;
  Python 3.13: 536 passed, 2 skipped, 72 subtests passed; Black,
  Flake8, Mypy and supply-chain checks PASS; 11/11 static contracts PASS.
- Main CI checks build/reproducibility, installation on Ubuntu 22.04 and
  24.04 (Python 3.10–3.13), Rust 1.97.1, Go 1.26.9 (the required check
  **label** remains `Go 1.26.8`), shell and dependency audits, secret scan,
  CycloneDX/SLSA and signed artefact verification.
- The code-scanning alert states, secret/dependency alert counts and SBOM
  inventory are timestamped operational observations. The current inventory
  must be rechecked before an irreversible final acceptance or release
  decision; no absence-of-vulnerabilities guarantee is made.
- Current GitHub Releases inventory includes published `v3.0.0-rc.1`;
  source RC3 `3.0.0-rc.3` remains unpublished. No new RC3 tag or release
  is authorized by this document.

## 5. Independent documentary integration and final human gate

This record is the **single new documentary delta** for this disposition.
It requires its own signed source commit, isolated documentation branch,
branch push CI, protected PR, PR CI, explicit permission for that PR's merge,
verified signed merge, and exact-main postmerge CI. These future results
**must not be marked PASS until observed**. If the protected base moves,
repeat the exact-SHA preflight and reauthorize if required.

Once those prerequisites have been independently verified, the architect must
make a **separate, explicit final decision** whether to accept/close/freeze
SUBTASK 8.7 based on this risk register and any new findings. Recording a
bounded TLS/soak risk acceptance here does not itself close the subtask.
SUBTASKS 8.8 and 8.9 may not begin until their gates receive distinct
express authorization. Stable release requires a separate GO/NO-GO process.

```text
TASK_8=IN_IMPLEMENTATION
PR_39=MERGED_SIGNED_VERIFIED
PR_40=MERGED_SIGNED_VERIFIED
PR_41=MERGED_SIGNED_VERIFIED
EXACT_MAIN_BASE=3812d08add81e11dd65cae4bef9e9e66d41c27b7
EXACT_MAIN_CI=37947441267_SUCCESS_28_OF_28
EXACT_MAIN_CODEQL=37947442615_SUCCESS_4_OF_4
CODEQL_ALERT_1=FIXED
CODEQL_ALERT_2=OPEN_HIGH_BOUNDED_ARCHITECT_SOURCE_RISK_ACCEPTANCE
R_SEC_NATIVE_01=COVERAGE_OPERATIONAL_LIMITS_DOCUMENTED
R_OPS_SOAK_01=BOUNDED_SOURCE_ONLY_ACCEPTED_NO_PRODUCTION_SOAK
R_DOC_STATE_01=TECHNICALLY_RESOLVED_ADMIN_CLOSURE_PENDING
R_SEC_BLOCKERS_01=TLS_KNOWN_BOUND_ACCEPTED_STABLE_BLOCKERS_NOT_CLEARED
DOCUMENTARY_PR=NOT_YET_INTEGRATED
SUBTASK_8_7=FINAL_ACCEPTANCE_PENDING
SUBTASK_8_8=BLOCKED
SUBTASK_8_9=BLOCKED
RC3_TAG=NOT_CREATED
RC3_PUBLICATION=NOT_AUTHORIZED
STABLE_RELEASE=NO_GO
```
