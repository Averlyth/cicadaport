# Estado formal de TASK 8

```text
PROJECT=CICADAPORT
ORGANIZATION=AVERLYTH

TASK_8=MVP_3_0_0_PRODUCTIZATION_AND_STABLE_RELEASE
TASK_8_STATUS=AUTHORIZED_IN_IMPLEMENTATION

TASK_8_CONTRACT=SRP-CICADAPORT-TASK-8-001
TASK_8_CONTRACT_VERSION=1.0-CANDIDATE

TASK_8_BASE=b1c963f93cb21a2e3b06900451d96e5df752f0b3
TASK_8_BRANCH=feat/task-8-mvp-3-stable-productization

CURRENT_SOURCE_VERSION=3.0.0-rc.2
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

SUBTASK_8_1=IN_IMPLEMENTATION
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

SUBTASK_8_1_3=IN_IMPLEMENTATION
SUBTASK_8_1_3_TARGET_PR=15
SUBTASK_8_1_3_DEPENDENCY=pytest
SUBTASK_8_1_3_FROM=>=9,<10
SUBTASK_8_1_3_TO=>=9.1.1,<10

SUBTASK_8_2=BLOCKED_BY_8_1
SUBTASK_8_3=BLOCKED
SUBTASK_8_4=BLOCKED
SUBTASK_8_5=BLOCKED
SUBTASK_8_6=BLOCKED
SUBTASK_8_7=BLOCKED
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

## Estado inicial de dependencias

```text
PR_9=SUPERSEDED_CLOSED
PR_10=OPEN
PR_14=SUPERSEDED_CLOSED
PR_15=IN_RECONCILIATION
PR_18=OPEN
PR_19=OPEN
PR_20=OPEN
PR_21=OPEN

DEPENDENCY_BACKLOG=OPEN
```

SUBTASK 8.1 queda formalmente autorizada para iniciar desde el `main` resultante
del cierre de SUBTASK 8.0. No se considera completada hasta que cada PR tenga
una resolución explícita y verificable.

## Gates actualmente pendientes

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

Estos valores describen trabajo pendiente; no implican necesariamente un fallo
funcional del producto.

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
