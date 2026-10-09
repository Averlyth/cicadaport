#!/usr/bin/env python3
"""Generate a deterministic CycloneDX 1.6 SBOM for the release artifact set."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
from email.parser import Parser
import json
from pathlib import Path
import re
import subprocess
import sys

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 tests
    import tomli as tomllib
import uuid
from zipfile import ZipFile

from packaging.requirements import Requirement

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

LOCK = ROOT / "requirements-release.txt"
PYPROJECT = ROOT / "pyproject.toml"
CARGO_LOCK = ROOT / "rust-core" / "Cargo.lock"
GO_MOD = ROOT / "go-banner" / "go.mod"


def git(*arguments: str) -> str:
    return subprocess.check_output(["git", *arguments], cwd=ROOT, text=True).strip()


def source_timestamp() -> str:
    epoch = int(git("show", "-s", "--format=%ct", "HEAD"))
    return (
        datetime.fromtimestamp(epoch, timezone.utc).isoformat().replace("+00:00", "Z")
    )


def normalize_name(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def python_components() -> list[dict]:
    text = LOCK.read_text(encoding="utf-8")
    components: list[dict] = []
    current: dict | None = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("--"):
            continue
        match = re.match(r"^([A-Za-z0-9_.-]+)==([^\\\s]+)", line)
        if match:
            name, version = match.groups()
            current = {
                "type": "library",
                "name": normalize_name(name),
                "version": version,
                "bom-ref": f"pkg:pypi/{normalize_name(name)}@{version}",
                "purl": f"pkg:pypi/{normalize_name(name)}@{version}",
                "hashes": [],
                "properties": [{"name": "cicadaport:ecosystem", "value": "python"}],
            }
            components.append(current)
        if current is not None:
            for digest in re.findall(r"--hash=sha256:([0-9a-f]{64})", line):
                current["hashes"].append({"alg": "SHA-256", "content": digest})
    for component in components:
        component["hashes"] = sorted(
            component["hashes"], key=lambda item: item["content"]
        )
    return components


def runtime_components_from_wheel(wheel: Path) -> list[dict]:
    """Direct runtime requirements; do not invent installed versions."""
    with ZipFile(wheel) as archive:
        metadata_paths = [
            name for name in archive.namelist() if name.endswith(".dist-info/METADATA")
        ]
        if len(metadata_paths) != 1:
            raise ValueError("Expected exactly one wheel METADATA")
        metadata = Parser().parsestr(archive.read(metadata_paths[0]).decode("utf-8"))
    from_wheel = sorted(
        str(Requirement(value)) for value in metadata.get_all("Requires-Dist", [])
    )
    project = tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))
    # Bind declarations to the actual distribution, not merely its requirements.
    from src.version import __version__ as expected_version

    metadata_names = metadata.get_all("Name", [])
    metadata_versions = metadata.get_all("Version", [])
    expected_name = normalize_name(project["project"]["name"])
    actual_name = (
        normalize_name(metadata_names[0]) if len(metadata_names) == 1 else None
    )
    if (
        len(metadata_names) != 1
        or len(metadata_versions) != 1
        or actual_name != expected_name
        or metadata_versions[0] != expected_version
    ):
        raise ValueError("Wheel distribution identity mismatch project metadata")
    from_project = sorted(
        str(Requirement(value)) for value in project["project"].get("dependencies", [])
    )
    if not from_wheel or from_wheel != from_project:
        raise ValueError("Wheel runtime requirements mismatch project metadata")
    components: list[dict] = []
    for requirement in from_wheel:
        parsed = Requirement(requirement)
        if parsed.url:
            raise ValueError("Direct-URL runtime requirement not supported")
        name = normalize_name(parsed.name)
        fingerprint = hashlib.sha256(requirement.encode()).hexdigest()[:16]
        components.append(
            {
                "type": "library",
                "name": name,
                "bom-ref": f"runtime-declaration:{name}:{fingerprint}",
                "purl": f"pkg:pypi/{name}",
                "properties": [
                    {"name": "cicadaport:role", "value": "runtime-declared"},
                    {"name": "cicadaport:requirement", "value": requirement},
                    {"name": "cicadaport:version-resolution", "value": "unresolved"},
                ],
            }
        )
    return components


def rust_components() -> list[dict]:
    payload = tomllib.loads(CARGO_LOCK.read_text(encoding="utf-8"))
    components = []
    for package in payload.get("package", []):
        name = package["name"]
        version = package["version"]
        component = {
            "type": "library" if name != "rust-core" else "application",
            "name": name,
            "version": version,
            "bom-ref": f"pkg:cargo/{name}@{version}",
            "purl": f"pkg:cargo/{name}@{version}",
            "properties": [{"name": "cicadaport:ecosystem", "value": "cargo"}],
        }
        checksum = package.get("checksum")
        if checksum:
            component["hashes"] = [{"alg": "SHA-256", "content": checksum}]
        components.append(component)
    return components


def go_components() -> list[dict]:
    module = "go-banner"
    for line in GO_MOD.read_text(encoding="utf-8").splitlines():
        if line.startswith("module "):
            module = line.split(maxsplit=1)[1]
            break
    return [
        {
            "type": "application",
            "name": module,
            "version": "1.0.0-internal",
            "bom-ref": f"pkg:golang/{module}@1.0.0-internal",
            "purl": f"pkg:golang/{module}@1.0.0-internal",
            "properties": [{"name": "cicadaport:ecosystem", "value": "go"}],
        }
    ]


def main() -> None:
    from src.version import SEMVER_VERSION, __version__

    if len(sys.argv) != 3:
        raise SystemExit("Usage: generate_cyclonedx_sbom.py OUTPUT WHEEL")
    output = Path(sys.argv[1])
    wheel = Path(sys.argv[2])
    commit = git("rev-parse", "HEAD")
    candidate_tree = git("write-tree")
    runtime = runtime_components_from_wheel(wheel)
    components = python_components() + rust_components() + go_components() + runtime
    components.sort(
        key=lambda item: (item["purl"], item["name"], item.get("version", ""))
    )
    application_ref = f"pkg:pypi/portscanner-pro@{__version__}?commit={commit}"
    namespace = uuid.UUID("ea7dd7e2-c7e2-5d5c-90e8-70fb6ad604f0")
    serial = uuid.uuid5(
        namespace,
        commit
        + "\n"
        + candidate_tree
        + "\n"
        + "\n".join(item["purl"] for item in components),
    )
    document = {
        "$schema": "https://cyclonedx.org/schema/bom-1.6.schema.json",
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{serial}",
        "version": 1,
        "metadata": {
            "timestamp": source_timestamp(),
            "component": {
                "type": "application",
                "name": "CicadaPort",
                "version": SEMVER_VERSION,
                "bom-ref": application_ref,
                "purl": f"pkg:pypi/portscanner-pro@{__version__}",
                "properties": [
                    {"name": "cicadaport:git-commit", "value": commit},
                    {"name": "cicadaport:git-candidate-tree", "value": candidate_tree},
                    {
                        "name": "cicadaport:contract",
                        "value": "EIVRC-CICADAPORT-5.6-001",
                    },
                    {
                        "name": "cicadaport:runtime-coverage",
                        "value": "direct-declarations-only-transitives-unresolved",
                    },
                ],
            },
            "tools": {
                "components": [
                    {
                        "type": "application",
                        "name": "cicadaport-cyclonedx-generator",
                        "version": "1",
                    }
                ]
            },
        },
        "components": components,
        "dependencies": [
            {
                "ref": application_ref,
                "dependsOn": sorted(item["bom-ref"] for item in runtime),
            }
        ],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    print(f"CYCLONEDX_SBOM={output}")
    print(f"CYCLONEDX_SBOM_SHA256={digest}")


if __name__ == "__main__":
    main()
