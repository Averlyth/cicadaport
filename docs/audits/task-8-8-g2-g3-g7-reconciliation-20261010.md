# TASK 8.8 — G2/G3/G7 reconciliación vigente posterior a G5

**Corte:** 2026-10-10 UTC. **Base exacta:** `main@62fa8c3a7e1b0d8e6002a302f19b6484ea0d75c1`. **Estado:** propuesta documental, no integrada.

Este documento añade evidencia vigente; no modifica los contratos congelados ni reemplaza los registros históricos. G2/G3/G7 NO se consideran cerrados por la mera existencia del borrador.

## G5: implementación y controles

- PR [#46](https://github.com/Averlyth/cicadaport/pull/46), commit fuente firmado `9a04043506b41e63284a4ce8bb04a0d020067d08`, merge firmado `62fa8c3a7e1b0d8e6002a302f19b6484ea0d75c1`, padres `6b58771c55201b4df7c6e874d3fbef008108926f` y `9a04043506b41e63284a4ce8bb04a0d020067d08`; tres archivos.
- [CI posmerge](https://github.com/Averlyth/cicadaport/actions/runs/38015618841): SUCCESS; 32/32 checks exactos correctos, sin omisiones.
- [CodeQL](https://github.com/Averlyth/cicadaport/actions/runs/38015618948): SUCCESS; regla `go/disabled-certificate-check`, alerta [#2](https://github.com/Averlyth/cicadaport/security/code-scanning/2): `fixed` en consulta G7 (anteriormente FIXED el 2026-10-10T02:05:30Z).
- Go exige cadena X.509, vigencia y hostname válidos antes de capturar banners TLS o enviar HEAD. El código Python de referencia usa aún un comportamiento distinto, fuera del motor Go público; no declararlo una equivalencia de confianza.

## G2 — Estado canónico (propuesta)

- Fuente y distribución del árbol: `3.0.0` (candidata estable, no publicada).
- Última prerelease pública verificada en consulta anterior: `v3.0.0-rc.1`.
- RC3: candidata fuente históricamente probada, sin tag ni GitHub Release `v3.0.0-rc.3` publicados. Requiere G4.
- Actualizaciones selectivas: `SECURITY.md`, `ROADMAP.md`, `README.md`, `docs/implementation/task-5-4-go-service-evidence-v2.md`, adenda al final de `docs/task-8-status.md`.
- No alterar el texto de actas con fecha anterior; conservar la negativa histórica CodeQL/soak por su corte original.

## G3 — Matriz contractual SUBTASK 8.5 (20 condiciones)

| Criterio contractual | Evidencia de referencia | Limitación | Estado documental |
| --- | --- | --- | --- |
| `CLEAN_INSTALL` | Installed artifacts; TASK 6.4 | CI positiva; comprobar evidencia individual | **PENDIENTE DE ACTA FINAL** |
| `WHEEL_INSTALL` | Installed artifacts; wheel build | CI positiva; comprobar evidencia individual | **PENDIENTE DE ACTA FINAL** |
| `SDIST_INSTALL` | Installed artifacts; sdist build | CI positiva; comprobar evidencia individual | **PENDIENTE DE ACTA FINAL** |
| `CLI_SMOKE` | Installed artifacts CLI | CI positiva; comprobar evidencia individual | **PENDIENTE DE ACTA FINAL** |
| `TUI_SMOKE` | Installed artifacts TUI | CI positiva; comprobar evidencia individual | **PENDIENTE DE ACTA FINAL** |
| `RUST_ENGINE` | Rust 1.97.1; native integration | CI positiva | **PENDIENTE DE ACTA FINAL** |
| `GO_EVIDENCE_ENGINE` | Go 1.26.9; native integration; G5 | CI positiva | **PENDIENTE DE ACTA FINAL** |
| `SESSION_CREATE` | TASK 6 and sessions tests | Vincular caso/log exactos | **PENDIENTE DE ACTA FINAL** |
| `SESSION_RESUME` | TASK 6 and sessions tests | Vincular caso/log exactos | **PENDIENTE DE ACTA FINAL** |
| `SESSION_RECOVERY` | TASK 6 and sessions tests | Vincular caso/log exactos | **PENDIENTE DE ACTA FINAL** |
| `CANCELLATION` | Rust and bridges cancellation tests | CI positiva; probar ruta final | **PENDIENTE DE ACTA FINAL** |
| `REPORT_GENERATION` | Report integration / installed artifacts | Vincular caso/log exactos | **PENDIENTE DE ACTA FINAL** |
| `SECURE_ARTIFACTS` | Secure artifacts tests / supply chain | CI positiva; vincular artefacto | **PENDIENTE DE ACTA FINAL** |
| `CONFIG_VALIDATION` | TASK 6.2 | CI positiva; comprobar evidencia individual | **PENDIENTE DE ACTA FINAL** |
| `HEALTH` | TASK 6.3 | CI positiva; comprobar evidencia individual | **PENDIENTE DE ACTA FINAL** |
| `READINESS` | TASK 6.3 | CI positiva; comprobar evidencia individual | **PENDIENTE DE ACTA FINAL** |
| `DIAGNOSTICS` | TASK 6.3 | CI positiva; comprobar evidencia individual | **PENDIENTE DE ACTA FINAL** |
| `UPDATE_PLAN` | TASK 6.4 | CI positiva; no ejecución de actualización productiva | **PENDIENTE DE ACTA FINAL** |
| `ROLLBACK_PLAN` | TASK 6.4 | CI positiva; no ejecución de rollback productivo | **PENDIENTE DE ACTA FINAL** |
| `LONG_RUNNING_OPERATION` | TASK 6.5 synthetic soak | Soak sintético aprobado; G6 real pendiente | **PENDIENTE DE ACTA FINAL** |

Un resultado global de CI no sustituye la identificación de la prueba/artefacto que cumple cada contrato. Los veinte renglones exigen esa conciliación antes del `SERVICE_READINESS=PASS` definitivo; no afirmar un SLA o soporte fuera de Linux x86_64 Ubuntu 22.04/24.04 Python 3.10–3.13.

## G7 — Inventario de seguridad observado

```json
{
  "code_scanning": {
    "status": "VERIFIED",
    "open_count": 0,
    "alerts": []
  },
  "dependabot": {
    "status": "VERIFIED",
    "open_count": 0,
    "alerts": []
  },
  "secret_scanning": {
    "status": "VERIFIED",
    "open_count": 0,
    "alerts": []
  },
  "alert_2": {
    "number": 2,
    "state": "fixed",
    "fixed_at": "2026-10-10T02:05:30Z",
    "dismissed_at": null
  }
}
```

Alerta nativa #2 actual: `fixed`. `FIXED` significa corrección detectada por CodeQL, sin descarte artificial. Fallos de API o visibilidad generan `UNVERIFIED`, nunca `0` por defecto. El SBOM requiere verificar específicamente la clausura transitiva y las versiones de paquetes sobre el SHA final; ningún recuento de versiones se certifica por este documento.

## G4 y G6 — Bloqueos que NO se cierran con documentación

**G4 / FINAL_RC:** la cláusula 13 del contrato propone `v3.0.0-rc.3`. Solo una decisión contractual expresa del arquitecto puede permitir sustituir la publicación RC3 por equivalencia de evidencia fuente, o debe ejecutarse el camino RC3 autorizado. No se crea tag, release ni se retrofecha evidencia.

**G6 / SOAK:** diez iteraciones sintéticas en CI no demuestran treinta minutos continuos en operación representativa. Ejecutar ensayo autorizado con umbrales y presupuesto de recursos, o aprobar una aceptación estable de alcance limitado sin declarar endurance. Ambos caminos exigen una decisión explícita y registro de límites.

## Matriz contractual 8.8 — evaluación, no aprobación

| Gate | Resultado en este corte |
| --- | --- |
| `DEPENDENCY_BACKLOG` | PENDIENTE inventario final |
| `RESOURCE_HYGIENE` | CI técnico PASS; alcance acotado |
| `TEST_BASELINE` | Conciliación previa documentada; acta final pendiente |
| `QUALITY_GATES` | PASS técnico exact-main 32/32 |
| `DOCUMENTATION` | CORRECCIÓN PREPARADA FUERA DE GIT |
| `SERVICE_READINESS` | MATRIZ 20/20 FORMADA; certificación individual pendiente |
| `FINAL_RC` | G4 decisión pendiente |
| `ENTERPRISE_ACCEPTANCE` | Source milestone histórico aceptado; revisión estable pendiente |
| `SECURITY_GATES` | TLS corregido; G7 inventario/SBOM pendiente |
| `SUPPLY_CHAIN` | CI positivo; auditoría final SBOM pendiente |
| `OPEN_BLOCKERS=0` | NO CERTIFICADO |

**STABLE_RELEASE=NO_GO.** Este borrador no autoriza merge, tag, publicación estable o comienzo de TASK 9.
