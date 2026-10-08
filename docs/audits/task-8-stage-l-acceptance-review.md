# CicadaPort TASK 8 — Stage L acceptance evidence and second PR preparation

**Evidence date:** 2026-10-08. **Decision:** documentation preparation only.
**Contract:** `SRP-CICADAPORT-TASK-8-001`, version `1.0-CANDIDATE`.
**Authorization limits:** no PR creation, no merge, no Dependabot closure,
no tags, no RC3/stable publication, no activation of SUBTASK 8.8 or 8.9.

## Verified provenance and source boundaries

- Previously merged source PR #37: signed implementation
  `5eb2ebfaaa4f701871b787a1c1420863b03cb36c`, merge
  `c27d13a0e7643f1ee6cc6fd4a20e3dce14643176`. Postmerge `main`
  workflow [37813550182](https://github.com/Averlyth/cicadaport/actions/runs/37813550182):
  28/28 jobs successful.
- Dependency source is a **distinct, subsequently signed commit**:
  `c0a1ace88cea37a4ad59303ff9d40c54b49b4788`; parent `c27d13a0`;
  tree `ed00bebc0ca4897f127a2e21ea7d1bcf681bbeaf`;
  GitHub signature verification is `valid`.
- Python release lock SHA-256:
  `c1daa8a206b5835db96b7188629f1e3f95405bd93f44f0c744bce60310035cc8`.
  It has 22 changed package versions relative to the parent; `filelock`
  changes from `3.32.2` to `4.0.12` (major version change).
- Stage D–F: stable source/lock generation; 16/16 local Stage E gates;
  hashed Python installation, `pip check`, `pip-audit --strict`, `cargo audit`,
  `govulncheck v1.1.4` and build backend compatibility passed. The scanners
  did not report known vulnerabilities; that is not an absolute guarantee.
- Stage I: reproducible artifact set with 7 compared files; wheel/sdist
  install and smoke outside the checkout; SHA-256 validation, CycloneDX SBOM,
  manifest, and exact commit/tree identity all passed on the signed SHA.
- Stage J: security branch push workflow
  [37822525656](https://github.com/Averlyth/cicadaport/actions/runs/37822525656),
  `success`, 28/28 jobs.
- Stage K: permanent branch was fast-forwarded to the same SHA. Push workflow
  [37823691270](https://github.com/Averlyth/cicadaport/actions/runs/37823691270),
  `success`, 28/28 jobs. Both branch workflows contain successful artifact
  build/attestation and signature/provenance verification jobs.
- `main` still points to `c27d13a0` at this evidence cutoff; the dependency
  candidate is **not** in `main`. The permanent and security source branches
  both point to `c0a1ace8`.

## Dependabot intake — independent resolution required

| PR | Proposal | Validated inclusion in candidate | Unresolved decision |
| --- | --- | --- | --- |
| #32 | `tokio` `1.53.1` -> `1.53.2` | Cargo manifest and lock, exact-version test contracts; Rust CI passes | Open, not merged or closed |
| #33 | `wheel` `0.47.0` -> `0.48.0` | Hash-pinned release lock, source build/installed-artifact checks; addresses `GHSA-vgq5-9859-3mmw` | Open, not merged or closed |
| #34 | `setuptools` `83.0.0` -> `84.0.0` | Build-system range permits `84.0.0`, lock installs and packaging passes | Open, not merged or closed |
| #35 | `black` requirement -> `>=26.10.0,<27` | Local Black 26.10.0 and CI quality gates pass | Open, not merged or closed |
| #36 | `build` `1.5.0` -> `1.6.1` | Hash-pinned release lock and wheel/sdist build gates pass | Open, not merged or closed |

All five changes have been reconciled into a candidate, not yet into `main`.
No original bot PR should be marked superseded solely because a branch passed
CI. Each bot PR needs an independent resolution after an equivalent source
change is integrated and verified on `main`.

## SUBTASK 8.7 — technical evidence versus final acceptance

The source-level Python/Rust/Go, code quality, security, dependency audit,
shell, CI matrix, operational acceptance, release, installation, supply-chain,
provenance, attestation and hash-verification gates have succeeded on the
signed candidate branch. The `ci.yml` operational job repeats the synthetic
TASK 6.5 resilience tests 10 times, which must not be relabeled as a
long-running production endurance test.

**Not yet satisfied:** the prospective second PR's exact-head checks,
protected review/merge, dependency resolution on `main`, exact `main`
postmerge CI and final human closure of SUBTASK 8.7. There is no signed,
independently authorized published RC3 tag/release. Therefore no stable GO
may be inferred from the 28/28 branch workflows.

## Second consolidated PR — proposed scope and sequencing

The second PR should originate from the permanent productization branch,
`feat/task-8-mvp-3-stable-productization`, and target `main`. It would carry
post-PR37 dependency reconciliation plus up-to-date evidence/gate preparation.
It must not claim that the backlog has been closed on `main`, that RC3 was
published, or that stable GO has already been decided.

Pre-PR requirements: documentary review, signed evidence commit if there are
changes, fresh exact-head push CI, diff review, branch protection validation,
independent human authorization to open the PR. Subsequent required gates:
PR CI and review, explicit merge authorization, protected merge, verified
`main` push CI, then independent resolution of original Dependabot PRs,
SUBTASK 8.7 decision, and finally a separately authorized 8.8/8.9 sequence.

Because the stable GO gate requires `DEPENDENCY_BACKLOG=CLOSED` and
`OPEN_BLOCKERS=0`, its final result cannot be accurately pre-certified inside
the unmerged PR that first integrates the dependency backlog. Carry the gate
mechanism and evidence preparation in the PR; record an eventual final GO/NO-GO
**after** the required integrations and review are verified.

## Explicit current decisions

```text
STAGE_L=EVIDENCE_REVIEW_COMPLETED_DOCUMENTATION_PREPARED_UNCOMMITTED
SUBTASK_8_7=SOURCE_TECHNICAL_VALIDATION_PASS_FORMAL_ACCEPTANCE_PENDING
DEPENDENCY_CANDIDATE_IN_MAIN=NO
DEPENDABOT_PRS_32_TO_36=OPEN_PENDING_INDEPENDENT_RESOLUTION
SECOND_CONSOLIDATED_PR=NOT_CREATED
PR_MERGE=NOT_AUTHORIZED
RC3_TAG=NOT_CREATED
RC3_PUBLICATION=NOT_AUTHORIZED
STABLE_GO_NO_GO=NOT_EXECUTED
SUBTASK_8_8=BLOCKED
SUBTASK_8_9=BLOCKED
STABLE_PUBLICATION=NOT_AUTHORIZED
```

Historical Stage G statements retain their original evidence cutoff; this
Stage L review is an additive later snapshot, not retroactive modification.
