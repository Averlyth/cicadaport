# Estado formal de TASK 8

**Corte de evidencia (2026-10-08, Stage G precommit):** Los indicadores de commit, CI y artefactos pendientes registran el estado en el momento de esta evaluación; sus resultados posteriores deben añadirse sin alterar retroactivamente esta evidencia.

```text
PROJECT=CICADAPORT
ORGANIZATION=AVERLYTH

TASK_8=MVP_3_0_0_PRODUCTIZATION_AND_STABLE_RELEASE
TASK_8_STATUS=AUTHORIZED_IN_IMPLEMENTATION

TASK_8_CONTRACT=SRP-CICADAPORT-TASK-8-001
TASK_8_CONTRACT_VERSION=1.0-CANDIDATE

TASK_8_BASE=b1c963f93cb21a2e3b06900451d96e5df752f0b3
TASK_8_BRANCH=feat/task-8-mvp-3-stable-productization

CURRENT_SOURCE_VERSION=3.0.0-rc.3
CURRENT_PUBLIC_RELEASE=v3.0.0-rc.1
PROPOSED_FINAL_RC=v3.0.0-rc.3
TARGET_STABLE_RELEASE=v3.0.0

SUBTASK_8_0=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
SUBTASK_8_0_IMPLEMENTATION_COMMIT=e8e9d0f3ec72a783f6b1289c3a965b720226fc02
SUBTASK_8_0_PR=24
SUBTASK_8_0_MERGE_COMMIT=291b05ffe82e402c0b7deff41f4d4ce034ebe4d1
SUBTASK_8_0_PREMERGE_PUSH_CI_RUN=37666907282
SUBTASK_8_0_PREMERGE_PR_CI_RUN=37666962395
SUBTASK_8_0_POST_MERGE_CI_RUN=37668126398
SUBTASK_8_0_POST_MERGE_CI_ATTEMPT_1=CANCELLED
SUBTASK_8_0_POST_MERGE_CI_ATTEMPT_2=PASS
SUBTASK_8_0_POST_MERGE_CI=PASS_AFTER_RERUN

SUBTASK_8_1=INITIAL_BACKLOG_INTEGRATED_POST_BASELINE_INTAKE_PENDING
SUBTASK_8_1_1=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
SUBTASK_8_1_1_SOURCE_PR=9
SUBTASK_8_1_1_SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
SUBTASK_8_1_1_DEPENDENCY=serde_json
SUBTASK_8_1_1_FROM=1.0.150
SUBTASK_8_1_1_TO=1.0.151
SUBTASK_8_1_1_IMPLEMENTATION_COMMIT=ff570e4e6187330497d11c73507b158f98108ad8
SUBTASK_8_1_1_PR=26
SUBTASK_8_1_1_MERGE_COMMIT=262324198b5a9dcead758d2fdd9809cda8689d34
SUBTASK_8_1_1_PREMERGE_PUSH_CI_RUN=37674586239
SUBTASK_8_1_1_PREMERGE_PR_CI_RUN=37674617719
SUBTASK_8_1_1_POST_MERGE_CI_RUN=37675364589
SUBTASK_8_1_1_POST_MERGE_CI=PASS

SUBTASK_8_1_2=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
SUBTASK_8_1_2_SOURCE_PR=14
SUBTASK_8_1_2_SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
SUBTASK_8_1_2_DEPENDENCY=pytest-cov
SUBTASK_8_1_2_FROM=>=7,<8
SUBTASK_8_1_2_TO=>=7.1.0,<8
SUBTASK_8_1_2_IMPLEMENTATION_COMMIT=f4544c9130f5eb1de950bd4b0de1d12235384790
SUBTASK_8_1_2_PR=27
SUBTASK_8_1_2_MERGE_COMMIT=8ffd6d7af722038234b85d978bddb90e0a5be616
SUBTASK_8_1_2_PREMERGE_PUSH_CI_RUN=37682321968
SUBTASK_8_1_2_PREMERGE_PR_CI_RUN=37682400146
SUBTASK_8_1_2_POST_MERGE_CI_RUN=37682899150
SUBTASK_8_1_2_POST_MERGE_CI=PASS

SUBTASK_8_1_3=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
SUBTASK_8_1_3_SOURCE_PR=15
SUBTASK_8_1_3_SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
SUBTASK_8_1_3_DEPENDENCY=pytest
SUBTASK_8_1_3_FROM=>=9,<10
SUBTASK_8_1_3_TO=>=9.1.1,<10
SUBTASK_8_1_3_IMPLEMENTATION_COMMIT=98dcbeddabe880733c35f76a967021f93724f00c
SUBTASK_8_1_3_PR=28
SUBTASK_8_1_3_MERGE_COMMIT=cce10142c859e4b20fccc1aec16a342f054d6e73
SUBTASK_8_1_3_PREMERGE_PUSH_CI_RUN=37684139764
SUBTASK_8_1_3_PREMERGE_PR_CI_RUN=37684216376
SUBTASK_8_1_3_POST_MERGE_CI_RUN=37684779206
SUBTASK_8_1_3_POST_MERGE_CI=PASS

SUBTASK_8_1_4=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
SUBTASK_8_1_4_SOURCE_PR=20
SUBTASK_8_1_4_SOURCE_PR_RESOLUTION=MERGED_DIRECT
SUBTASK_8_1_4_DEPENDENCY=flake8
SUBTASK_8_1_4_FROM=>=7,<8
SUBTASK_8_1_4_TO=>=7.4.1,<8
SUBTASK_8_1_4_SOURCE_COMMIT=14e9b494ab0035242787d2f747014bedf34c6893
SUBTASK_8_1_4_MERGE_COMMIT=b7d88f316339d6cb2478675ae27ad6e2f894d3a5
SUBTASK_8_1_4_PREMERGE_PUSH_CI_RUN=37685065461
SUBTASK_8_1_4_PREMERGE_PR_CI_RUN=37685072512
SUBTASK_8_1_4_POST_MERGE_CI_RUN=37685685963
SUBTASK_8_1_4_POST_MERGE_CI=PASS

SUBTASK_8_1_5=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
SUBTASK_8_1_5_SOURCE_PR=21
SUBTASK_8_1_5_SOURCE_PR_RESOLUTION=MERGED_DIRECT
SUBTASK_8_1_5_DEPENDENCY=mypy
SUBTASK_8_1_5_FROM=>=1.19,<2
SUBTASK_8_1_5_TO=>=2.4.0,<3
SUBTASK_8_1_5_SOURCE_COMMIT=982f41b539182b9d2331d55e9f1d8d41e717a827
SUBTASK_8_1_5_MERGE_COMMIT=550fd221cb4ff1c5435bc02b58bc2057f67b3cef
SUBTASK_8_1_5_PREMERGE_PUSH_CI_RUN=37685959419
SUBTASK_8_1_5_PREMERGE_PR_CI_RUN=37685966937
SUBTASK_8_1_5_POST_MERGE_CI_RUN=37687530157
SUBTASK_8_1_5_POST_MERGE_CI=PASS
SUBTASK_8_1_5_MYPY_BASELINE_VERSION=1.20.2
SUBTASK_8_1_5_MYPY_TARGET_VERSION=2.4.0
SUBTASK_8_1_5_MYPY_BASELINE_ERRORS=389
SUBTASK_8_1_5_MYPY_TARGET_ERRORS=389
SUBTASK_8_1_5_MYPY_NEW_ONLY_ERRORS=0
SUBTASK_8_1_5_MYPY_DIFFERENTIAL=PASS

SUBTASK_8_1_6=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
SUBTASK_8_1_6_SOURCE_PR=10
SUBTASK_8_1_6_SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
SUBTASK_8_1_6_DEPENDENCY=serde
SUBTASK_8_1_6_SERDE_FROM=1.0.228
SUBTASK_8_1_6_SERDE_TO=1.0.229
SUBTASK_8_1_6_SYN_FROM=2.0.117
SUBTASK_8_1_6_SYN_TO=3.0.3
SUBTASK_8_1_6_IMPLEMENTATION_COMMIT=3ad4deb55c8dbd2d972bde2a1f566d2e1988cf9f
SUBTASK_8_1_6_PR=29
SUBTASK_8_1_6_MERGE_COMMIT=8d848e1d8f8a97f71fdefe8b01cfbc23a007b5d3
SUBTASK_8_1_6_PREMERGE_PUSH_CI_RUN=37689226362
SUBTASK_8_1_6_PREMERGE_PR_CI_RUN=37689430822
SUBTASK_8_1_6_POST_MERGE_CI_RUN=37690025028
SUBTASK_8_1_6_POST_MERGE_CI=PASS

SUBTASK_8_1_7=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
SUBTASK_8_1_7_SOURCE_PR=18
SUBTASK_8_1_7_SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
SUBTASK_8_1_7_DEPENDENCY=tokio
SUBTASK_8_1_7_FROM=1.52.3
SUBTASK_8_1_7_TO=1.53.1
SUBTASK_8_1_7_IMPLEMENTATION_COMMIT=0c1c842b7fc6414e2c3f663a2b9a0e17ded1368d
SUBTASK_8_1_7_TEST_CONTRACT_COMMIT=c13728a99bb883881ffeea5eff31d1b0565007a1
SUBTASK_8_1_7_PR=30
SUBTASK_8_1_7_MERGE_COMMIT=a8b0791fafb516ed8f167099e715be283e90e102
SUBTASK_8_1_7_PREMERGE_PUSH_CI_RUN=37692475263
SUBTASK_8_1_7_PREMERGE_PR_CI_RUN=37692480885
SUBTASK_8_1_7_POST_MERGE_CI_RUN=37695775245
SUBTASK_8_1_7_POST_MERGE_CI=PASS
SUBTASK_8_1_7_RUNTIME_STRESS_ITERATIONS=25
SUBTASK_8_1_7_RUNTIME_STRESS=PASS
SUBTASK_8_1_7_PYTHON_CONTRACT_FIX=PASS
SUBTASK_8_1_7_RESOURCE_WARNINGS=6_DEFERRED_TO_8_2

SUBTASK_8_1_8=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
SUBTASK_8_1_8_TARGET_PR=19
SUBTASK_8_1_8_DEPENDENCY=actions/attest
SUBTASK_8_1_8_FROM=4.2.1
SUBTASK_8_1_8_TO=4.2.2
SUBTASK_8_1_8_FROM_SHA=508db95dd578ae2727ebd6217d5ba78e4fbda05d
SUBTASK_8_1_8_TO_SHA=1e69f48acb82d1966a394da916b4c1698aa569d6
SUBTASK_8_1_8_SUPPLY_CHAIN_VALIDATION=PASS
SUBTASK_8_1_8_SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
SUBTASK_8_1_8_PR=31
SUBTASK_8_1_8_MERGE_COMMIT=67b900b4c378d766b8829231b3e9e930baceac71
SUBTASK_8_1_8_POST_MERGE_CI_RUN=37698558022
SUBTASK_8_1_8_POST_MERGE_CI=PASS

SUBTASK_8_2=IMPLEMENTED_PR37_REMOTE_CI_PASS_PENDING_FORMAL_CLOSURE
SUBTASK_8_3=IMPLEMENTED_PR37_REMOTE_CI_PASS_PENDING_FORMAL_CLOSURE
SUBTASK_8_4=IMPLEMENTED_PR37_REMOTE_CI_PASS_PENDING_FORMAL_CLOSURE
SUBTASK_8_5=IMPLEMENTED_PR37_REMOTE_CI_PASS_PENDING_FORMAL_CLOSURE
SUBTASK_8_6=RC3_SOURCE_INTEGRATED_PUBLICATION_NOT_AUTHORIZED
SUBTASK_8_7=SOURCE_PR37_CI_PASS_RELEASE_ACCEPTANCE_PENDING
SUBTASK_8_8=BLOCKED
SUBTASK_8_9=BLOCKED

NEW_FUNCTIONAL_EXPANSION=BLOCKED
STABLE_RELEASE_PUBLICATION=NOT_AUTHORIZED
```

## Propósito

TASK 8 convierte la implementación actual de CicadaPort en la primera versión
estable publicable de Averlyth y apta para prestación de servicio dentro de su
alcance oficialmente soportado.

La TASK prioriza estabilización, corrección, calidad, operación, seguridad,
documentación, empaquetado y release engineering antes de ampliar
funcionalidades.

## Baseline autorizado

```text
main@b1c963f93cb21a2e3b06900451d96e5df752f0b3
```

El preflight confirmó igualdad entre `HEAD`, `main`, `origin/main` y
`merge-base` antes de crear la rama de TASK 8.

## Estado heredado

```text
HITO_3=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
TASK_4=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
TASK_5=INTEGRATED_IN_MAIN
TASK_6=INTEGRATED_IN_MAIN
TASK_7=INTEGRATED_IN_MAIN
CP_ORG_01=COMPLETED_CLOSED_FROZEN
```

Los estados intermedios conservados en documentos históricos no se modifican
retroactivamente.

## Secuencia autorizada

```text
8.0 Governance, contract and release baseline
8.1 Dependency backlog reconciliation
8.2 Runtime and resource hygiene
8.3 Test baseline, coverage and Python quality gates
8.4 Documentation and canonical current-state reconciliation
8.5 Service readiness
8.6 Final release candidate
8.7 Enterprise acceptance and soak
8.8 Stable GO/NO-GO
8.9 v3.0.0 publication and post-release verification
```

## Cierre de SUBTASK 8.0

SUBTASK 8.0 queda cerrada y congelada sobre la integración verificada de la PR
`#24`.

Evidencia consolidada:

```text
IMPLEMENTATION_COMMIT=e8e9d0f3ec72a783f6b1289c3a965b720226fc02
IMPLEMENTATION_SIGNATURE=PASS_SSH_ED25519

PR=24
PR_PREMERGE_STATE=CLEAN
PR_PREMERGE_MERGEABLE=MERGEABLE

PREMERGE_PUSH_CI_RUN=37666907282
PREMERGE_PUSH_CI=PASS

PREMERGE_PR_CI_RUN=37666962395
PREMERGE_PR_CI=PASS

MERGE_COMMIT=291b05ffe82e402c0b7deff41f4d4ce034ebe4d1
MERGE_SIGNATURE=VERIFIED_VALID_BY_GITHUB
MERGE_PARENT_1=b1c963f93cb21a2e3b06900451d96e5df752f0b3
MERGE_PARENT_2=e8e9d0f3ec72a783f6b1289c3a965b720226fc02

POST_MERGE_CI_RUN=37668126398
POST_MERGE_CI_ATTEMPT_1=CANCELLED
POST_MERGE_CI_ATTEMPT_1_CLASSIFICATION=OPERATIONAL_CANCELLATION_NO_TEST_REGRESSION
POST_MERGE_CI_ATTEMPT_2=PASS
POST_MERGE_CI_ATTEMPT_2_SUCCESS_JOBS=26
POST_MERGE_CI=PASS_AFTER_RERUN

FILES_ADDED=2
INSERTIONS=725
DELETIONS=0
SCOPE_VIOLATIONS=0
```

El primer intento del CI post-merge terminó cancelado. Los jobs ya ejecutados
habían resultado satisfactorios salvo `Shell`, que quedó cancelado, y la
integración fue omitida como consecuencia de esa cancelación. El segundo intento
ejecutó 26 jobs y los 26 finalizaron satisfactoriamente. No existe evidencia de
una regresión funcional asociada al primer intento.

La imposibilidad del keyring local de verificar la firma RSA del merge de
GitHub no invalida la firma: GitHub registra el merge commit como
`verified=true` y `reason=valid`.

No se creó etiqueta específica para SUBTASK 8.0. El cierre contractual de TASK
8 y cualquier etiqueta institucional asociada permanecen reservados para el
gate final correspondiente.

## Cierre de SUBTASK 8.1.1

La reconciliación de `serde_json` se integró desde el baseline vigente de TASK 8.
La PR Dependabot original `#9` no fue fusionada: quedó cerrada como supersedida
por la PR `#26`.

```text
SOURCE_PR=9
SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
DEPENDENCY=serde_json
FROM=1.0.150
TO=1.0.151

IMPLEMENTATION_COMMIT=ff570e4e6187330497d11c73507b158f98108ad8
IMPLEMENTATION_SIGNATURE=PASS_SSH_ED25519
PR=26
MERGE_COMMIT=262324198b5a9dcead758d2fdd9809cda8689d34

LOCAL_RUST_TESTS=30_PASS_0_FAIL
LOCAL_CARGO_CHECK=PASS
LOCAL_CARGO_CLIPPY=PASS

PREMERGE_PUSH_CI_RUN=37674586239
PREMERGE_PUSH_CI=PASS
PREMERGE_PR_CI_RUN=37674617719
PREMERGE_PR_CI=PASS
POST_MERGE_CI_RUN=37675364589
POST_MERGE_CI=PASS
```

## Cierre de SUBTASK 8.1.2

La reconciliación de `pytest-cov` se integró desde el baseline vigente de TASK 8.
La PR Dependabot original `#14` no fue fusionada: quedó cerrada como supersedida
por la PR `#27`.

```text
SOURCE_PR=14
SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
DEPENDENCY=pytest-cov
FROM=>=7,<8
TO=>=7.1.0,<8

IMPLEMENTATION_COMMIT=f4544c9130f5eb1de950bd4b0de1d12235384790
IMPLEMENTATION_SIGNATURE=PASS_SSH_ED25519
PR=27
MERGE_COMMIT=8ffd6d7af722038234b85d978bddb90e0a5be616

LOCAL_PYTEST_COV_VERSION=7.1.0
LOCAL_TESTS=531_PASS_2_SKIPPED
LOCAL_SUBTESTS=72_PASS
LOCAL_WARNINGS=6_RESOURCE_WARNINGS_DEFERRED_TO_8_2
LOCAL_COVERAGE=83_PERCENT

PREMERGE_PUSH_CI_RUN=37682321968
PREMERGE_PUSH_CI=PASS
PREMERGE_PR_CI_RUN=37682400146
PREMERGE_PR_CI=PASS
POST_MERGE_CI_RUN=37682899150
POST_MERGE_CI=PASS
```

## Cierre de SUBTASK 8.1.3

La reconciliación de `pytest` se integró desde el baseline vigente de TASK 8.
La PR Dependabot original `#15` no fue fusionada: quedó cerrada como
supersedida por la PR `#28`.

```text
SOURCE_PR=15
SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
DEPENDENCY=pytest
FROM=>=9,<10
TO=>=9.1.1,<10

IMPLEMENTATION_COMMIT=98dcbeddabe880733c35f76a967021f93724f00c
PR=28
MERGE_COMMIT=cce10142c859e4b20fccc1aec16a342f054d6e73

PREMERGE_PUSH_CI_RUN=37684139764
PREMERGE_PUSH_CI=PASS
PREMERGE_PR_CI_RUN=37684216376
PREMERGE_PR_CI=PASS
POST_MERGE_CI_RUN=37684779206
POST_MERGE_CI=PASS
```

## Cierre de SUBTASK 8.1.4

La reconciliación de `flake8` se integró directamente mediante la PR Dependabot
`#20`, después de que su commit firmado quedara rebasado exactamente sobre el
`main` vigente y los gates protegidos finalizaran correctamente.

```text
SOURCE_PR=20
SOURCE_PR_RESOLUTION=MERGED_DIRECT
DEPENDENCY=flake8
FROM=>=7,<8
TO=>=7.4.1,<8

SOURCE_COMMIT=14e9b494ab0035242787d2f747014bedf34c6893
SOURCE_SIGNATURE=VERIFIED_VALID_BY_GITHUB
MERGE_COMMIT=b7d88f316339d6cb2478675ae27ad6e2f894d3a5

PREMERGE_PUSH_CI_RUN=37685065461
PREMERGE_PUSH_CI=PASS
PREMERGE_PR_CI_RUN=37685072512
PREMERGE_PR_CI=PASS
POST_MERGE_CI_RUN=37685685963
POST_MERGE_CI=PASS
```

La actualización de la dependencia no activa por sí sola el gate de Flake8. La
definición y aplicación del gate de calidad permanecen reservadas para SUBTASK
8.3.

## Cierre de SUBTASK 8.1.5

La reconciliación de `mypy` se integró directamente mediante la PR Dependabot
`#21`. Al tratarse de un salto mayor de 1.x a 2.x, se ejecutó además una
comparación diferencial sobre el mismo código con objetivo Python 3.10.

```text
SOURCE_PR=21
SOURCE_PR_RESOLUTION=MERGED_DIRECT
DEPENDENCY=mypy
FROM=>=1.19,<2
TO=>=2.4.0,<3

SOURCE_COMMIT=982f41b539182b9d2331d55e9f1d8d41e717a827
SOURCE_SIGNATURE=VERIFIED_VALID_BY_GITHUB
MERGE_COMMIT=550fd221cb4ff1c5435bc02b58bc2057f67b3cef

MYPY_BASELINE_VERSION=1.20.2
MYPY_TARGET_VERSION=2.4.0
MYPY_BASELINE_ERRORS=389
MYPY_TARGET_ERRORS=389
MYPY_NEW_ONLY_ERRORS=0
MYPY_DIFFERENTIAL=PASS

PREMERGE_PUSH_CI_RUN=37685959419
PREMERGE_PUSH_CI=PASS
PREMERGE_PR_CI_RUN=37685966937
PREMERGE_PR_CI=PASS
POST_MERGE_CI_RUN=37687530157
POST_MERGE_CI=PASS
```

Los 389 diagnósticos de tipado son deuda preexistente y no una regresión de Mypy
2.4.0. La definición del gate Mypy y el tratamiento de dicha deuda permanecen
reservados para SUBTASK 8.3.

## Cierre de SUBTASK 8.1.6

La reconciliación de `serde` y su transición a `syn` 3 se integró desde el
baseline vigente de TASK 8. La PR Dependabot original `#10` no fue fusionada:
quedó cerrada como supersedida por la PR `#29`.

```text
SOURCE_PR=10
SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
DEPENDENCY=serde
SERDE_FROM=1.0.228
SERDE_TO=1.0.229
SERDE_CORE_FROM=1.0.228
SERDE_CORE_TO=1.0.229
SERDE_DERIVE_FROM=1.0.228
SERDE_DERIVE_TO=1.0.229
SYN_FROM=2.0.117
SYN_TO=3.0.3

IMPLEMENTATION_COMMIT=3ad4deb55c8dbd2d972bde2a1f566d2e1988cf9f
IMPLEMENTATION_SIGNATURE=PASS_SSH_ED25519
PR=29
MERGE_COMMIT=8d848e1d8f8a97f71fdefe8b01cfbc23a007b5d3

LOCAL_CARGO_FMT=PASS
LOCAL_CARGO_CHECK=PASS
LOCAL_RUST_TESTS=30_PASS_0_FAIL
LOCAL_CARGO_CLIPPY=PASS

PREMERGE_PUSH_CI_RUN=37689226362
PREMERGE_PUSH_CI=PASS
PREMERGE_PR_CI_RUN=37689430822
PREMERGE_PR_CI=PASS
POST_MERGE_CI_RUN=37690025028
POST_MERGE_CI=PASS
```

## Cierre de SUBTASK 8.1.7

La reconciliación de `tokio` se integró desde el baseline vigente de TASK 8.
La PR Dependabot original `#18` no fue fusionada: quedó cerrada como
supersedida por la PR `#30`.

```text
SOURCE_PR=18
SOURCE_PR_RESOLUTION=SUPERSEDED_CLOSED_NOT_MERGED
DEPENDENCY=tokio
FROM=1.52.3
TO=1.53.1

IMPLEMENTATION_COMMIT=0c1c842b7fc6414e2c3f663a2b9a0e17ded1368d
IMPLEMENTATION_SIGNATURE=PASS_SSH_ED25519
TEST_CONTRACT_COMMIT=c13728a99bb883881ffeea5eff31d1b0565007a1
TEST_CONTRACT_SIGNATURE=PASS_SSH_ED25519
PR=30
MERGE_COMMIT=a8b0791fafb516ed8f167099e715be283e90e102

LOCAL_CARGO_FMT=PASS
LOCAL_CARGO_CHECK=PASS
LOCAL_RUST_TESTS=30_PASS_0_FAIL
LOCAL_RUST_RELEASE_TESTS=30_PASS_0_FAIL
LOCAL_CARGO_CLIPPY=PASS
LOCAL_RELEASE_BUILD=PASS
LOCAL_RUNTIME_STRESS_ITERATIONS=25
LOCAL_RUNTIME_STRESS=PASS

INITIAL_PREMERGE_FAILURE_CLASSIFICATION=STALE_EXACT_VERSION_TEST_ASSERTIONS
PYTHON_CONTRACT_TARGETED_TESTS=2_PASS
PYTHON_SUITE=531_PASS_2_SKIPPED
PYTHON_SUBTESTS=72_PASS
PYTHON_COVERAGE=83_PERCENT
PYTHON_RESOURCE_WARNINGS=6_DEFERRED_TO_8_2

PREMERGE_PUSH_CI_RUN=37692475263
PREMERGE_PUSH_CI=PASS
PREMERGE_PR_CI_RUN=37692480885
PREMERGE_PR_CI=PASS
POST_MERGE_CI_RUN=37695775245
POST_MERGE_CI=PASS
```

La actualización de Tokio preserva el pin exacto, las features contractuales,
el modelo de runtime, los límites de concurrencia y las rutas de cancelación.
Las advertencias de recursos SQLite observadas en la suite Python permanecen
asignadas a SUBTASK 8.2.

## Estado inicial de dependencias

```text
PR_9=SUPERSEDED_CLOSED
PR_10=SUPERSEDED_CLOSED
PR_14=SUPERSEDED_CLOSED
PR_15=SUPERSEDED_CLOSED
PR_18=SUPERSEDED_CLOSED
PR_19=IN_RECONCILIATION
PR_20=MERGED
PR_21=MERGED

DEPENDENCY_BACKLOG=OPEN
```

SUBTASK 8.1 queda formalmente autorizada para iniciar desde el `main` resultante
del cierre de SUBTASK 8.0. No se considera completada hasta que cada PR tenga
una resolución explícita y verificable.

## Gates históricos anteriores a la integración PR #37

```text
RESOURCE_WARNINGS=UNRESOLVED
TEST_BASELINE=NOT_RECONCILED
COVERAGE_BASELINE=NOT_RECONCILED
BLACK_GATE=NOT_IMPLEMENTED
FLAKE8_GATE=NOT_IMPLEMENTED
MYPY_GATE=NOT_IMPLEMENTED
CURRENT_STATE_DOCUMENTATION=NOT_RECONCILED
SERVICE_READINESS=NOT_REVALIDATED
FINAL_RC=NOT_BUILT
STABLE_GO_NO_GO=NOT_EXECUTED
```

Estos valores corresponden al diagnóstico histórico anterior a PR #37.
No representan el estado vigente; la consolidación verificable se
registra en la sección Stage G al final de este documento.

## Regla de publicación

No se publicará `v3.0.0` por el solo hecho de que el software ejecute
correctamente sus operaciones principales.

La versión estable requiere cierre verificable de dependencias, recursos,
pruebas, calidad, documentación, operación, seguridad, supply chain,
empaquetado, release candidate y aceptación integral.

## Alcance congelado hasta v3.0.0

No se incorporarán nuevas técnicas públicas de red durante TASK 8 salvo que una
corrección sea estrictamente necesaria para cumplir un contrato ya existente.

Las ampliaciones funcionales se planificarán después del cierre estable de
`v3.0.0`.

## TASK 8 consolidated productization gate (historical PR #37 preparation snapshot)

```text
CURRENT_ACTIVE_SOURCE_VERSION=3.0.0-rc.3
HISTORICAL_TASK_5_6_RC2_RECORDS=PRESERVED
SUBTASK_8_1_9=BASELINE_AUDIT_PASS_NEW_INTAKE_PENDING_TRIAGE
ORIGINAL_DEPENDABOT_PR_19=SUPERSEDED_CLOSED_NOT_MERGED
OPEN_DEPENDABOT_BACKLOG=5
PR31_POST_MERGE_MAIN=67b900b4c378d766b8829231b3e9e930baceac71
PR31_POST_MERGE_CI=37698558022_PASS
SQLITE_RESOURCE_TESTS=53_PASS_14_SUBTESTS
PYTEST_PY313_LOCAL=531_PASS_2_SKIPPED_72_SUBTESTS
COVERAGE_PY313_LOCAL=82_PERCENT
COVERAGE_CI_FLOOR=82_PERCENT_PROPOSED_PENDING_REMOTE
BLACK_LOCAL=PASS
FLAKE8_LOCAL=PASS
MYPY_FULL_SOURCE_LOCAL=PASS
TASK_6_SERVICE_RUNTIME_LOCAL=282_PASS
SYNTHETIC_SOAK_CI=NEW_GATE_PENDING_REMOTE
RC3_TAG=NOT_CREATED
RC3_GITHUB_RELEASE=NOT_PUBLISHED
ENTERPRISE_RC3_ACCEPTANCE=NOT_YET_CERTIFIED
STABLE_GO_NO_GO=NOT_AUTHORIZED
STABLE_RELEASE_PUBLICATION=NOT_AUTHORIZED
```

This block preserves the pre-PR37 source-preparation snapshot. Later
CI gates passed on PR #37 and merged main; separate RC3 publication
authorization is still required. Historical RC2 validators and governance
records retain their original frozen meaning.

## Post-baseline Dependabot intake (October 2026)

The GitHub read-only inventory identifies **5 newly open Dependabot PRs** after the signed TASK 8 dependency baseline. They are not silently included in the already-tested RC3 source and are not automatically closed, merged, or permanently deferred. Individual risk and release impact remain to be classified before stable GO/NO-GO.

| PR | Proposed dependency change | Decision |
| --- | --- | --- |
| #32 | build(deps): bump tokio from 1.53.1 to 1.53.2 in /rust-core | OPEN — requires classification |
| #33 | build(deps): bump wheel from 0.47.0 to 0.48.0 | OPEN — requires classification |
| #34 | build(deps-dev): bump setuptools from 83.0.0 to 84.0.0 | OPEN — requires classification |
| #35 | build(deps-dev): update black requirement from <27,>=25 to >=26.10.0,<27 | OPEN — requires classification |
| #36 | build(deps): bump build from 1.5.0 to 1.6.1 | OPEN — requires classification |

Security review requirement: PR #33 (wheel 0.47.0 → 0.48.0) includes the upstream `wheel convert` path-traversal fix tracked as `GHSA-vgq5-9859-3mmw`. Determine toolchain applicability and any vulnerability scanner findings; do not assert safety without evidence. The RC3 candidate may be prepared and tested in parallel, but no stable GO decision is permitted while this review is unresolved.

```text
POST_BASELINE_DEPENDABOT_OPEN_COUNT=5
POST_BASELINE_DEPENDABOT_OPEN_PRS=32,33,34,35,36
POST_BASELINE_DEPENDABOT_CLASSIFICATION=PENDING_SECURITY_AND_COMPATIBILITY_REVIEW
WHEEL_GHSA_VGQ5_9859_3MMW=REVIEW_REQUIRED
FINAL_STABLE_GO_NO_GO=BLOCKED_PENDING_RELEASE_EVIDENCE
```


## Stage G: reconciled PR37 integration and dependency security intake

The first consolidated productization PR #37 has been merged into `main`.
The statuses and measurements above include historical snapshots; the values
below are the latest evidence for the completed source integration. Nothing
in this section authorizes publication of RC3 or stable v3.0.0.

```text
TASK8_SOURCE_PR=37_MERGED
TASK8_SOURCE_IMPLEMENTATION_COMMIT=5eb2ebfaaa4f701871b787a1c1420863b03cb36c
TASK8_SOURCE_MAIN_MERGE_COMMIT=c27d13a0e7643f1ee6cc6fd4a20e3dce14643176
TASK8_SOURCE_PREMERGE_PUSH_CI=37788101220_PASS
TASK8_SOURCE_PREMERGE_PR_CI=37788678813_PASS
TASK8_SOURCE_POSTMERGE_MAIN_CI=37813550182_PASS_28_OF_28
TASK8_SOURCE_MAIN_GPG=VERIFIED_GITHUB_AND_LOCAL_KEY_FINGERPRINT
TASK8_SOURCE_MATRIX=UBUNTU_22_04_AND_24_04_PYTHON_3_10_TO_3_13_PASS
TASK8_SOURCE_PROVENANCE_VERIFY=PASS_POSTMERGE_PUSH
TASK8_SOURCE_COVERAGE=82_25_PERCENT
TASK8_SOURCE_PYTEST=534_PASS_2_SKIPPED_72_SUBTESTS
TASK8_SOURCE_RESOURCE=53_PASS_14_SUBTESTS
DEPENDENCY_RECONCILIATION_BRANCH=feat/task-8-rc3-security-dependency-reconciliation
DEPENDENCY_RECONCILIATION_BASE=c27d13a0e7643f1ee6cc6fd4a20e3dce14643176
DEPENDENCY_DIRECT_PROPOSALS=32,33,34,35,36
DEPENDENCY_RELEASE_LOCK_SHA256=c1daa8a206b5835db96b7188629f1e3f95405bd93f44f0c744bce60310035cc8
DEPENDENCY_RELEASE_LOCK_VERSION_DELTAS=22
DEPENDENCY_STAGE_D=LOCAL_SOURCE_AND_LOCK_STABLE_PASS
DEPENDENCY_STAGE_E=LOCAL_16_OF_16_GATES_PASS
DEPENDENCY_STAGE_F=PYTHON_RUST_GO_AUDITS_PASS
DEPENDENCY_STAGE_F_HASHED_INSTALL=PASS
DEPENDENCY_STAGE_F_PIP_CHECK=PASS
DEPENDENCY_STAGE_F_PIP_AUDIT=NO_KNOWN_VULNERABILITIES_FOUND
DEPENDENCY_STAGE_F_CARGO_AUDIT=PASS
DEPENDENCY_STAGE_F_GOVULNCHECK=NO_VULNERABILITIES_FOUND
DEPENDENCY_STAGE_F_BUILD_BACKEND_COMPATIBILITY=PASS
DEPENDENCY_RECONCILIATION_COMMIT=NOT_CREATED
DEPENDENCY_RECONCILIATION_REMOTE_CI=NOT_RUN
DEPENDENCY_RECONCILIATION_RELEASE_ARTIFACTS=NOT_REVALIDATED
DEPENDABOT_SOURCE_PRS=OPEN_PENDING_INDEPENDENT_SUPERSEDED_RESOLUTION
RC3_TAG=NOT_CREATED
RC3_RELEASE=NOT_PUBLISHED
STABLE_GO_NO_GO=NOT_AUTHORIZED
STABLE_PUBLICATION=NOT_AUTHORIZED
```

The regenerated Python lock contains 22 version changes, including major
`filelock` 3.32.2 to 4.0.12. Static audit and installation evidence do **not**
replace reproducible wheel/sdist verification and complete exact-commit CI.
Wheel 0.48.0 includes the upstream fix associated with
`GHSA-vgq5-9859-3mmw`; the repository text search found no direct invocation
of `wheel convert` in the inspected paths. That search does not establish
absence of indirect calls or eliminate the need for package verification.
Dependabot PRs #32–#36 remain open until each is resolved independently;
no original bot PR has been merged as part of this uncommitted reconciliation.

## Stage L — current evidence after signed dependency reconciliation (2026-10-08)

This is an **additive, post-Stage-G snapshot**. Historical Stage G `NOT_CREATED`,
`NOT_RUN` and other pending values above remain valid for their evidence cut-off.
They must not be interpreted as the current status of the repository.

```text
STAGE_L=DOCUMENTATION_PREPARATION_UNCOMMITTED
POST_BASELINE_DEPENDENCY_COMMIT=c0a1ace88cea37a4ad59303ff9d40c54b49b4788
POST_BASELINE_DEPENDENCY_PARENT=c27d13a0e7643f1ee6cc6fd4a20e3dce14643176
POST_BASELINE_DEPENDENCY_TREE=ed00bebc0ca4897f127a2e21ea7d1bcf681bbeaf
POST_BASELINE_DEPENDENCY_SIGNATURE=GITHUB_VERIFIED_VALID_SSH
POST_BASELINE_DEPENDENCY_RELEASE_LOCK_SHA256=c1daa8a206b5835db96b7188629f1e3f95405bd93f44f0c744bce60310035cc8
POST_BASELINE_RELEASE_LOCK_VERSION_CHANGES=22
STAGE_I_LOCAL_REPRODUCIBILITY=PASS_7_FILES
STAGE_I_LOCAL_WHEEL_SDIST_INSTALL_SMOKE=PASS
STAGE_I_LOCAL_SBOM_MANIFEST_HASHES=PASS
STAGE_I_EXACT_COMMIT_BINDING=PASS
STAGE_J_RECONCILIATION_PUSH_CI=37822525656_PASS_28_OF_28
STAGE_K_PERMANENT_BRANCH_FAST_FORWARD=PASS
STAGE_K_PERMANENT_PUSH_CI=37823691270_PASS_28_OF_28
STAGE_K_PERMANENT_REMOTE_HEAD=c0a1ace88cea37a4ad59303ff9d40c54b49b4788
STAGE_K_SECURITY_SOURCE_REMOTE_HEAD=c0a1ace88cea37a4ad59303ff9d40c54b49b4788
MAIN_LAST_VERIFIED=c27d13a0e7643f1ee6cc6fd4a20e3dce14643176
DEPENDABOT_PRS_32_TO_36=OPEN_NOT_MERGED_NOT_CLOSED
SUBTASK_8_7=SOURCE_TECHNICAL_GATES_PASS_FINAL_ACCEPTANCE_PENDING
SUBTASK_8_8=BLOCKED_NO_FORMAL_GO_NO_GO
SUBTASK_8_9=BLOCKED_NO_PUBLICATION
RC3_TAG=NOT_CREATED
RC3_PUBLICATION=NOT_AUTHORIZED
STABLE_PUBLICATION=NOT_AUTHORIZED
```

The post-baseline dependency commit is **not integrated in `main`**. The two
successful branch `push` workflows are not substitutes for future pull-request
checks, a protected merge, exact `main` post-merge CI, and a final human decision.
The proposed second consolidated PR must not record stable GO before the backlog,
release acceptance and post-merge gates are actually satisfied.

## Stage R — Current post-Stage-Q evidence snapshot (2026-10-08)

This section is an additive current-state record. Prior Stage G and
Stage L snapshots retain their original evidence cut-offs.

The consolidated dependency and acceptance PR #38 was merged into
`main` as signed merge commit
`b57a3f011f88fe917323a2eb8c9d12c7fcedaeee`.
GitHub verified the signature as valid.

Its parents are:
- `c27d13a0e7643f1ee6cc6fd4a20e3dce14643176`;
- `36d28a69bf4e90c2f23b48da2e9864c784e63123`.

The postmerge `main` workflow
[37850121564](https://github.com/Averlyth/cicadaport/actions/runs/37850121564)
completed with 28 of 28 successful jobs, including the
push-only release-artifact provenance verification.

Stage Q administratively resolved original Dependabot PRs
#32, #33, #34, #35 and #36 as superseded.
All five are CLOSED, none was individually merged, and the
five original branch references were verified at their original SHAs.
Dependabot's automatic branch deletions were repaired without
moving `main`, rewriting history, or changing application code.

The architect subsequently approved and froze Stage Q.

```text
STAGE_O=COMPLETED_VERIFIED
STAGE_P=COMPLETED_AUDITED_RESOLUTION_PREPARED
STAGE_Q=COMPLETED_CONSOLIDATED_CLOSED_FROZEN
STAGE_Q_DEPENDABOT_CLOSED=5_OF_5
STAGE_Q_DEPENDABOT_BRANCHES_PRESERVED=5_OF_5

MAIN=b57a3f011f88fe917323a2eb8c9d12c7fcedaeee
MAIN_MERGE_SIGNATURE=GITHUB_VERIFIED_VALID
MAIN_POSTMERGE_CI=37850121564_PASS_28_OF_28

SUBTASK_8_7=FINAL_ACCEPTANCE_PENDING
SUBTASK_8_8=BLOCKED
SUBTASK_8_9=BLOCKED
RC3_TAG=NOT_CREATED
RC3_PUBLICATION=NOT_AUTHORIZED
STABLE_RELEASE=NO_GO
```

The native GitHub Dependabot alerts and secret-scanning alert
features returned disabled errors; the code-scanning API returned
`no analysis found`. These are inventory limitations, not proof
of zero vulnerabilities or zero residual blockers.

The passing CI includes dependency audits, SAST, Gitleaks,
reproducibility, installation, SBOM, provenance, attestations,
operational acceptance and ten synthetic bounded-resource soak
iterations. The synthetic soak must not be called a
production-duration endurance test.

The current security and release documentation must be
reconciled through a separately validated protected PR.
This snapshot does not pre-authorize a release or stable GO.
