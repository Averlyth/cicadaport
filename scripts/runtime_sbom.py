#!/usr/bin/env python3
"""CicadaPort G7: wheel-bound, installed, versioned runtime dependency closure.

The lock of release/audit tools is NOT the runtime dependency graph.
Snapshots deliberately omit installation timestamps, temporary paths and index URLs.
One published SBOM represents the build runner cell; each installed-artifact job
independently verifies its own Python/Ubuntu cell without claiming version parity.
"""
from __future__ import annotations

from collections import defaultdict, deque
from email.parser import Parser
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile
from zipfile import ZipFile

try:
    from packaging.markers import default_environment
    from packaging.requirements import Requirement
    from packaging.utils import canonicalize_name
    from packaging.version import Version
except ModuleNotFoundError:  # setup-python matrix hosts only guarantee pip
    from pip._vendor.packaging.markers import default_environment
    from pip._vendor.packaging.requirements import Requirement
    from pip._vendor.packaging.utils import canonicalize_name
    from pip._vendor.packaging.version import Version

SCHEMA = "cicadaport-runtime-resolution-v1"
COVERAGE = "resolved-transitive-installed-build-cell"
SHA = re.compile(r"[0-9a-f]{64}\Z")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def wheel_metadata(wheel: Path) -> dict:
    with ZipFile(wheel) as archive:
        names = [n for n in archive.namelist() if n.endswith(".dist-info/METADATA")]
        require(len(names) == 1, "wheel must contain exactly one METADATA")
        metadata = Parser().parsestr(archive.read(names[0]).decode("utf-8"))
    name, version = metadata.get("Name"), metadata.get("Version")
    require(name is not None and version is not None, "wheel identity missing")
    require(canonicalize_name(name) == "portscanner-pro", "wrong distribution name")
    require(Version(version) == Version("3.0.0"), "wrong distribution version")
    return {"name": canonicalize_name(name), "version": version,
            "requires_dist": sorted(metadata.get_all("Requires-Dist", []))}


def marker_environment() -> dict:
    # These stable PEP 508 fields are sufficient to evaluate every declared marker.
    # Compare with the pip-inspect environment in capture mode.
    e = default_environment()
    return {key: e[key] for key in sorted(e)}


def _validate_node(record: dict) -> dict:
    require(isinstance(record, dict), "installed record not an object")
    name = record.get("name")
    version = record.get("version")
    requires = record.get("requires_dist", [])
    require(isinstance(name, str) and name and
            canonicalize_name(name) == name, "noncanonical node name")
    require(isinstance(version, str) and version and
            str(Version(version)) == version, "noncanonical node version")
    require(isinstance(requires, list) and all(isinstance(v, str) for v in requires)
            and requires == sorted(set(requires)), "invalid node requirements")
    for raw in requires:
        req = Requirement(raw)
        require(req.url is None, "direct URL runtime dependency prohibited")
    hash_value = record.get("sha256")
    require(isinstance(hash_value, str) and SHA.fullmatch(hash_value) is not None,
            "missing sha256 from recorded wheel or pip install report")
    return record


def resolve(wheel: Path, records: list[dict], environment: dict) -> tuple[list[dict], list[dict]]:
    """Reconstruct full reachable PEP 508 graph, including propagated extras."""
    root = wheel_metadata(wheel)
    require(isinstance(environment, dict), "missing marker environment")
    for key in default_environment():
        require(isinstance(environment.get(key), str), "marker environment incomplete: " + key)
    require(isinstance(records, list) and records, "no installed distributions")
    by_name: dict[str, dict] = {}
    for raw in records:
        node = _validate_node(raw)
        require(node["name"] not in by_name, "duplicated installed project: " + node["name"])
        by_name[node["name"]] = node
    require(root["name"] in by_name, "installed application is missing")
    installed_root = by_name[root["name"]]
    require(installed_root["version"] == root["version"] and
            installed_root["requires_dist"] == root["requires_dist"],
            "installed application differs from exact wheel METADATA")
    require(installed_root["sha256"] == digest(wheel), "application wheel hash mismatch")
    found: set[str] = set()
    edges: dict[str, set[str]] = defaultdict(set)
    visited: set[tuple[str, tuple[str, ...]]] = set()
    queue = deque([(root["name"], tuple())])
    while queue:
        name, extras = queue.popleft()
        key = (name, extras)
        if key in visited:
            continue
        visited.add(key)
        node = by_name[name]
        found.add(name)
        edges.setdefault(name, set())
        for raw in node["requires_dist"]:
            requirement = Requirement(raw)
            applicable = requirement.marker is None or any(
                requirement.marker.evaluate({**environment, "extra": e})
                for e in ("", *extras)
            )
            if not applicable:
                continue
            target = canonicalize_name(requirement.name)
            require(target in by_name, "missing transitive distribution: " + target)
            installed = by_name[target]
            require(Version(installed["version"]) in requirement.specifier,
                    "unsatisfied dependency: " + str(requirement))
            edges[name].add(target)
            next_extras = tuple(sorted(requirement.extras))
            queue.append((target, next_extras))
    require(found == set(by_name), "unreachable or build-tool packages in runtime closure")
    nodes = sorted((by_name[n] for n in found), key=lambda x: x["name"])
    links = [{"name": n, "depends_on": sorted(edges[n])} for n in sorted(found)]
    return nodes, links


def validated_snapshot(wheel: Path, data: dict) -> tuple[list[dict], list[dict]]:
    require(isinstance(data, dict) and set(data) ==
            {"schema", "wheel_sha256", "environment", "os_release", "nodes", "edges"},
            "unexpected snapshot schema")
    require(data["schema"] == SCHEMA and data["wheel_sha256"] == digest(wheel),
            "wrong snapshot schema or wheel SHA")
    require(isinstance(data["os_release"], str) and
            re.fullmatch(r"[a-z0-9_.-]{1,50}", data["os_release"]) is not None,
            "invalid OS release")
    nodes, edges = resolve(wheel, data["nodes"], data["environment"])
    require(nodes == data["nodes"] and edges == data["edges"],
            "snapshot contains missing, orphan or altered dependency graph")
    return nodes, edges


def installed_snapshot(wheel: Path, pip_inspect: dict, reports: list[dict]) -> tuple[list[dict], list[dict]]:
    require(isinstance(pip_inspect, dict) and pip_inspect.get("version") == "1",
            "pip inspect JSON schema unsupported")
    require(isinstance(pip_inspect.get("installed"), list), "pip inspect installed missing")
    metadata = wheel_metadata(wheel)
    target = metadata["name"]
    installed = {}
    for item in pip_inspect["installed"]:
        meta = item.get("metadata", {})
        raw_name = meta.get("name")
        if not isinstance(raw_name, str):
            continue
        name = canonicalize_name(raw_name)
        require(name not in installed, "duplicate installed project")
        installed[name] = {
            "name": name, "version": str(Version(str(meta.get("version")))),
            "requires_dist": sorted(set(meta.get("requires_dist") or [])),
        }
    # Bind each hash to the *installed* distribution identity, not just its
    # normalized name. pip report alone is not a trusted inventory of versions.
    require(isinstance(reports, list) and reports, "pip install report is empty")
    hashes = {target: digest(wheel)}
    seen_report: set[str] = set()
    for item in reports:
        require(isinstance(item, dict), "malformed pip install report entry")
        meta = item.get("metadata", {})
        require(isinstance(meta, dict), "missing pip report metadata")
        raw_name = meta.get("name")
        raw_version = meta.get("version")
        require(isinstance(raw_name, str) and raw_name and
                isinstance(raw_version, str) and raw_version,
                "pip report missing distribution name/version")
        name = canonicalize_name(raw_name)
        require(name in installed, "pip report distribution not installed: " + name)
        require(name not in seen_report, "duplicate pip report distribution: " + name)
        require(Version(raw_version) == Version(installed[name]["version"]),
                "pip report/inspect version mismatch: " + name)
        seen_report.add(name)
        if name != target:
            info = item.get("download_info") or {}
            archives = (info.get("archive_info") or {}).get("hashes") or {}
            value = archives.get("sha256")
            require(isinstance(value, str) and SHA.fullmatch(value) is not None,
                    "pip download report lacks sha256: " + name)
            hashes[name] = value
    require(target in seen_report, "application wheel missing from pip report")
    # Traverse installed metadata first; do not demand hashes for bootstrap pip.
    universe = []
    for name, item in sorted(installed.items()):
        universe.append({**item, "sha256": hashes.get(name, "0" * 64)})
    e = pip_inspect.get("environment", {})
    for key, val in marker_environment().items():
        require(e.get(key) == val, "pip environment disagrees with runtime: " + key)
    # Reachability graph ignores pip, setuptools and other bootstrap packages.
    by_name = {node["name"]: node for node in universe}
    seen = {target}
    queue = deque([(target, tuple())])
    visited = set()
    deps: dict[str, set[str]] = defaultdict(set)
    while queue:
        name, extras = queue.popleft()
        if (name, extras) in visited:
            continue
        visited.add((name, extras))
        require(name in by_name, "runtime dependency not installed: " + name)
        for raw in by_name[name]["requires_dist"]:
            req = Requirement(raw)
            require(req.url is None, "direct URL dependency prohibited")
            if req.marker is not None and not any(
                req.marker.evaluate({**e, "extra": x}) for x in ("", *extras)
            ):
                continue
            child = canonicalize_name(req.name)
            require(child in by_name, "missing runtime dependency: " + child)
            seen.add(child)
            deps[name].add(child)
            queue.append((child, tuple(sorted(req.extras))))
    result_nodes = sorted((by_name[n] for n in seen), key=lambda item: item["name"])
    for n in result_nodes:
        require(n["name"] in hashes, "installed runtime lacks recorded archive SHA: " + n["name"])
    return result_nodes, [{"name": n, "depends_on": sorted(deps[n])}
                          for n in sorted(seen)]


def capture(wheel: Path, output: Path) -> None:
    require(wheel.is_file(), "wheel missing")
    with tempfile.TemporaryDirectory(prefix="cicadaport-g7-runtime-") as tmp:
        root = Path(tmp)
        env = root / "venv"
        subprocess.run([sys.executable, "-m", "venv", str(env)], check=True,
                       stdout=subprocess.DEVNULL)
        py = env / "bin" / "python"
        report = root / "install-report.json"
        subprocess.run([str(py), "-m", "pip", "install", "--no-cache-dir", "--disable-pip-version-check",
                        "--report", str(report), str(wheel.resolve())],
                       check=True, stdout=subprocess.DEVNULL)
        subprocess.run([str(py), "-m", "pip", "check"], check=True,
                       stdout=subprocess.DEVNULL)
        inspected = json.loads(subprocess.check_output(
            [str(py), "-m", "pip", "inspect", "--local"], text=True))
        report_data = json.loads(report.read_text("utf-8"))
        nodes, edges = installed_snapshot(wheel, inspected, report_data["install"])
    env = marker_environment()
    data = {"schema": SCHEMA, "wheel_sha256": digest(wheel),
            "environment": env, "os_release": read_os_release(),
            "nodes": nodes, "edges": edges}
    validated_snapshot(wheel, data)
    output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("G7_RUNTIME_SNAPSHOT=PASS_INSTALLED_TRANSITIVE_CLOSURE")
    print("G7_RUNTIME_NODES=" + str(len(nodes) - 1))


def read_os_release() -> str:
    text = Path("/etc/os-release").read_text("utf-8")
    match = re.search(r'^ID="?([a-zA-Z0-9_.-]+)"?$', text, re.M)
    return match.group(1).lower() if match else "unknown"


def inspect_existing(python: Path) -> dict:
    return json.loads(subprocess.check_output(
        [str(python), "-m", "pip", "inspect", "--local"], text=True))


def verify_installed(python: Path, wheel: Path, sbom: Path) -> None:
    subprocess.run([str(python), "-m", "pip", "check"], check=True,
                   stdout=subprocess.DEVNULL)
    inspected = inspect_existing(python)
    # Hashes were authenticated at build time; this job independently reconstructs
    # the installed reachability graph; no invented pin parity across Python minors.
    universe = []
    for item in inspected["installed"]:
        meta = item.get("metadata", {})
        if isinstance(meta.get("name"), str):
            universe.append({"name": canonicalize_name(meta["name"]),
                             "version": str(Version(str(meta["version"]))),
                             "requires_dist": sorted(set(meta.get("requires_dist") or [])),
                             "sha256": digest(wheel) if canonicalize_name(meta["name"]) == "portscanner-pro"
                             else "0" * 64})
    env = inspected["environment"]
    graph_root = wheel_metadata(wheel)
    by_name = {n["name"]: n for n in universe}
    seen = {graph_root["name"]}
    pending = deque([(graph_root["name"], tuple())])
    visited = set()
    while pending:
        name, extras = pending.popleft()
        if (name, extras) in visited:
            continue
        visited.add((name, extras))
        require(name in by_name, "matrix runtime missing distribution: " + name)
        for raw in by_name[name]["requires_dist"]:
            req = Requirement(raw)
            require(req.url is None, "matrix direct URL runtime forbidden")
            if req.marker and not any(req.marker.evaluate({**env, "extra": x})
                                      for x in ("", *extras)):
                continue
            child = canonicalize_name(req.name)
            require(child in by_name, "matrix transitive distribution absent: " + child)
            require(Version(by_name[child]["version"]) in req.specifier,
                    "matrix unsatisfied runtime requirement")
            seen.add(child)
            pending.append((child, tuple(sorted(req.extras))))
    require(by_name[graph_root["name"]]["version"] == graph_root["version"] and
            by_name[graph_root["name"]]["requires_dist"] == graph_root["requires_dist"],
            "matrix installed wheel identity does not match METADATA")
    doc = json.loads(sbom.read_text("utf-8"))
    props = {p["name"]: p["value"] for p in doc["metadata"]["component"]["properties"]}
    require(props.get("cicadaport:wheel-sha256") == digest(wheel),
            "matrix wheel hash mismatch SBOM")
    require(props.get("cicadaport:runtime-coverage") == COVERAGE,
            "matrix canonical SBOM does not declare resolved runtime")
    print("G7_MATRIX_RUNTIME_CLOSURE=PASS_" + str(len(seen) - 1) + "_INSTALLED_DEPS")
    print("G7_MATRIX_RUNTIME_PYTHON=" + env["python_version"])
    print("G7_MATRIX_CANONICAL_BUILD_CELL=" + props.get("cicadaport:runtime-python", "unknown"))


def main() -> None:
    require(len(sys.argv) in (4, 5), "usage: runtime_sbom.py capture WHEEL SNAPSHOT | verify-installed PYTHON WHEEL SBOM")
    command = sys.argv[1]
    if command == "capture" and len(sys.argv) == 4:
        capture(Path(sys.argv[2]), Path(sys.argv[3]))
    elif command == "verify-installed" and len(sys.argv) == 5:
        verify_installed(Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]))
    else:
        raise ValueError("unsupported runtime SBOM mode")


if __name__ == "__main__":
    main()
