# Security Policy

CicadaPort is a security-engineering and TCP reconnaissance platform intended exclusively for systems, networks, laboratories, and environments that the operator owns or is explicitly authorized to assess.

Every expanded target, IP address, hostname, range, CIDR entry, and target-file record must remain within the authorized assessment scope.

## Supported Versions

The source tree currently identifies CicadaPort as `3.0.0-rc.3` (`3.0.0rc3` in Python package metadata).

`3.0.0-rc.3` is a source-level release candidate and is not currently a published GitHub Release.

The latest published prerelease is `v3.0.0-rc.1`.

| Reference | Security state | Distribution state |
| --- | --- | --- |
| `main` | Current development | Source repository |
| `3.0.0-rc.3` | Current release candidate | Not published |
| `v3.0.0-rc.1` | Latest published prerelease | Published |
| Earlier or unmaintained versions | Not maintained | Unsupported |

The currently verified support matrix is limited to:

- Linux x86_64;
- Ubuntu 22.04;
- Ubuntu 24.04;
- Python 3.10 through 3.13;
- Rust 1.97.1;
- Go 1.26.9.

Windows, macOS, ARM64, and Python 3.14 are not currently part of the verified support matrix.

Successful execution on an unvalidated environment does not automatically extend the supported-platform declaration.

## Reporting a Vulnerability

Do not disclose suspected vulnerabilities through a public issue, discussion, pull request, repository, or public proof of concept.

Use GitHub private vulnerability reporting when it is available for the repository.

A useful report should include, where applicable:

- the affected commit, version, or release;
- the affected component;
- a concise technical description;
- the security impact;
- authorized reproduction steps;
- sanitized logs or evidence;
- a sanitized proof of concept when required to demonstrate the issue;
- relevant environmental information.

Do not include real credentials, secrets, access tokens, private keys, personal data, or unauthorized third-party information.

If private vulnerability reporting is unavailable, open a public issue requesting a private communication channel **without including vulnerability details**.

## Security Scope

Security reports concerning CicadaPort may include issues affecting:

- Python orchestration and input validation;
- Rust TCP engine behavior;
- Go service-evidence processing;
- native JSONL contract validation;
- session persistence and recovery;
- report and artifact generation;
- unsafe filesystem behavior;
- privilege or permission boundaries;
- dependency or supply-chain integrity;
- CI and release-security controls;
- terminal or output sanitization;
- unintended expansion of network behavior;
- security-relevant failures of documented isolation or validation guarantees.

## Out of Scope

The following are outside the intended security-reporting scope unless they directly demonstrate a vulnerability in CicadaPort itself:

- unauthorized scanning of third-party infrastructure;
- social engineering;
- denial-of-service activity against third parties;
- destructive testing;
- vulnerabilities in unrelated external systems;
- dependency-version reports without demonstrated reachable impact;
- unsupported environments where the issue cannot be reproduced within the supported matrix;
- requests to add offensive capabilities that are intentionally outside the CicadaPort security model.

## TLS Observation Trust Boundary

CicadaPort's Go banner engine may intentionally negotiate TLS with an unknown,
self-signed, expired or otherwise untrusted certificate **only for authorized
service observation**. Such a connection does not authenticate the endpoint:
`certificate_verified=false` and
`verification_not_performed_observation_mode` must remain explicit in evidence.
Service banners and headers from this connection are untrusted observations,
not proof of the endpoint's identity, legitimacy or certificate validity.

TLS observation is restricted at runtime to a passive read or the fixed,
credential-free `HEAD / HTTP/1.0` probe; it rejects modified request payloads
and unapproved probe descriptors before opening the connection. No passwords,
API tokens, cookies, authenticated HTTP requests or privileged actions are
permitted through this transport. TLS 1.2 is the minimum negotiated version.
Do not reuse this intentionally unauthenticated TLS configuration for ordinary
HTTP clients, software updates, authenticated API calls or release operations.

The use of `InsecureSkipVerify` in this narrowly bounded observation path
remains a **real identity-authentication limitation** and is not categorized as
a CodeQL false positive. The CodeQL finding `go/disabled-certificate-check`
requires a separately recorded, explicit architect risk decision; tests and
these restrictions do not establish authenticated transport or eliminate
active network-interception risks.

## Operational Boundaries

CicadaPort does not currently expose the following capabilities through its supported public reconnaissance workflow:

- raw-socket scanning;
- SYN scanning;
- UDP scanning;
- unrestricted host discovery;
- vulnerability exploitation;
- destructive operations;
- arbitrary offensive scripting.

Changes that introduce or expand security-sensitive network behavior require explicit review, testing, documentation, and governance approval.

## Responsible Disclosure

Do not perform testing that exceeds the authorization granted for the affected environment.

Public disclosure should occur only after the issue has been responsibly assessed and an appropriate remediation or disclosure process has been established.

## Repository Ownership

CicadaPort is maintained by **Averlyth** as part of the **Obscuryx Security Platform**.

Repository:

[github.com/Averlyth/cicadaport](https://github.com/Averlyth/cicadaport)
