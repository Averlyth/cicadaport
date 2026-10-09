# ACTA DE EVALUACIÓN GO/NO-GO — SUBTASK 8.8

**Proyecto:** CicadaPort 3.0.0 — Averlyth / Obscuryx Security Platform  
**Registro propuesto:** `SGN-CICADAPORT-8.8-001`  
**Versión documental:** `0.1-CANDIDATA`  
**Fecha de corte:** 2026-10-09 (UTC; evidencia posterior a la PR #43)  
**Contrato rector:** `SRP-CICADAPORT-TASK-8-001`, `1.0-CANDIDATE`  
**Estado del acta:** `BORRADOR_PREPARADO_NO_APROBADO_NO_INTEGRADO`  
**Autoridad:** Arquitecto del proyecto, pendiente de resolución formal del acta  
**Decisión vigente:** `STABLE_RELEASE=NO_GO`  

## 1. Objeto y límites de autoridad

Se evalúa el cumplimiento simultáneo de las once condiciones de SUBTASK 8.8 para autorizar o impedir la distribución estable de CicadaPort `v3.0.0`. La autorización recibida alcanza exclusivamente la preparación documental del acta, no su aprobación, commit, push, integración, aceptación ampliada de riesgos, etiquetado ni publicación.

El presente registro distingue hechos verificados, interpretaciones acotadas y decisiones pendientes. Una CI verde y un estado `stable` en los metadatos de fuente no prueban por sí solos la aptitud para distribución estable. Las evidencias históricas se conservan bajo sus fechas de corte; no se reescriben como si hubieran sido generadas posteriormente.

## 2. Identidad inmutable y superficie evaluada

| Concepto | Evidencia observada |
| --- | --- |
| Repositorio | `Averlyth/cicadaport` |
| PR de preparación estable | `#43`, integrada y cerrada |
| Commit fuente firmado | `943f96e80c8cb20f35b90ce1e08d2dbd9d6961c8` |
| Commit `main` de integración | `18f0b7bcc127b8e562f322e5cbe8068ef6a7d0a3` |
| Padres del merge | `9f854be4919832b0d40c06321e3dd5bf9254f56d` y `943f96e80c8cb20f35b90ce1e08d2dbd9d6961c8` |
| Árbol Git | `12491489dd92bb9c24a148db500cd5b68421cc6e` |
| Firma de integración | GitHub `verified=true`, `reason=valid` |
| CI de push del candidato | `37969213374`: 28/28 `success` |
| CI de PR #43 | `37969997921`: 27 `success`, 1 `skipped` por condición del evento |
| CI exacto postmerge de `main` | `37972053597`: 28/28 `success`, sin fallos, omisiones ni pendientes |
| CodeQL exacto postmerge | 4/4 analizadores: Go, Python, Rust y Actions `success` |
| Artefacto interno de Actions | `cicadaport-3.0.0-linux-x86_64`, ID `11637995331`, no constituye publicación |
| Canal fuente | `3.0.0`, `RELEASE_CHANNEL=stable`; lanzamiento estable no aprobado |
| Última GitHub Release publicada | `v3.0.0-rc.1` (prerelease) |
| Matriz verificada | Linux x86_64; Ubuntu 22.04/24.04; Python 3.10–3.13; Rust 1.97.1; Go 1.26.9 |

El contexto obligatorio denominado `Go 1.26.8` es un nombre heredado del ruleset `20137979`; el compilador ejecutado está fijado a Go `1.26.9`. El ruleset permanece activo y exige 25 checks con actualización estricta de rama. La integración se realizó mediante merge commit protegido.

### 2.1. Referencias primarias para auditoría

- PR integrada: https://github.com/Averlyth/cicadaport/pull/43
- Merge definitivo: https://github.com/Averlyth/cicadaport/commit/18f0b7bcc127b8e562f322e5cbe8068ef6a7d0a3
- CI del source commit: https://github.com/Averlyth/cicadaport/actions/runs/37969213374
- CI de la PR: https://github.com/Averlyth/cicadaport/actions/runs/37969997921
- CI postmerge exacto: https://github.com/Averlyth/cicadaport/actions/runs/37972053597
- Attestation provenance: https://github.com/Averlyth/cicadaport/attestations/54420590
- Attestation SBOM: https://github.com/Averlyth/cicadaport/attestations/54420606
- CodeQL #2: https://github.com/Averlyth/cicadaport/security/code-scanning/2
- Contrato: `docs/contracts/task-8-stable-release-productization-v1.md` (apartados 8.5–8.9 y cláusula 15)
- Aceptación previa: `docs/audits/task-8-7-risk-disposition-preclosure-20261009.md`
- Preparación estable integrada: `docs/audits/task-8-8-9-stable-source-prepublication.md`
- Inventario local exact-main entregado por Prometheus: `/tmp/cicadaport-task889-isolated.HhBM9g/security-exact-main.json` (ruta externa a este borrador, no adjunta ni incorporada aún al repositorio)

## 3. Evidencia funcional, de calidad, seguridad y suministro

**Pruebas de fuente y operación.** El workflow postmerge verificó los ocho cruces de Python 3.10–3.13 con Ubuntu 22.04/24.04; Rust con `fmt`, Clippy, tests y release build; Go con formato, `vet`, tests con detector de carreras y build; ShellCheck, Black, Flake8, Mypy, controles de recursos e integración sobre ambos Ubuntu. La instalación y ejecución fuera del checkout de wheel y sdist fue correcta en las ocho combinaciones soportadas. Se ejecutaron diez iteraciones sintéticas del soak de TASK 6.5; ello no constituye una prueba de duración ni de cargas reales de producción.

**Baseline Python medido.** En el job postmerge `Python tests (ubuntu-24.04, 3.13)` se observaron **535 passed, 5 skipped, 72 subtests passed**, cobertura **82,09 %**, umbral exigido **82 %**. La evidencia local anterior comunicaba **538 passed, 2 skipped, 72 subtests** y una cobertura medida distinta. No se presume una regresión: las omisiones deben relacionarse por nombre, motivo y entorno antes de declarar `TEST_BASELINE=RECONCILED`. El mismo CI aprobó un subconjunto de **53 pruebas y 14 subtests** para el control de recursos SQLite.

**Cadena de suministro.** El build postmerge produjo `portscanner_pro-3.0.0.tar.gz` y `portscanner_pro-3.0.0-py3-none-linux_x86_64.whl`. La generación reproducible, manifest, hashes, CycloneDX y verificación de artefactos resultaron correctas. El flujo de push emitió attestations firmadas de procedencia SLSA y SBOM, con cinco sujetos declarados en cada emisión. Las attestations observadas son `54420590` (provenance) y `54420606` (SBOM); el job posterior de verificación de firmas y procedencia terminó `success`.

**Inventario nativo de seguridad en `main`.** La consulta paginada, aportada para el commit exacto de integración, concluyó `inventory=PASS`: **CodeQL: 1 alerta abierta (#2)**; **Dependabot: 0 alertas abiertas**; **Secret Scanning: 0 alertas abiertas**. El hallazgo CodeQL #2 sigue `open`, regla `go/disabled-certificate-check`, severidad `high`. Cuatro análisis CodeQL exitosos significan ejecución correcta del análisis, no ausencia de hallazgos. Los inventarios de alertas son observaciones del corte; su resultado nulo no certifica ausencia de vulnerabilidades no detectadas.

## 4. Matriz contractual de las once condiciones

`PASS` significa comprobación sustentada dentro del alcance indicado. `PENDIENTE` o `NO_CERTIFICADO` no satisfacen la igualdad literal exigida por la cláusula 15 del contrato. No se transforma un resultado parcial en un `PASS` mediante inferencia.

| Requisito exigido | Dictamen en este corte | Fundamento y trabajo restante |
| --- | --- | --- |
| `DEPENDENCY_BACKLOG=CLOSED` | `EVIDENCIA_FAVORABLE_PENDIENTE_ACTA_FINAL` | Backlog inicial reconciliado; Stage Q cerró #32–#36 como superseded y conservó sus referencias; cero alertas Dependabot y cero PR abiertas observadas. Anexar conciliación final del inventario y exclusiones de alcance. |
| `RESOURCE_HYGIENE=PASS` | `PASS_TÉCNICO` | Control SQLite 53 pruebas/14 subtests, warnings gate y soak sintético en CI. No equivale a resistencia operacional ilimitada. |
| `TEST_BASELINE=RECONCILED` | `PENDIENTE` | CI exacta: 535/5/72 y 82,09 %; evidencia local precedente: 538/2/72. Explicar nominalmente los tres casos de diferencia y el cambio de cobertura. |
| `QUALITY_GATES=PASS` | `PASS_TÉCNICO` | Black, Flake8, Mypy, pytest con umbral 82 %, Rust, Go, Shell y CI final correctos. |
| `DOCUMENTATION=CURRENT` | `PENDIENTE` | `README.md` y `SECURITY.md` distinguen fuente 3.0.0 de publicación. `ROADMAP.md` aún llama versión vigente a RC3, y los registros históricos requieren una fuente canónica de estado posterior; corregir solo textos realmente vigentes y añadir una adenda, sin alterar snapshots. |
| `SERVICE_READINESS=PASS` | `PASS_TÉCNICO_ACOTADO_PENDIENTE_CERTIFICACIÓN` | Instalación/ejecución, salud, configuración, sesiones, recuperación, cancelación y pruebas operativas sobre matriz soportada. Conciliar punto por punto la lista de 8.5 y no declarar SLA ni soporte de plataformas no evaluadas. |
| `FINAL_RC=PASS` | `PENDIENTE_DE_DECISIÓN_CONTRACTUAL` | RC3 fue validada como candidata fuente pero nunca etiquetada/publicada; aclarar formalmente si 8.6 exige tag RC3 previo o permite la trazabilidad fuente ya probada sin publicar RC3. No inventar cierre ni excepción tácita. |
| `ENTERPRISE_ACCEPTANCE=PASS` | `PASS_FUENTE_ACOTADO` | SUBTASK 8.7 figura formalmente cerrada para su alcance de fuente; la aceptación anterior de TLS y soak no se extiende automáticamente a distribución estable. |
| `SECURITY_GATES=PASS` | `NO_CERTIFICADO` | CodeQL #2 HIGH abierta; falta disposición exclusiva para producto estable, evidencia de controles y reevaluación del riesgo de suplantación/MITM. |
| `SUPPLY_CHAIN=PASS` | `PASS_TÉCNICO` | Lock, auditorías, hashes, build reproducible, wheel/sdist, SBOM, attestations y verificación de procedencia sobre SHA exacto. |
| `OPEN_BLOCKERS=0` | `NO_CERTIFICADO` | Riesgo HIGH sin disposición estable, baseline/documentación/RC por reconciliar y ausencia de evidencia suficiente para afirmar que no existen bloqueadores contractuales. |

**Resultado contractual:** no se cumplen simultáneamente las once igualdades exigidas. El resultado permanece `STABLE_RELEASE=NO_GO`.

## 5. Registro de riesgos residuales y decisiones pendientes

### R-SEC-TLS-01 — identidad TLS no autenticada

**Situación:** `go-banner/main.go` mantiene `tls.Config{InsecureSkipVerify: true, MinVersion: tls.VersionTLS12}` en la ruta de observación. Se conservan pruebas de guardas previas a la conexión (`TestTLSObservationPolicyPermitsOnlyPassiveAndCanonicalHEAD`, `TestTLSObservationPolicyRejectsNonCanonicalProbesBeforeDial`) y de veracidad de evidencia (`TestTLSEvidenceNeverClaimsUnverifiedCertificateIsVerified`). La conexión acepta certificados desconocidos y no autentica la identidad remota; sigue siendo susceptible a suplantación y MITM.

**Controles existentes:** observación pasiva o petición fija sin credenciales `HEAD / HTTP/1.0`; rechazo previo a conexión de planes no permitidos; mínimo TLS 1.2; `certificate_verified=false`; `verification_not_performed_observation_mode`; prohibición documentada de reutilizarla para autenticación, secretos, actualizaciones y canales de confianza.

**Aceptación anterior:** exclusivamente para el hito de fuente 8.7. **Pendiente en 8.8:** revisión de amenaza y rutas de datos, verificación de que no se procesan observaciones no autenticadas como identidad confiable, ensayos negativos de política en el SHA final, documentación de uso y una resolución explícita del arquitecto: remediar o aceptar el riesgo residual únicamente en un perímetro de distribución definido. La aceptación no elimina la alerta ni permite etiquetarla como falso positivo. **Decisión actual: NO_ACEPTADO_PARA_DISTRIBUCIÓN_ESTABLE**.

### R-OPS-SOAK-01 — duración y representatividad operacional

Las diez iteraciones CI acreditan resistencia sintética acotada, no operación continua representativa ni cumplimiento de SLO. **Pendiente:** aceptar por escrito la limitación de alcance y excluir promesas de endurance, o ejecutar una prueba de duración con escenario, métricas, umbrales, cancelación, recuperación y presupuesto de recursos definidos de antemano. **Decisión actual: SIN_DISPOSICIÓN_ESTABLE**.

### R-TEST-BASELINE-01 — variación entre ambientes

El CI postmerge de Python 3.13 muestra 535 aprobadas/5 omitidas; el antecedente local 538/2. La cobertura de CI es 82,09 % y supera el mínimo del 82 %. **Pendiente:** identificar casos omitidos, contrastar condiciones de ejecución y registrar la reconciliación de cobertura y contadores. **Decisión actual: PENDIENTE**.

### R-DOC-STABLE-01 — incoherencia de estado vigente

Las referencias de `ROADMAP.md` a RC3 como versión fuente actual contradicen `src/version.py=3.0.0`. Los documentos con corte anterior deben mantenerse como evidencia histórica. **Pendiente:** fuente canónica de estado posterior a PR #43 y corrección selectiva de textos declarados vigentes. **Decisión actual: PENDIENTE**.

### R-FINAL-RC-01 — criterio de aceptación de RC3

Se verificó una fuente RC3 previa y después una candidata fuente estable `3.0.0`, pero no se observó la publicación ni etiqueta `v3.0.0-rc.3`. **Pendiente:** decisión documentada sobre el criterio de 8.6, sin calificar unilateralmente el paso omitido como cumplido ni generar la etiqueta sin autorización. **Decisión actual: PENDIENTE**.

### R-SEC-VISIBILITY-01 — limitaciones de cobertura

El inventario de alertas y los escáneres de CI son controles positivos pero no un inventario exhaustivo de rutas explotables. La revisión de 8.7 detectó entradas SBOM sin versión plenamente resuelta en un corte anterior; no se presume que ese número permanezca igual. **Pendiente:** verificar trazabilidad y cobertura de componentes del SBOM exacto de 3.0.0 y documentar exclusiones o componentes no resueltos. **Decisión actual: PENDIENTE_DE_VERIFICACIÓN_ACOTADA**.

## 6. Plan verificable de remediación y reconsideración

| Orden | Acción necesaria | Criterio de salida |
| --- | --- | --- |
| G1 | Reconciliar casos `skipped` y cobertura entre pruebas locales y CI | Tabla por test, causa, evidencia y resultado; `TEST_BASELINE=RECONCILED` justificable |
| G2 | Rectificar el estado documental vigente y adjuntar el acta 8.8 | La versión fuente, última publicación y estado de gates coinciden en documentos canónicos; snapshots históricos preservados |
| G3 | Consolidar matrices de dependencias, servicio y 8.7 | Cada criterio de 8.5 y 8.7 vinculado a prueba, log, artefacto o aceptación de alcance |
| G4 | Resolver el criterio de la final RC | Decisión del arquitecto que interpreta fielmente 8.6 y mantiene historia; si requiere nuevo trabajo, hacerlo bajo gate separado |
| G5 | Emitir disposición estable del TLS HIGH | Decisión expresa, amenaza/controles verificables, alcance declarado y alerta #2 tratada con transparencia |
| G6 | Emitir disposición estable del soak | Prueba de duración suficiente o aceptación expresa del alcance restringido y de las declaraciones excluidas |
| G7 | Verificar inventario final, SBOM y blockers | Consultas paginadas, clasificación de cada riesgo, evidencia trazable y capacidad de sostener `SECURITY_GATES=PASS` y `OPEN_BLOCKERS=0` sin omisiones |
| G8 | Repetir gates si cambia `main` | Firma, árbol, CI postmerge, CodeQL, artefactos y hashes sobre el nuevo SHA exacto; no reutilizar indebidamente el SHA anterior |

La evolución del documento seguirá la secuencia: borrador revisado → autorización del texto → rama documental aislada desde `main` exacto → commit firmado → CI push → PR y CI → autorización independiente de merge → merge protegido y CI exacto de `main` → decisión formal de 8.8. Ninguno de esos pasos posteriores queda autorizado por el permiso de preparación de este borrador.

## 7. Resolución del corte y prohibiciones

La información analizada demuestra una candidata de **código fuente técnicamente validada y trazable**, no una distribución estable cuyo riesgo residual y obligaciones contractuales estén completamente resueltos. Conforme a la cláusula 15, basta una condición insatisfecha para mantener `NO_GO`; existen varias condiciones pendientes. La aprobación de este acta candidata, si llegara a producirse, **no** constituiría un cambio a `GO`.

No se autoriza: alterar la alerta CodeQL #2, cerrar o degradar hallazgos sin fundamento, omitir pruebas contractuales, realizar merge adicional, modificar reglas de protección, crear la etiqueta `v3.0.0`, publicar una GitHub Release, subir paquetes ni cerrar TASK 8. Cualquier publicación estable requerirá previamente una nueva evaluación integral sobre el SHA exacto y una autorización separada y expresa.

```text
ACT_RECORD=SGN-CICADAPORT-8.8-001
ACT_VERSION=0.1-CANDIDATA
ACT_STATUS=BORRADOR_PREPARADO_NO_APROBADO_NO_INTEGRADO
PROJECT=CICADAPORT
SOURCE_VERSION=3.0.0
EXACT_MAIN_SHA=18f0b7bcc127b8e562f322e5cbe8068ef6a7d0a3
PR_43=MERGED_SIGNED_VERIFIED
MAIN_CI=37972053597_SUCCESS_28_OF_28
MAIN_CODEQL=SUCCESS_4_OF_4
DEPENDABOT_OPEN=0
SECRET_SCANNING_OPEN=0
CODEQL_ALERT_2=OPEN_HIGH
TEST_BASELINE_RECONCILIATION=PENDING
DOCUMENTATION_CURRENT=PENDING
FINAL_RC_GATE=PENDING
STABLE_TLS_RISK_DISPOSITION=PENDING
STABLE_SOAK_DISPOSITION=PENDING
SECURITY_GATES=NOT_CERTIFIED_FOR_STABLE
OPEN_BLOCKERS_ZERO=NOT_CERTIFIED
SUBTASK_8_8=ACT_CANDIDATE_PREPARATION
SUBTASK_8_9=PUBLICATION_BLOCKED
STABLE_RELEASE=NO_GO
STABLE_TAG=NOT_AUTHORIZED
STABLE_PUBLICATION=NOT_AUTHORIZED
TASK_8_FINAL_CLOSURE=PENDING
```

**Firma/ratificación del arquitecto:** pendiente. Este campo no debe completarse por inferencia, por CI o por autorización de preparación documental.

---

## 8. Adenda de aprobación del contenido — 2026-10-09

**Naturaleza:** registro posterior a la elaboración de la versión `0.1-CANDIDATA`, sin reescribir el corte original.

El arquitecto del proyecto aprobó expresamente el contenido del acta `SGN-CICADAPORT-8.8-001` y ratificó que la decisión de distribución estable permanece `STABLE_RELEASE=NO_GO`. Posteriormente autorizó iniciar la preparación de una rama documental aislada para incorporarla al repositorio. Estas autorizaciones se produjeron en la conversación de gobierno del proyecto; **no** constituyen una firma criptográfica ni una aprobación de integración a `main`.

Las menciones anteriores a `BORRADOR_PREPARADO_NO_APROBADO_NO_INTEGRADO`, «aprobación pendiente» y «firma/ratificación pendiente» describen el estado al momento de redactarse el documento inicial. Esta adenda actualiza exclusivamente el **estado de aprobación del contenido**, sin reinterpretar ni sustituir la evidencia histórica. Se conserva íntegramente el documento original, cuyo SHA-256 era:

`3c5bbc77c908c14d128b36411a55405967572ec28757306a182530afe3fd25f6`

```text
ACT_RECORD=SGN-CICADAPORT-8.8-001
ACT_VERSION=0.1-CANDIDATA
ACT_CONTENT=ARCHITECT_APPROVED
ACT_APPROVAL_EVIDENCE=PROJECT_CONVERSATION
ACT_DOCUMENTARY_BRANCH=PREPARATION_AUTHORIZED
ACT_GIT_COMMIT=NOT_YET_CREATED
ACT_GIT_PUSH=NOT_YET_EXECUTED
ACT_PULL_REQUEST=NOT_YET_CREATED
ACT_GIT_INTEGRATION=NOT_AUTHORIZED
EXACT_BASE_MAIN_SHA=18f0b7bcc127b8e562f322e5cbe8068ef6a7d0a3
STABLE_RELEASE=NO_GO
STABLE_TLS_RISK_DISPOSITION=PENDING
STABLE_SOAK_DISPOSITION=PENDING
STABLE_TAG=NOT_AUTHORIZED
STABLE_PUBLICATION=NOT_AUTHORIZED
TASK_8_FINAL_CLOSURE=PENDING
```

La aprobación del acta no implica cierre de SUBTASK 8.8, aceptación de riesgos para distribución estable, aprobación de GO ni publicación de CicadaPort `v3.0.0`. La creación y preparación de la rama no autorizan automáticamente su merge protegido; éste requiere una decisión independiente.
