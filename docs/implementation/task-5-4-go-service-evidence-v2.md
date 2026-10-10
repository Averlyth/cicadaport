# SUBTASK 5.4 — Go Service Evidence Engine v2

```text
CONTRACT=GSEV2-CICADAPORT-5.4-001
VERSION=1.0-CANDIDATE
BASE=7bac7fff3c2f0e14db74505923e0e5f64edc7eb7
PUBLIC_CONTRACT_VERSION=1
SERVICE_EVIDENCE_CONTRACT_VERSION=2
NETWORK_TECHNIQUE=TCP_CONNECT_AND_SAFE_BANNER_EVIDENCE
VULNERABILITY_DETECTION=NOT_IMPLEMENTED
```

## Arquitectura de compatibilidad

`banner_request` y `banner_result` permanecen exactamente en versión 1 y stdout
continúa reservado a un registro público por puerto. La evidencia ampliada v2 no
se inyecta en esos objetos: se emite, cuando el orquestador proporciona el
descriptor heredado `CICADAPORT_SERVICE_EVIDENCE_FD`, por un canal JSONL
independiente. La ausencia del descriptor conserva el comportamiento público
anterior.

## Streaming y recursos

El motor deja de acumular y ordenar todos los resultados antes de stdout. Cada
worker entrega un resultado al concluir el endpoint; el consumidor lo codifica
de inmediato. La cola de puertos y la cola de resultados están acotadas al menor
valor entre la concurrencia efectiva y 32. El orden de finalización no forma
parte del contrato; el orden de presentación final corresponde al orquestador.

Un error del consumidor cancela el contexto compartido. Las conexiones activas
se cierran al cancelar, los productores dejan de admitir trabajo y los canales
se drenan hasta finalizar sin goroutines huérfanas.

## Timeouts por fase

La solicitud pública v1 conserva `timeout_ms`. El adaptador interno lo proyecta
sin reinterpretar el contrato a seis presupuestos explícitos:

- conexión;
- negociación TLS;
- escritura;
- primer byte;
- lectura ociosa;
- duración total del probe.

La duración total limita todas las fases. La evidencia registra la fase de
fallo y si ya se habían observado bytes parciales.

## Lectura y sanitización

La lectura es incremental en bloques de 512 bytes y conserva como máximo 4.096
bytes. Finaliza por terminador versionado, EOF, timeout ocioso o truncamiento.
Cada evidencia incluye longitud observada, longitud capturada, indicador de
truncamiento, codificación y SHA-256 del contenido capturado.

`banner_display` se construye desde UTF-8 válido y elimina NUL, C0/C1, ESC,
secuencias CSI/OSC, DEL, controles bidi e invisibles peligrosos. CR, LF y TAB se
normalizan a espacios. Los bytes crudos no se imprimen directamente.

## Evidencia TLS veraz

La implementación actual del motor Go ejecuta una negociación TLS autenticada. `crypto/tls` comprueba la cadena X.509, vigencia y nombre del objetivo usando las raíces del sistema, con TLS 1.2 como mínimo. Un certificado autofirmado no confiable, caducado, desconocido o con nombre incorrecto provoca fallo cerrado antes de enviar el probe y no permite capturar un banner.

La evidencia distingue negociación, presencia y verificación; `certificate_verified=true` exige una cadena verificada. Se preservan versión, suite, ALPN, sujeto, emisor, SAN, vigencia, SHA-256 y longitud de cadena cuando la negociación es válida. La modificación está incorporada en PR #46, firmada, con CI protegido y CodeQL posmerge correctos sobre 62fa8c3a7e1b0d8e6002a302f19b6484ea0d75c1.

El diseño de observación TLS no autenticada pertenece a los registros históricos de TASK 5.4 y 8.7; no representa el comportamiento Go vigente.

## Registro de probes

La primera versión incluye únicamente:

- `passive-banner@1`, sin payload;
- `http-head@1`, probe seguro HEAD para los puertos HTTP ya admitidos.

Ambos declaran transporte, hash del payload, límite de lectura, terminadores,
nivel de invasividad, política predeterminada y parser. No existen probes
`active` o `restricted` habilitados por defecto.

## Límites preservados

- no se modifica `rust-core/`;
- no se modifica Session Store v2;
- no se modifica ningún contrato público v1;
- no se añaden detección de vulnerabilidades, explotación ni probes externos;
- las pruebas materiales usan exclusivamente loopback.
