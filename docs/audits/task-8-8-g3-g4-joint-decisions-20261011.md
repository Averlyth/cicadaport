# ACTA G3 + G4 — Aceptación operativa acotada y excepción de publicación RC3

**Proyecto:** CicadaPort · Averlyth · TASK 8, SUBTASKS 8.5–8.9.
**Fecha de decisión del arquitecto:** 2026-10-11.
**Registro:** `G34-CICADAPORT-8.8-20261011` · versión `1.0-DECISIÓN`.
**Base de evidencia inmutable:** `main@53a3bb06cdade11d21c0f706fbcbc3117a34abc8`.
**Contrato rector:** `SRP-CICADAPORT-TASK-8-001` (1.0-CANDIDATE).
**Alcance de esta PR:** exclusivamente documentación; no modifica código, condiciones de CI, protecciones, etiquetas ni releases.

## 1. Autoridad y alcance de la decisión

En la conversación del proyecto del 2026-10-11, el **arquitecto del proyecto aprobó expresamente y por separado**:

1. **G3:** aceptación formal de las **20 condiciones de 8.5 solo en su alcance probado**, incluida la limitación de TUI instalada, las operaciones de actualización y rollback, y los escenarios de carga. No se acepta un SLA o producción general por inferencia.
2. **G4:** **excepción procedimental explícita** que permite omitir la publicación/tag independiente de `v3.0.0-rc.3` y tomar como referencia técnica el candidato posterior firmado de fuente `3.0.0`, con sus propias pruebas. **No** se declara identidad binaria, igualdad de funcionalidad o que RC3 haya sido publicada.

El consentimiento anterior **no** equivale a una aprobación de revisión formal en GitHub ni autoriza integrar esta nueva PR automáticamente. La aceptación documental queda vinculada a su propia PR, commit firmado y CI; cualquier merge requiere autorización posterior independiente. Tampoco autoriza GO estable, tags, GitHub Releases, paquetes, despliegues ni cerrar todos los gates 8.8.

## 2. Evidencia primaria: G3, G4 y G7

| Fuente | Identidad y resultado |
| --- | --- |
| RC3 integrada históricamente | `c27d13a0e7643f1ee6cc6fd4a20e3dce14643176` · CI [37813550182](https://github.com/Averlyth/cicadaport/actions/runs/37813550182): **28/28** jobs correctos |
| G7-R1 y PR #48 | [PR #48](https://github.com/Averlyth/cicadaport/pull/48), commit de rama firmado `ad542c3e37a92e9c589afe923b1031264c531bbc` |
| Fuente candidata estable actual | Merge firmado `53a3bb06cdade11d21c0f706fbcbc3117a34abc8`, padres `0f8afde7b0a87bbcb729238af01f5df4bb60e839` y `ad542c3e37a92e9c589afe923b1031264c531bbc` |
| CI postmerge exact-main | [38169376262](https://github.com/Averlyth/cicadaport/actions/runs/38169376262): **28/28** jobs correctos; **32/32** checks del commit entre ambos workflows |
| CodeQL/seguridad postmerge | [38169376347](https://github.com/Averlyth/cicadaport/actions/runs/38169376347): SUCCESS, **4/4** jobs |
| Python 3.13 Ubuntu 24.04 | [Job 114558555450](https://github.com/Averlyth/cicadaport/actions/runs/38169376262/job/114558555450): **565 passed, 5 skipped, 72 subtests**; cobertura **82,09 %**; 24 casos nominativos cotejados |
| Matriz de artefactos | Ubuntu 22.04/24.04 × Python 3.10–3.13: **8/8** celdas; wheel y sdist probados fuera del checkout, **16/16** smokes |
| Supply chain G7 | Snapshot runtime instalado con **9 dependencias transitivas**, `CYCLONEDX_TRANSITIVE_RUNTIME_CLOSURE=PASS_BUILD_CELL`, build reproducible, attestation SBOM/provenance verificada en `push` |
| Soak G6 adicional | Evidencia local informada por el usuario: **1.800 s**, 360 ciclos, 720 conexiones loopback en Kali 2026.3; no equivale a soak de producción Ubuntu ni certifica RSS de procesos hijos |

Las evidencias tienen alcance y SHA propios. Una fuente posterior corregida no se convierte retroactivamente en la RC3 original. Una atestación de build-cell tampoco constituye un lock universal de las ocho celdas.

## 3. G3 — decisión por los 20 criterios contractuales

El arquitecto **ACEPTA LOS VEINTE CRITERIOS SOLAMENTE EN EL ALCANCE DEMOSTRADO** a continuación. Las pruebas identificadas corresponden a CI o scripts instalados; las limitaciones forman parte inseparable de la decisión.

| # | Criterio | Prueba/artefacto de referencia | Alcance probado y exclusiones | Decisión humana |
| ---: | --- | --- | --- | --- |
| 1 | `CLEAN_INSTALL` | scripts/test_release_artifacts.sh; scripts/release_smoke.py | 8/8 Ubuntu×Python; rueda y sdist en entornos virtuales distintos, fuera del checkout; sin plataformas adicionales | **APROBADO SOLO EN ALCANCE INDICADO** |
| 2 | `WHEEL_INSTALL` | scripts/test_release_artifacts.sh; scripts/release_smoke.py | 8/8 ejecuciones wheel; el smoke de paquete no sustituye certificación de despliegue real | **APROBADO SOLO EN ALCANCE INDICADO** |
| 3 | `SDIST_INSTALL` | scripts/test_release_artifacts.sh; scripts/release_smoke.py | 8/8 ejecuciones sdist; build nativo y entorno de herramientas según CI | **APROBADO SOLO EN ALCANCE INDICADO** |
| 4 | `CLI_SMOKE` | scripts/release_smoke.py; tests/test_session_cli.py::test_create_session_persists_and_reports | CLI instalada --version/--help, TCP loopback y reporte local; fuera de checkout | **APROBADO SOLO EN ALCANCE INDICADO** |
| 5 | `TUI_SMOKE` | scripts/release_smoke.py (import src.tui); tests/test_batch_session_interfaces.py | Importación de src.tui en distribución instalada + pruebas fuente TUI; NO test interactivo humano end-to-end instalado | **APROBADO SOLO EN ALCANCE INDICADO** |
| 6 | `RUST_ENGINE` | tests/test_single_target_resume.py::test_loopback_executor_completes_open_and_closed_ports; scripts/release_smoke.py | Loopback y contratos, Rust fmt/clippy/tests; no carga externa | **APROBADO SOLO EN ALCANCE INDICADO** |
| 7 | `GO_EVIDENCE_ENGINE` | tests/test_task_5_4_go_evidence.py::test_tls_evidence_is_truthful; scripts/release_smoke.py | Banner loopback, tests Go TLS verificado y regresión; no demostrar cada CA/hostname de producción | **APROBADO SOLO EN ALCANCE INDICADO** |
| 8 | `SESSION_CREATE` | tests/test_session_cli.py::test_create_session_persists_and_reports | Test nominal PASSED; persistencia en laboratorio CI | **APROBADO SOLO EN ALCANCE INDICADO** |
| 9 | `SESSION_RESUME` | tests/test_single_target_resume.py::test_interruption_is_persisted_and_resume_skips_completed_port | Test nominal PASSED; no replica todas las interrupciones operativas | **APROBADO SOLO EN ALCANCE INDICADO** |
| 10 | `SESSION_RECOVERY` | tests/test_session_store_v2.py::test_recover_rolls_back_uncommitted_state; tests/test_batch_session_runtime.py::test_failure_isolated_and_resume_retries_only_pending_work | Dos tests nominales PASSED; pruebas de fallos inyectados | **APROBADO SOLO EN ALCANCE INDICADO** |
| 11 | `CANCELLATION` | tests/test_bridge_cancellation.py::test_rust_subprocess_is_terminated_on_cancellation; tests/test_bridge_cancellation.py::test_go_subprocess_is_terminated_on_cancellation | Dos tests nominales PASSED; G6 reporta 6 pares de cancelación y 5 operaciones posteriores, sin inferir cobertura universal | **APROBADO SOLO EN ALCANCE INDICADO** |
| 12 | `REPORT_GENERATION` | tests/test_secure_artifacts_v2.py::test_reports_use_private_files_and_neutralize_terminal_controls; scripts/release_smoke.py | Test nominal PASSED + reporte CLI instalado; archivos locales | **APROBADO SOLO EN ALCANCE INDICADO** |
| 13 | `SECURE_ARTIFACTS` | tests/test_secure_artifacts_v2.py::test_atomic_writer_ignores_umask_and_rejects_overwrite; tests/test_secure_artifacts_v2.py::test_writer_rejects_symlink_target | Dos tests nominales PASSED; permisos, sobreescritura y symlink locales | **APROBADO SOLO EN ALCANCE INDICADO** |
| 14 | `CONFIG_VALIDATION` | tests/test_task_6_2_configuration_environment.py::test_precedence_cli_environment_file_default; tests/test_task_6_2_configuration_environment.py::test_secret_file_requires_private_mode | Dos tests nominales PASSED; configuración local y fichero secreto | **APROBADO SOLO EN ALCANCE INDICADO** |
| 15 | `HEALTH` | tests/test_task_6_3_health_readiness_metrics_logging.py::test_health_starts_fail_closed_and_live | Test nominal PASSED; health in-process, NO endpoint HTTP público | **APROBADO SOLO EN ALCANCE INDICADO** |
| 16 | `READINESS` | tests/test_task_6_3_health_readiness_metrics_logging.py::test_readiness_is_false_by_default; tests/test_task_6_3_health_readiness_metrics_logging.py::test_readiness_from_task_6_2_diagnostics_passes | Dos tests nominales PASSED; readiness local, NO prueba de orquestador producción | **APROBADO SOLO EN ALCANCE INDICADO** |
| 17 | `DIAGNOSTICS` | tests/test_task_6_2_configuration_environment.py::test_environment_diagnostics_fail_closed_on_required_dependency; tests/test_task_6_3_health_readiness_metrics_logging.py::test_logging_redacts_known_secret_and_high_signal_values | Dos tests nominales PASSED; dependencias e higiene de logs locales | **APROBADO SOLO EN ALCANCE INDICADO** |
| 18 | `UPDATE_PLAN` | tests/test_task_6_4_installation_update_rollback.py::test_update_plan_is_deterministic; tests/test_task_6_4_installation_update_rollback.py::test_update_plan_rejects_backup_hash_mismatch | Dos tests nominales PASSED; SOLO generación/validación de plan, NO actualización ejecutada | **APROBADO SOLO EN ALCANCE INDICADO** |
| 19 | `ROLLBACK_PLAN` | tests/test_task_6_4_installation_update_rollback.py::test_rollback_plan_is_deterministic; tests/test_task_6_4_installation_update_rollback.py::test_rollback_plan_rejects_backup_hash_not_in_manifest | Dos tests nominales PASSED; SOLO generación/validación de plan, NO rollback ejecutado | **APROBADO SOLO EN ALCANCE INDICADO** |
| 20 | `LONG_RUNNING_OPERATION` | tests/test_task_6_5_resilience_long_running_operation.py::test_harness_completes; tests/test_task_6_5_resilience_long_running_operation.py::test_synthetic_soak_10000 | Dos tests nominales PASSED + 10 iteraciones soak sintético CI + G6 1.800 s Kali loopback; sin carga multiusuario/SLO/medida RSS hijos | **APROBADO SOLO EN ALCANCE INDICADO** |

### Límites indelegables de G3

- `TUI_SMOKE`: la instalación verifica la importación de `src.tui` y las pruebas de fuente, **no** una sesión interactiva E2E manual instalada.
- `UPDATE_PLAN` y `ROLLBACK_PLAN`: existen verificaciones de planes e integridad, **no** ejecución real de actualización o rollback en producción.
- `LONG_RUNNING_OPERATION`: diez ensayos sintéticos CI y G6 en Kali/loopback durante 1.800 s; no se demuestra SLO, representatividad Ubuntu de duración equivalente, multiusuario ni límites RSS propios de los procesos Rust/Go.
- Alcance formal de soporte: **Linux x86_64, Ubuntu 22.04/24.04, Python 3.10–3.13**; Rust 1.97.1 y Go 1.26.9. No se amplía a Windows, macOS, ARM64 ni Python 3.14.
- Se acepta la evidencia operacional **limitada**, no una certificación de prestación comercial ilimitada; todo gate de distribución estable se evalúa aparte.

**Resultado G3:** `G3=FORMALLY_APPROVED_SCOPED_20_OF_20`; la aprobación es decisión del arquitecto, no una nueva ejecución de producción.

## 4. G4 — excepción formal a la publicación independiente de RC3

El arquitecto **APRUEBA OMITIR** el tag y la publicación individual de `v3.0.0-rc.3`, reemplazando **el paso procedimental de publicación RC3** por la combinación auditada de evidencia RC3 histórica y evidencia posterior del candidato fuente estable.

La comparativa GitHub entre `c27d13a0e7643f1ee6cc6fd4a20e3dce14643176` y `53a3bb06cdade11d21c0f706fbcbc3117a34abc8` arroja **26 commits posteriores, 0 commits divergentes y 47 archivos diferentes**. La lista completa por categoría queda congelada en esta acta:


### CI y protección (1)

- `.github/workflows/ci.yml`

### Go / TLS autenticado (2)

- `go-banner/main.go`
- `go-banner/main_test.go`

### Rust / dependencias nativas (2)

- `rust-core/Cargo.toml`
- `rust-core/Cargo.lock`

### Identidad/versionado/packaging (9)

- `.go-version`
- `pyproject.toml`
- `requirements.txt`
- `requirements-dev.txt`
- `requirements-release.in`
- `requirements-release.txt`
- `setup.py`
- `src/version.py`
- `src/native.py`

### Herramientas, release engineering y SBOM (9)

- `scripts/audit_dependencies.sh`
- `scripts/build_all.sh`
- `scripts/build_release_artifacts.sh`
- `scripts/check_tools.sh`
- `scripts/generate_cyclonedx_sbom.py`
- `scripts/runtime_sbom.py`
- `scripts/test_release_artifacts.sh`
- `scripts/verify_supply_chain.py`
- `scripts/verify_task_8_8_9_stable_source.py`

### Pruebas y controles (9)

- `tests/test_release_candidate_support.py`
- `tests/test_task_5_3_rust_engine.py`
- `tests/test_task_5_4_go_evidence.py`
- `tests/test_task_5_5_supply_chain.py`
- `tests/test_task_5_6_enterprise_release.py`
- `tests/test_task_7_5_rust_hardening.py`
- `tests/test_task_8_8_9_stable_source.py`
- `tests/test_task_8_8_runtime_sbom.py`
- `tests/test_task_8_release_quality.py`

### Documentación y política (15)

- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `README.md`
- `ROADMAP.md`
- `SECURITY.md`
- `docs/audits/task-8-7-risk-disposition-preclosure-20261009.md`
- `docs/audits/task-8-8-9-stable-source-prepublication.md`
- `docs/audits/task-8-8-g2-g3-g7-reconciliation-20261010.md`
- `docs/audits/task-8-8-stable-go-no-go-candidate.md`
- `docs/audits/task-8-stage-l-acceptance-review.md`
- `docs/audits/task-8-stage-r3-postmerge-evidence.md`
- `docs/implementation/task-5-4-go-service-evidence-v2.md`
- `docs/task-8-acceptance.md`
- `docs/task-8-rc3-release.md`
- `docs/task-8-status.md`

Las variaciones son **materiales**: verificación autenticada TLS/X.509 y hostname en Go (G5), Go 1.26.9, Tokio 1.53.2, actualizaciones de Python/release lock, identidad `3.0.0` en la fuente, cadena de suministro y SBOM transitivo G7-R1. No se afirma equivalencia de binarios, hashes, SBOM byte a byte, semántica estricta, ni identidad de artefactos.

**Estado histórico inequívoco:** RC3 se probó como fuente pero no se creó su tag ni se publicó como GitHub Release. La única prerelease pública observada es `v3.0.0-rc.1`. **El waiver no ordena crear retroactivamente RC3** ni es permiso de crear `v3.0.0`.

**Resultado G4:** `G4=ARCHITECT_APPROVED_RC3_PUBLICATION_WAIVER`; para la evaluación final de `FINAL_RC` se documentará **sustitución procedimental autorizada, no RC3 publicada**. Las condiciones 8.8 restantes no se dan por satisfechas automáticamente.

## 5. Gate de TASK 8.8: estado posterior a las decisiones G3/G4

| Condición | Estado de este registro | Salvedad |
| --- | --- | --- |
| `DEPENDENCY_BACKLOG` | Por reconciliar en acta final exact-main | No se infiere cierre de un inventario previo |
| `RESOURCE_HYGIENE` | PASS técnico dentro de pruebas acotadas | Sin SLO de producción |
| `TEST_BASELINE` | CI PASS; conciliación longitudinal pendiente | 565/5/72, cobertura 82,09 %; explicar variación histórica |
| `QUALITY_GATES` | PASS técnico exact-main | Se renuevan sobre SHA de la PR documental |
| `DOCUMENTATION` | Acta y adenda preparadas, integración pendiente | No reescribir documentación histórica |
| `SERVICE_READINESS` | **G3 aprobado en alcance limitado** | No aptitud productiva ilimitada |
| `FINAL_RC` | **G4 waiver procedimental aprobado** | No tag RC3, no identidad binaria, sin publicación |
| `ENTERPRISE_ACCEPTANCE` | Evidencia de fuente aprobada previamente; gate final separado | No extender automáticamente riesgos anteriores |
| `SECURITY_GATES` | CI técnico PASS, inventario nativo final pendiente | G5 TLS autenticado; alerta #2 observada FIXED en corte 2026-10-10; estado actual no inferido de CodeQL verde |
| `SUPPLY_CHAIN` | PASS técnico exact-main G7 | Attestations/snapshots ligados a su SHA |
| `OPEN_BLOCKERS=0` | **NO CERTIFICADO** | Falta reconciliación integral y autorización independiente |

**Decisión global invariable:** `STABLE_RELEASE=NO_GO`. Ni G3 ni G4 sustituyen la decisión simultánea de las once condiciones del contrato. Queda **no autorizada** la transición a `v3.0.0` pública.

## 6. Requisitos para integrar esta PR documental

1. Una rama documental aislada nacida exactamente de `main@53a3bb06cdade11d21c0f706fbcbc3117a34abc8`, con **solo esta acta nueva** y una adenda final en `docs/task-8-status.md`.
2. Diff limitado a dos archivos documentales; contenido histórico intacto; commit **firmado** y push **sin fuerza**, no rebase ni cherry-picks.
3. CI de rama y PR nuevo correctos sobre el **nuevo SHA** (el CI anterior sigue ligado a su corte, no se reutiliza como CI de un commit distinto).
4. Revisión documental y autorización independiente antes de cualquier merge; después, verificación de padres, firma y CI posmerge exact-main.
5. Ningún tag, release, paquete, merge automático, cambio del ruleset, bypass de CI o cierre final 8.8/8.9.

## 7. Registro de decisiones

```text
G3_HUMAN_SIGNOFF=APPROVED_EXPLICIT_SCOPED_20_OF_20
G3_SCOPE=SUPPORTED_LINUX_X86_64_LAB_AND_CI_ONLY
G3_TUI_INTERACTIVE_INSTALLED_E2E=NOT_DEMONSTRATED
G3_UPDATE_ROLLBACK_EXECUTION=NOT_DEMONSTRATED
G3_PRODUCTION_ENDURANCE_SLO=NOT_DEMONSTRATED
G4_RC3_WAIVER=APPROVED_EXPLICIT_PROCEDURAL_SUBSTITUTION
G4_RC3_SOURCE_SHA=c27d13a0e7643f1ee6cc6fd4a20e3dce14643176
G4_RC3_SOURCE_CI=37813550182_SUCCESS_28_OF_28
G4_SOURCE_DELTA=26_COMMITS_47_FILES
G4_BINARY_EQUIVALENCE=NOT_ASSERTED
G4_RC3_TAG=NOT_CREATED
G4_RC3_PUBLICATION=NOT_EXECUTED
G7_MAIN_SHA=53a3bb06cdade11d21c0f706fbcbc3117a34abc8
G7_POSTMERGE_CI=38169376262_SUCCESS_28_OF_28
G7_MAIN_CHECKS=SUCCESS_32_OF_32
G3_G4_DOCUMENTARY_PR=AUTHORIZED_NOT_YET_INTEGRATED
G3_G4_DOCUMENTARY_MERGE=NOT_AUTHORIZED
TASK_8_8=NO_GO_PENDING_FINAL_ELEVEN_GATE_REVIEW
TASK_8_9=PUBLICATION_NOT_AUTHORIZED
STABLE_RELEASE=NO_GO
```
