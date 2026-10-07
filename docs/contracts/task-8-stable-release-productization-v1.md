# SRP-CICADAPORT-TASK-8-001 — CicadaPort 3.0.0 Stable Release Productization

```text
CONTRACT=SRP-CICADAPORT-TASK-8-001
VERSION=1.0-CANDIDATE
STATUS=AUTHORIZED_IN_IMPLEMENTATION

PROJECT=CICADAPORT
ORGANIZATION=AVERLYTH

TASK_8=MVP_3_0_0_PRODUCTIZATION_AND_STABLE_RELEASE
TASK_8_BRANCH=feat/task-8-mvp-3-stable-productization

AUTHORIZED_BASE=main@b1c963f93cb21a2e3b06900451d96e5df752f0b3

CURRENT_SOURCE_VERSION=3.0.0-rc.2
CURRENT_PYTHON_VERSION=3.0.0rc2
CURRENT_PUBLIC_RELEASE=v3.0.0-rc.1

PROPOSED_FINAL_RC=3.0.0-rc.3
PROPOSED_FINAL_PYTHON_RC=3.0.0rc3
TARGET_STABLE_RELEASE=v3.0.0

NEW_NETWORK_CAPABILITIES=BLOCKED
HISTORY_REWRITE=PROHIBITED
FORCE_PUSH=PROHIBITED
CI_BYPASS=PROHIBITED
STABLE_PUBLICATION=REQUIRES_SEPARATE_FINAL_GATE
```

## 1. Propósito

TASK 8 transforma el estado actual de CicadaPort en la primera versión estable
publicable de Averlyth.

El objetivo es obtener una versión `3.0.0` instalable, verificable, operable,
recuperable, documentada y soportable para prestación de servicio dentro de la
matriz y superficie funcional oficialmente declaradas.

Esta TASK no persigue incrementar todavía la superficie de reconocimiento ni
incorporar nuevas técnicas de red. Su objetivo es cerrar correctamente el
producto que ya existe.

La definición de "funcionalidad completa" utilizada por esta TASK significa
completitud dentro del alcance soportado de CicadaPort 3.0.0, no implementación
de todas las técnicas posibles de reconocimiento de red.

## 2. Base autorizada

La única base autorizada para iniciar TASK 8 es:

```text
main@b1c963f93cb21a2e3b06900451d96e5df752f0b3
```

Rama autorizada:

```text
feat/task-8-mvp-3-stable-productization
```

El preflight inicial demostró:

```text
HEAD=b1c963f93cb21a2e3b06900451d96e5df752f0b3
main=b1c963f93cb21a2e3b06900451d96e5df752f0b3
origin/main=b1c963f93cb21a2e3b06900451d96e5df752f0b3
WORKTREE=CLEAN
BASE_SYNCHRONIZED=YES
```

## 3. Estado heredado

Permanecen preservados y no se reabren por esta TASK:

```text
HITO_3=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
TASK_4=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
TASK_5=INTEGRATED_IN_MAIN
TASK_6=INTEGRATED_IN_MAIN
TASK_7=INTEGRATED_IN_MAIN
CP_ORG_01=COMPLETED_CLOSED_FROZEN
```

Los documentos históricos que contienen estados intermedios se conservan como
evidencia temporal y no deben modificarse retroactivamente para aparentar un
estado que no tenían cuando fueron creados.

TASK 8 debe introducir fuentes de estado actuales cuando sea necesario.

## 4. Arquitectura preservada

La arquitectura pública sigue siendo:

```text
Python -> Rust -> Python -> Go -> Python
```

Invariantes:

1. Python mantiene orquestación, política, CLI, TUI, persistencia,
   presentación y compatibilidad.
2. Rust continúa siendo el motor público obligatorio para TCP.
3. Go continúa siendo obligatorio para evidencia de servicio cuando la fase de
   banners está habilitada.
4. No existe fallback público silencioso hacia motores Python.
5. Las implementaciones Python internas pueden permanecer como referencia,
   paridad o soporte de pruebas sin convertirse en motores públicos
   seleccionables.
6. Los contratos nativos y canónicos congelados no se reinterpretan
   silenciosamente.
7. Toda actividad de red debe permanecer limitada a sistemas propios,
   loopback, laboratorio o alcance expresamente autorizado.

## 5. Alcance de TASK 8

TASK 8 comprende exclusivamente las siguientes materias de productización:

- reconciliación de dependencias;
- eliminación de warnings y fugas de recursos relevantes;
- corrección de defectos funcionales encontrados durante aceptación;
- reconciliación del baseline de pruebas;
- gobierno de cobertura;
- análisis estático Python;
- calidad de código;
- seguridad del software;
- auditoría de dependencias;
- secret scanning;
- SAST;
- supply chain;
- SBOM;
- provenance y attestations;
- build reproducible;
- empaquetado;
- wheel y sdist;
- instalación limpia;
- actualización;
- rollback;
- diagnóstico;
- health y readiness;
- observabilidad;
- cancelación;
- persistencia;
- recuperación;
- sesiones largas;
- reanudación;
- artefactos seguros;
- documentación técnica;
- documentación de usuario;
- documentación operativa;
- documentación de seguridad;
- documentación de soporte;
- release notes;
- release engineering;
- construcción de la release candidate final;
- aceptación empresarial;
- publicación estable controlada.

## 6. Materias expresamente fuera de alcance

Hasta el cierre de `v3.0.0` permanecen bloqueadas:

- descubrimiento activo general de hosts;
- ICMP discovery;
- ARP discovery;
- raw sockets;
- raw packets;
- SYN scan;
- nuevas modalidades públicas UDP;
- técnicas de evasión;
- fingerprinting activo de sistemas operativos;
- detección general de vulnerabilidades;
- explotación;
- post-explotación;
- scripting ofensivo;
- escaneo externo no autorizado;
- selección pública arbitraria de motores;
- expansión de plataforma sin validación formal.

Una corrección necesaria para que una capacidad ya declarada funcione conforme
a contrato no se considera expansión funcional.

## 7. Descomposición obligatoria

| Subtask | Resultado requerido |
| --- | --- |
| 8.0 | Gobierno, contrato y baseline de release |
| 8.1 | Reconciliación completa del backlog de dependencias |
| 8.2 | Runtime y resource hygiene |
| 8.3 | Baseline de pruebas, cobertura y quality gates Python |
| 8.4 | Reconciliación documental y estado canónico |
| 8.5 | Service readiness y aceptación operativa |
| 8.6 | Construcción de la release candidate final |
| 8.7 | Enterprise acceptance, soak y validación integral |
| 8.8 | Gate definitivo GO/NO-GO de versión estable |
| 8.9 | Publicación `v3.0.0` y verificación post-release |

Las subtasks se ejecutan de forma controlada. Una subtask posterior no debe
utilizarse para ocultar una divergencia no resuelta de una anterior.

## 8. SUBTASK 8.1 — Dependency backlog reconciliation

El backlog inicial está compuesto por:

```text
PR_9=serde_json
PR_10=serde
PR_14=pytest-cov
PR_15=pytest
PR_18=tokio
PR_19=actions/attest
PR_20=flake8
PR_21=mypy
```

Orden inicial de evaluación:

```text
8.1.1 PR #9  serde_json
8.1.2 PR #14 pytest-cov
8.1.3 PR #15 pytest
8.1.4 PR #20 flake8
8.1.5 PR #21 mypy
8.1.6 PR #10 serde
8.1.7 PR #18 tokio
8.1.8 PR #19 actions/attest
8.1.9 auditoría consolidada
```

Cada dependencia debe terminar con una decisión explícita:

```text
MERGED
SUPERSEDED
DEFERRED_WITH_JUSTIFICATION
CLOSED_NOT_REQUIRED
```

Ninguna PR se fusiona únicamente porque Dependabot la haya generado o porque un
CI incompleto figure en verde.

## 9. SUBTASK 8.2 — Runtime and resource hygiene

La salida requerida es:

```text
KNOWN_RESOURCE_LEAKS=0
REPRODUCIBLE_RESOURCE_WARNINGS=0
UNBOUNDED_RESOURCE_PATHS=0
```

Se revisarán específicamente:

- conexiones SQLite;
- sesiones;
- procesos nativos;
- pipes;
- archivos;
- temporary files;
- descriptores;
- workers;
- cancelación;
- recuperación ante excepciones.

Los warnings existentes deben ser clasificados y corregidos o documentados con
evidencia técnica suficiente antes del gate estable.

## 10. SUBTASK 8.3 — Test baseline and quality gates

TASK 8 debe reconciliar el baseline real de pruebas antes de declarar estabilidad.

La diferencia histórica observada entre ejecuciones no puede resolverse
alterando artificialmente contadores.

Debe determinarse por qué una baseline previa registraba:

```text
531 passed
2 skipped
72 subtests
83 percent coverage
```

mientras que el baseline actual observado registra:

```text
528 passed
5 skipped
72 subtests
82 percent coverage
```

La reconciliación debe demostrar si la diferencia procede de cambios
intencionales, entorno, clasificación de tests, eliminación de casos,
condicionales o una regresión real.

Quality gates requeridos antes de estable:

```text
PYTEST=PASS
BLACK_CHECK=PASS
FLAKE8=PASS
MYPY=PASS
COVERAGE_FLOOR=ENFORCED
```

El valor definitivo del coverage floor se fijará únicamente después de medir y
reconciliar la baseline, evitando escoger un umbral que oculte regresiones o
bloquee artificialmente código actualmente válido.

## 11. SUBTASK 8.4 — Documentation reconciliation

Se preservan los documentos históricos existentes.

TASK 8 debe crear una fuente canónica de estado vigente y reconciliar, cuando
corresponda:

- README;
- ROADMAP;
- CHANGELOG;
- SECURITY;
- CONTRIBUTING;
- user manual;
- operations;
- architecture;
- support matrix;
- installation;
- upgrade;
- rollback;
- recovery;
- release documentation;
- estado actual de TASK 5;
- integración de TASK 6;
- integración de TASK 7;
- migración organizacional;
- versión y canales de release.

No se alterarán documentos históricos únicamente para reemplazar estados que
eran correctos en el momento en que fueron emitidos.

## 12. SUBTASK 8.5 — Service readiness

Para declarar CicadaPort apto para prestación de servicio debe verificarse como
mínimo:

```text
CLEAN_INSTALL=PASS
WHEEL_INSTALL=PASS
SDIST_INSTALL=PASS
CLI_SMOKE=PASS
TUI_SMOKE=PASS
RUST_ENGINE=PASS
GO_EVIDENCE_ENGINE=PASS
SESSION_CREATE=PASS
SESSION_RESUME=PASS
SESSION_RECOVERY=PASS
CANCELLATION=PASS
REPORT_GENERATION=PASS
SECURE_ARTIFACTS=PASS
CONFIG_VALIDATION=PASS
HEALTH=PASS
READINESS=PASS
DIAGNOSTICS=PASS
UPDATE_PLAN=PASS
ROLLBACK_PLAN=PASS
LONG_RUNNING_OPERATION=PASS
```

La aceptación se realiza en la matriz oficialmente soportada. Una plataforma no
validada no puede declararse soportada por inferencia.

## 13. SUBTASK 8.6 — Final release candidate

La candidata final propuesta es:

```text
SemVer=3.0.0-rc.3
Python=3.0.0rc3
GitTag=v3.0.0-rc.3
```

`3.0.0-rc.2` permanece como estado fuente histórico no publicado.

La candidata final solo puede construirse después de completar las subtasks
previas y no debe publicarse usando contenido distinto bajo una etiqueta de
versión ya existente.

## 14. SUBTASK 8.7 — Enterprise acceptance

La aceptación integral debe incluir:

- tests Python;
- tests Rust;
- clippy;
- rustfmt;
- tests Go;
- go vet;
- race detector;
- ShellCheck;
- integración;
- análisis estático;
- secret scanning;
- SAST;
- auditorías de dependencias;
- build reproducible;
- release lock;
- installed-artifact tests;
- manifests;
- hashes;
- SBOM;
- provenance;
- attestations;
- recuperación;
- cancelación;
- soak tests;
- bounded-resource validation.

No se acepta como evidencia suficiente el éxito aislado de un subconjunto.

## 15. SUBTASK 8.8 — Stable release GO/NO-GO

Antes de publicar `v3.0.0` deben cumplirse simultáneamente:

```text
DEPENDENCY_BACKLOG=CLOSED
RESOURCE_HYGIENE=PASS
TEST_BASELINE=RECONCILED
QUALITY_GATES=PASS
DOCUMENTATION=CURRENT
SERVICE_READINESS=PASS
FINAL_RC=PASS
ENTERPRISE_ACCEPTANCE=PASS
SECURITY_GATES=PASS
SUPPLY_CHAIN=PASS
OPEN_BLOCKERS=0
```

Cualquier condición distinta produce:

```text
STABLE_RELEASE=NO_GO
```

La transición a `GO` requiere evidencia reproducible.

## 16. SUBTASK 8.9 — Stable publication

La publicación estable comprende:

- commit definitivo;
- CI definitivo;
- tag firmado `v3.0.0`;
- release GitHub;
- wheel;
- sdist;
- manifiestos;
- hashes;
- SBOM;
- provenance;
- attestations;
- verificación de artefactos instalados;
- verificación post-release;
- documentación final;
- registro de cierre.

La publicación estable requiere autorización final independiente después del
GO/NO-GO técnico.

## 17. Matriz de salida mínima de TASK 8

```text
FUNCTIONAL_ACCEPTANCE=PASS
REGRESSION_TESTS=PASS

PYTHON_TESTS=PASS
BLACK=PASS
FLAKE8=PASS
MYPY=PASS
COVERAGE_GOVERNANCE=PASS

RUST_TESTS=PASS
RUSTFMT=PASS
CLIPPY=PASS

GO_TESTS=PASS
GO_VET=PASS
GO_RACE=PASS

SHELLCHECK=PASS

SECRET_SCANNING=PASS
SAST=PASS
DEPENDENCY_AUDITS=PASS

RELEASE_LOCK=PASS
REPRODUCIBLE_BUILD=PASS
SBOM=PASS
PROVENANCE=PASS
ATTESTATIONS=PASS

INSTALLATION=PASS
UPDATE=PASS
ROLLBACK=PASS
RECOVERY=PASS
LONG_RUNNING_OPERATION=PASS

DOCUMENTATION=CURRENT
SUPPORT_MATRIX=CURRENT
SECURITY_POLICY=CURRENT

STABLE_RELEASE=v3.0.0
```

## 18. Reglas de trazabilidad

Cada cambio material debe conservar:

1. subtask;
2. motivación;
3. baseline;
4. archivos modificados;
5. pruebas ejecutadas;
6. resultados;
7. commit identificable;
8. CI remoto;
9. decisión;
10. estado final.

No se permite:

- reescribir historial;
- force push;
- saltar required checks;
- ocultar fallos mediante exclusiones no justificadas;
- bajar controles de seguridad únicamente para obtener CI verde;
- alterar contratos congelados sin una nueva versión explícita.

## 19. Flujo de integración

```text
diagnóstico
-> corrección
-> validación focalizada
-> validación completa
-> revisión de diff
-> commit firmado
-> push no forzado
-> pull request
-> CI remoto
-> revisión
-> merge controlado
-> CI de main
-> evidencia de cierre
```

## 20. Restricciones de publicación

TASK 8 está autorizada para preparación material y validación.

Este contrato no autoriza automáticamente:

```text
MERGE_TO_MAIN
FINAL_RC_PUBLICATION
STABLE_TAG_CREATION
STABLE_RELEASE_PUBLICATION
PACKAGE_PUBLICATION
TASK_8_CLOSURE_TAG
```

Cada gate irreversible debe estar respaldado por el estado técnico requerido.

## 21. Resultado esperado

Al finalizar TASK 8, CicadaPort debe poder declararse:

```text
PRODUCT=CicadaPort
VERSION=3.0.0
CHANNEL=stable
STATUS=PUBLICABLE_AND_SERVICE_READY
SUPPORTED_SCOPE=VERIFIED
DOCUMENTATION=CURRENT
SECURITY_GATES=PASS
SUPPLY_CHAIN=VERIFIED
RELEASE_ARTIFACTS=VERIFIED
```

La ampliación funcional posterior deberá realizarse sobre la baseline estable
resultante y bajo nuevas TASKS explícitas.
