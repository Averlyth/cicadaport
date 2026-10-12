# ACTA DE RECONCILIACIÓN CONTRACTUAL — CICADAPORT TASK 8.8

**Registro:** `SGN-CICADAPORT-8.8-FINAL-RECON-20261012` · `1.0-CANDIDATA`.
**Fecha de corte:** 2026-10-12 UTC, según evidencia de Prometheus.
**Contrato rector:** [`SRP-CICADAPORT-TASK-8-001`](../contracts/task-8-stable-release-productization-v1.md), cláusula 15.
**Candidato examinado:** `main@54180410fcf8201322c06a00ab8493777458b17e`.
**Naturaleza:** reconciliación y disposición de riesgo; **NO es un acta de GO estable**.
**Ámbito de esta PR:** esta acta nueva y una adenda en `docs/task-8-status.md` únicamente.

## 1. Identidad, procedencia y corte

La PR [#49](https://github.com/Averlyth/cicadaport/pull/49) integró G3/G4 mediante el merge firmado [`54180410fcf8201322c06a00ab8493777458b17e`](https://github.com/Averlyth/cicadaport/commit/54180410fcf8201322c06a00ab8493777458b17e), con padres exactos `53a3bb06cdade11d21c0f706fbcbc3117a34abc8` y `d160c69fd8f464ffe677c113667c3a273f046698`. GitHub devolvió `verified=true`, `reason=valid`.

- [CI posmerge 38172257541](https://github.com/Averlyth/cicadaport/actions/runs/38172257541): `completed/success`, 28/28 jobs satisfactorios.
- [CodeQL posmerge 38172257687](https://github.com/Averlyth/cicadaport/actions/runs/38172257687): `completed/success`, 4/4 jobs satisfactorios.
- Checks agregados del SHA: `32/32 success`, sin pendientes ni fallos.
- Captura nativa de Prometheus: `/home/cicada/Development/GitHub/cicada-patches/TASK88_FINAL_AUDIT_20261012T033317Z` (ubicación del operador, no incluida en Git); resultado `INVENTORY_CAPTURED_PENDING_CONTRACTUAL_REVIEW`.
- En la captura: `CODE_SCANNING_OPEN=0`, `DEPENDABOT_OPEN=0`, `SECRET_SCANNING_OPEN=0`, `OPEN_PULLS=0`, `SECURITY_API_ERRORS=0`; alerta CodeQL #2 `go/disabled-certificate-check` = `fixed`.
- Los recuentos cero se refieren únicamente a alertas **abiertas y visibles en la fecha del corte**; no acreditan ausencia universal de vulnerabilidades o riesgos.

Los archivos de evidencia JSON fueron validados estructuralmente en el preflight; para auditar su integridad, los hashes SHA-256 calculados sobre sus bytes originales son:

| Archivo local de evidencia | SHA-256 |
| --- | --- |
| `remote_main.json` | `01ab4d4df399837395ded06cb43bfd1405b2aa9aeec01bef253cbfaf3bcb067c` |
| `commit.json` | `5a005a23f197720481b39c04a51b2d2d87123ac9e0e0c66965a12947111f0853` |
| `workflow_ci.json` | `d6c5c6cc7e1262ac4df6f8c08781a7e5601662a59b0939cc86d8410c4a7cf901` |
| `workflow_codeql.json` | `c6996f4bdc5ade4048deebd18b89578828f001611663dc660c616b5eee7c6771` |
| `checks.json` | `f2f7dc6e77a521d7eb2124e58f90f4b6a3bb76a228549a975fb3f8d93321823a` |
| `code_scanning.json` | `93a632246f28a39eedc6577fda8be826f662ca408592e96b1b2b26b4256eea3d` |
| `dependabot.json` | `93a632246f28a39eedc6577fda8be826f662ca408592e96b1b2b26b4256eea3d` |
| `secret_scanning.json` | `93a632246f28a39eedc6577fda8be826f662ca408592e96b1b2b26b4256eea3d` |
| `codeql_alert_2.json` | `2f5df7f8b121f45040d94ea4bda10d0c11706b05ff38cd32bc76f53bb68308b9` |
| `open_pulls.json` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |

Los archivos anteriores permanecen externos al repositorio; esta PR conserva el manifiesto de hashes y la identificación del corte, no una atestación nueva de dichos JSON. Cualquier revalidación requiere la consulta nativa actual y la revisión del SHA final.

## 2. Decisiones anteriores preservadas

- **G3:** `FORMALLY_APPROVED_SCOPED_20_OF_20`. Los 20 criterios de SUBTASK 8.5 fueron aceptados por el arquitecto *solo* dentro de su alcance demostrado. La [matriz nominal](task-8-8-g3-g4-joint-decisions-20261011.md) conserva la evidencia de cada criterio y sus exclusiones.
- **G4:** `RC3_PUBLICATION_WAIVER_APPROVED`. Queda autorizada la **sustitución procedimental de publicar** `v3.0.0-rc.3` por evidencia histórica RC3 más pruebas independientes del candidato fuente `3.0.0`. RC3 no fue etiquetada ni publicada, ni se presume identidad de artefactos, hashes, SBOM o equivalencia funcional estricta.
- **G5:** ruta Go TLS actual con validación X.509 y nombre de host. La alerta histórica CodeQL #2 figura `fixed`; la observación anterior como `open` se preserva como fotografía válida de otro corte, no como estado vigente.
- **G7:** [PR #48](https://github.com/Averlyth/cicadaport/pull/48) integrada sobre `main@53a3bb06cdade11d21c0f706fbcbc3117a34abc8`; cobertura transitiva runtime del SBOM en la celda de construcción, controles de versiones PEP 440, hashes pip, reproducibilidad, provenance y attestations verificados en la evidencia de CI. No se afirma identidad de dependencias entre las ocho celdas Ubuntu/Python.
- **SUBTASK 8.7:** cerrada y congelada según expediente precedente, con aceptación de fuente y riesgos operacionales acotados. El presente registro no amplía la aceptación de fuente a garantías productivas generales.

## 3. Conciliación nominal de pruebas y cobertura

Sobre el workflow [38172257541](https://github.com/Averlyth/cicadaport/actions/runs/38172257541), el [job Python 3.13 / Ubuntu 24.04](https://github.com/Averlyth/cicadaport/actions/runs/38172257541/job/114567138627) terminó con **565 passed, 5 skipped, 72 subtests**, cobertura **82,09 %** (piso requerido: **82 %**). En Ubuntu 22.04 / Python 3.13 se observaron los mismos 565/5/72 y cobertura 82,07 %. El [job de integración Ubuntu 24.04](https://github.com/Averlyth/cicadaport/actions/runs/38172257541/job/114567356395) terminó con **568 passed, 2 skipped, 72 subtests**.

| Tres pruebas que cambian de skipped a passed | Causa comprobada | Prueba de cierre |
| --- | --- | --- |
| `TestPythonRustEngineParity::test_known_open_and_closed_local_ports_have_equal_contract` | En la suite genérica no existe binario Rust de release en ruta esperada | PASSED en integración luego de `scripts/build_all.sh` |
| `TestPythonGoBannerParity::test_hostile_passive_banner_has_identical_output` | En la suite genérica no existe binario Go en ruta esperada | PASSED en integración luego de `scripts/build_all.sh` |
| `TestSpecializedNativeFlowIntegration::test_python_orchestrates_rust_scan_then_go_banner_locally` | No están disponibles ambos binarios en las rutas esperadas | PASSED en integración luego de `scripts/build_all.sh` |

Las otras dos omisiones corresponden a `tests/test_native_observability.py::test_real_rust` y `::test_real_go`, condicionadas por las variables `CICADAPORT_TEST_RUST_BINARY` y `CICADAPORT_TEST_GO_BINARY` no configuradas en esos jobs. **No** se afirma que esos dos casos específicos se hayan ejecutado. Existen además validaciones nativas, de bridge y de instalación en los jobs correspondientes.

Los recuentos históricos `535/5` y `538/2` provienen de un corte fuente anterior; el compare `18f0b7bcc127b8e562f322e5cbe8068ef6a7d0a3` → `54180410fcf8201322c06a00ab8493777458b17e` contiene **14 commits posteriores**, entre ellos la incorporación de pruebas para la cadena de suministro G7. No deben compararse cantidades de pruebas de fuentes distintas como si fueran la misma suite. Las diferencias de ejecución de **tres casos** en el SHA actual están identificadas por nombre y explicadas por precondiciones de binarios; no hay evidencia de regresión de esos tres casos. Esta reconciliación técnica se somete a cierre contractual mediante la PR; no se cambia el umbral de cobertura ni se deshabilitan tests.

## 4. Aceptación expresa de R-OPS-SOAK-01 para distribución estable

**Decisión explícita del arquitecto (2026-10-11, hora local; registrada en esta acta el 2026-10-12 UTC):** se **APRUEBA FORMALMENTE** la aceptación acotada del riesgo `R-OPS-SOAK-01` para distribuir CicadaPort `v3.0.0` **solo dentro de la matriz validada**, sin certificación de endurance productivo, SLO comercial ni métricas de uso de recursos no demostradas.

Alcance probado: Linux x86_64; Ubuntu 22.04 y 24.04; Python 3.10–3.13; Rust 1.97.1; Go 1.26.9. La evidencia disponible comprende pruebas sintéticas acotadas de CI y el ensayo local comunicado de 1.800 segundos / 360 ciclos / 720 conexiones loopback sobre Kali 2026.3. Ese ensayo no demuestra equivalencia con una carga productiva representativa de Ubuntu, operación multiusuario, SLO o medición completa de RSS de procesos nativos hijos.

Esta aceptación mantiene íntegramente las limitaciones de G3: la TUI instalada carece de prueba E2E manual interactiva; `UPDATE_PLAN` y `ROLLBACK_PLAN` demuestran planes, no actualización ni rollback productivos; ninguna de estas limitaciones puede convertirse en una garantía comercial. El riesgo aceptado debe figurar sin atenuación en las notas públicas de versión y matriz de soporte de TASK 8.9.

**La decisión anterior no autoriza** el GO, el merge de esta PR, un tag, release, publicación de paquetes, despliegue ni cierre de TASK 8.

## 5. Matriz de las once condiciones contractuales

La columna «situación del corte» describe evidencia de la fuente base y decisiones previas, **no** un PASS final automático de todos los gates. La cláusula 15 requiere simultaneidad sobre el SHA definitivo firmado e integrado.

| Gate exigido | Situación del corte | Pendiente para cierre definitivo |
| --- | --- | --- |
| `DEPENDENCY_BACKLOG=CLOSED` | Backlog inicial y PR #32–#36 reconciliadas históricamente; `0` PR abiertas y `0` alertas Dependabot en inventario nativo | Ratificar que no apareció intake nuevo y disponer su cierre en el acta final |
| `RESOURCE_HYGIENE=PASS` | PASS técnico: 53 pruebas y 14 subtests SQLite; gates de warnings y pruebas acotadas; R-OPS-SOAK-01 aceptado con límites | Mantener aceptación acotada, sin inferir endurance productivo |
| `TEST_BASELINE=RECONCILED` | Explicación nominal de cinco skips y 3 PASS adicionales de integración; 565/5 frente a 568/2; cobertura >=82 % | Ratificar reconciliación sobre la versión fuente final |
| `QUALITY_GATES=PASS` | CI de Python/Black/Flake8/Mypy, Rust, Go y Shell y 32/32 checks satisfactorios | Renovar controles si cambia SHA de fuente/CI |
| `DOCUMENTATION=CURRENT` | README, ROADMAP y SECURITY presentan identidad de fuente y prerelease; esta acta consolida el estado del corte | Integrar esta PR y comprobar coherencia canónica posmerge; históricos no se reescriben |
| `SERVICE_READINESS=PASS` | G3 aprobado formalmente 20/20 dentro de la matriz soportada, con exclusiones explícitas | Reutilizar aprobación vigente, sin extenderla a producción general |
| `FINAL_RC=PASS` | G4 exime procedimiento de publicación de `v3.0.0-rc.3`; fuente RC3 anterior probada; candidato 3.0.0 probado separadamente | Asentar sustitución procedimental en cierre final; RC3 sigue sin publicar |
| `ENTERPRISE_ACCEPTANCE=PASS` | SUBTASK 8.7 cerrada para fuente, con riesgos acotados; decisiones G3 y R-OPS-SOAK-01 registradas | Respetar alcance y confirmar si hay riesgos de distribución no dispuestos |
| `SECURITY_GATES=PASS` | Captura nativa: 0 alertas abiertas CodeQL, Dependabot y Secret Scanning; alerta #2 FIXED; jobs de seguridad exitosos | Revalidar inventario ante nuevos commits o alertas; ausencia total de fallos desconocidos no se presume |
| `SUPPLY_CHAIN=PASS` | Evidencia G7: release lock, hash-pins, SBOM runtime de build-cell, hashes, artefactos reproducibles, provenance y attestations en CI | Vincular evidencia exacta al SHA publicable; no afirmar SBOM único para todas las celdas |
| `OPEN_BLOCKERS=0` | No hay PR ni alertas abiertas en la captura; no se conoce bloqueo técnico nuevo del inventario consultado | **NO_CERTIFICADO** hasta revisión integral, integración y autorización del gate 8.8 |

## 6. Condiciones para cerrar TASK 8.8 y pasar a publicación

1. Revisar el diff de esta PR, firma del commit y el CI de rama/PR; obtener autorización **independiente** para su merge protegido.
2. Una vez integrada, comprobar padres, firma, árboles y CI exacto de `main`, y que el inventario de alertas no haya cambiado materialmente.
3. Emitir un dictamen **GO o NO_GO** explícito que certifique simultáneamente los once gates, incluido `OPEN_BLOCKERS=0` sobre la base final. Hasta entonces no se declara `DOCUMENTATION=CURRENT` ni `OPEN_BLOCKERS=0` como hechos consumados.
4. Solicitar autorización **separada** para TASK 8.9, tag firmado `v3.0.0`, GitHub Release, wheel/sdist, manifiestos, SHA-256, SBOM, provenance, attestations, descarga/instalación y verificación pospublicación.

La única release pública observada al corte es `v3.0.0-rc.1`. Ni la preparación documental ni el código fuente `3.0.0` equivalen a una publicación estable.

```text
TASK_8_8=FINAL_ELEVEN_GATE_RECONCILIATION_PR_PREPARATION
CONTRACT=SRP-CICADAPORT-TASK-8-001
RECONCILIATION_BASE=54180410fcf8201322c06a00ab8493777458b17e
G3=FORMALLY_APPROVED_SCOPED_20_OF_20
G4=RC3_PUBLICATION_WAIVER_APPROVED
R_OPS_SOAK_01=ARCHITECT_ACCEPTED_FOR_BOUNDED_STABLE_DISTRIBUTION
NATIVE_SECURITY_INVENTORY=PASS_OPEN_ZERO_AT_EVIDENCE_CUTOFF
CODEQL_ALERT_2=FIXED
TEST_BASELINE=TECHNICALLY_RECONCILED_PENDING_FINAL_GATE
DOCUMENTATION=PR_PREPARATION_NOT_MERGED
OPEN_BLOCKERS_ZERO=NOT_CERTIFIED
STABLE_RELEASE=NO_GO
STABLE_TAG=NOT_AUTHORIZED
STABLE_PUBLICATION=NOT_AUTHORIZED
TASK_8_9=PUBLICATION_BLOCKED
```
