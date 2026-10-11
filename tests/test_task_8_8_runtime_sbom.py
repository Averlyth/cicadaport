"""Direct runtime metadata coverage of the CycloneDX candidate."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile

import pytest

from scripts.generate_cyclonedx_sbom import runtime_components_from_wheel


def make_wheel(tmp_path: Path, requirement: str | None) -> Path:
    wheel = tmp_path / "sample.whl"
    lines = ["Metadata-Version: 2.3", "Name: portscanner-pro", "Version: 3.0.0"]
    if requirement:
        lines.append(f"Requires-Dist: {requirement}")
    with ZipFile(wheel, "w") as archive:
        archive.writestr(
            "portscanner_pro-3.0.0.dist-info/METADATA", "\n".join(lines) + "\n"
        )
    return wheel


def test_declared_runtime_is_unversioned_and_auditable(tmp_path: Path) -> None:
    items = runtime_components_from_wheel(make_wheel(tmp_path, "textual<9,>=0.80"))
    assert len(items) == 1
    component = items[0]
    assert component["name"] == "textual"
    assert component["purl"] == "pkg:pypi/textual"
    assert "version" not in component
    assert {item["name"]: item["value"] for item in component["properties"]}[
        "cicadaport:version-resolution"
    ] == "unresolved"


def test_missing_declared_runtime_fails_closed(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="runtime requirements mismatch"):
        runtime_components_from_wheel(make_wheel(tmp_path, None))


def test_malformed_wheel_fails_closed(tmp_path: Path) -> None:
    wheel = tmp_path / "invalid.whl"
    with ZipFile(wheel, "w") as archive:
        archive.writestr("README", "missing metadata")
    with pytest.raises(ValueError, match="exactly one wheel METADATA"):
        runtime_components_from_wheel(wheel)


def test_strict_policy_bootstrap_without_site_packages() -> None:
    """CI must be able to check policies before installing release dependencies."""
    if sys.version_info < (3, 11):
        pytest.skip("Existing policy verifier requires stdlib tomllib")
    root = Path(__file__).resolve().parent.parent
    result = subprocess.run(
        [sys.executable, "-S", "scripts/verify_supply_chain.py", "--strict"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + "\n" + result.stderr
    assert "SUPPLY_CHAIN_POLICY=PASS" in result.stdout


@pytest.mark.parametrize(
    ("name", "version"),
    [
        ("unrelated-project", "3.0.0"),
        ("portscanner-pro", "9.9.9"),
        (None, "3.0.0"),
        ("portscanner-pro", None),
    ],
)
def test_wheel_identity_fails_closed(
    tmp_path: Path, name: str | None, version: str | None
) -> None:
    wheel = tmp_path / "wrong-identity.whl"
    headers = ["Metadata-Version: 2.3"]
    if name is not None:
        headers.append(f"Name: {name}")
    if version is not None:
        headers.append(f"Version: {version}")
    headers.append("Requires-Dist: textual<9,>=0.80")
    with ZipFile(wheel, "w") as archive:
        archive.writestr(
            "portscanner_pro-3.0.0.dist-info/METADATA", "\n".join(headers) + "\n"
        )
    with pytest.raises(ValueError, match="Wheel distribution identity mismatch"):
        runtime_components_from_wheel(wheel)


# G7 runtime-resolved closure tests. All fixtures run offline.
from scripts.runtime_sbom import (  # noqa: E402
    COVERAGE,
    SCHEMA,
    digest,
    marker_environment,
    installed_snapshot,
    resolve,
    validated_snapshot,
)


def g7_node(name: str, version: str, requirements=(), sha="a" * 64) -> dict:
    return {
        "name": name,
        "version": version,
        "requires_dist": sorted(requirements),
        "sha256": sha,
    }


def g7_valid(tmp_path: Path):
    wheel = make_wheel(tmp_path, "textual<9,>=0.80")
    nodes = [
        g7_node("portscanner-pro", "3.0.0", ["textual<9,>=0.80"], digest(wheel)),
        g7_node(
            "textual", "1.0", ["rich>=1", "platformdirs>=3; python_version < '3.14'"]
        ),
        g7_node("rich", "2.0"),
        g7_node("platformdirs", "4.0"),
    ]
    env = marker_environment()
    nodes, edges = resolve(wheel, nodes, env)
    snapshot = {
        "schema": SCHEMA,
        "wheel_sha256": digest(wheel),
        "environment": env,
        "os_release": "ubuntu",
        "nodes": nodes,
        "edges": edges,
    }
    return wheel, snapshot


def test_g7_positive_versioned_transitive_graph(tmp_path: Path) -> None:
    wheel, snapshot = g7_valid(tmp_path)
    nodes, edges = validated_snapshot(wheel, snapshot)
    assert len(nodes) == 4
    assert next(e for e in edges if e["name"] == "textual")["depends_on"] == [
        "platformdirs",
        "rich",
    ]
    assert COVERAGE == "resolved-transitive-installed-build-cell"


@pytest.mark.parametrize(
    "tamper",
    [
        "wheel_hash",
        "missing_edge",
        "missing_node",
        "duplicate",
        "wrong_version",
        "wrong_name",
        "missing_hash",
        "fake_build_tool",
        "wrong_python_env",
    ],
)
def test_g7_runtime_closure_fails_closed(tmp_path: Path, tamper: str) -> None:
    import copy

    wheel, original = g7_valid(tmp_path)
    data = copy.deepcopy(original)
    if tamper == "wheel_hash":
        data["wheel_sha256"] = "0" * 64
    elif tamper == "missing_edge":
        next(e for e in data["edges"] if e["name"] == "textual")["depends_on"] = [
            "rich"
        ]
    elif tamper == "missing_node":
        data["nodes"] = [n for n in data["nodes"] if n["name"] != "rich"]
    elif tamper == "duplicate":
        data["nodes"].append(dict(data["nodes"][-1]))
    elif tamper == "wrong_version":
        next(n for n in data["nodes"] if n["name"] == "textual")["version"] = "99.0"
    elif tamper == "wrong_name":
        next(n for n in data["nodes"] if n["name"] == "textual")["name"] = "Textual"
    elif tamper == "missing_hash":
        next(n for n in data["nodes"] if n["name"] == "rich")["sha256"] = ""
    elif tamper == "fake_build_tool":
        data["nodes"].append(g7_node("pip-audit", "2.0"))
        data["nodes"].sort(key=lambda n: n["name"])
    elif tamper == "wrong_python_env":
        data["environment"].pop("python_version")
    with pytest.raises(ValueError):
        validated_snapshot(wheel, data)


def test_g7_extra_marker_activated(tmp_path: Path) -> None:
    wheel = make_wheel(tmp_path, "textual[syntax]<9,>=0.80")
    nodes = [
        g7_node(
            "portscanner-pro", "3.0.0", ["textual[syntax]<9,>=0.80"], digest(wheel)
        ),
        g7_node("textual", "1.0", ["pygments>=2; extra == 'syntax'"]),
        g7_node("pygments", "2.0"),
    ]
    out, links = resolve(wheel, nodes, marker_environment())
    assert len(out) == 3
    assert next(e for e in links if e["name"] == "textual")["depends_on"] == [
        "pygments"
    ]


def test_g7_runtime_rejects_unresolved_direct_url(tmp_path: Path) -> None:
    wheel = make_wheel(tmp_path, "textual<9,>=0.80")
    nodes = [
        g7_node("portscanner-pro", "3.0.0", ["textual<9,>=0.80"], digest(wheel)),
        g7_node("textual", "1.0", ["badpkg @ https://example.invalid/a.whl"]),
        g7_node("badpkg", "1.0"),
    ]
    with pytest.raises(ValueError, match="direct URL"):
        resolve(wheel, nodes, marker_environment())


def g7_pip_join_fixture(tmp_path: Path):
    """Synthetic inspect/report pair for a real METADATA-bearing test wheel."""
    wheel = make_wheel(tmp_path, "textual<9,>=0.80")
    inspected = {
        "version": "1",
        "installed": [
            {
                "metadata": {
                    "name": "portscanner-pro",
                    "version": "3.0.0",
                    "requires_dist": ["textual<9,>=0.80"],
                }
            },
            {"metadata": {"name": "Textual", "version": "1.0", "requires_dist": []}},
            {"metadata": {"name": "pip", "version": "26.2.1", "requires_dist": []}},
        ],
        "environment": marker_environment(),
    }
    report = [
        {"metadata": {"name": "portscanner-pro", "version": "3.0.0"}},
        {
            "metadata": {"name": "textual", "version": "1.0"},
            "download_info": {"archive_info": {"hashes": {"sha256": "a" * 64}}},
        },
    ]
    return wheel, inspected, report


def test_g7_r1_pip_hash_bound_to_installed_version(tmp_path: Path) -> None:
    wheel, inspected, report = g7_pip_join_fixture(tmp_path)
    nodes, edges = installed_snapshot(wheel, inspected, report)
    assert [n["name"] for n in nodes] == ["portscanner-pro", "textual"]
    assert next(n for n in nodes if n["name"] == "textual")["sha256"] == "a" * 64
    assert next(e for e in edges if e["name"] == "portscanner-pro")["depends_on"] == [
        "textual"
    ]


def test_g7_r1_pep440_equivalent_version_is_accepted(tmp_path: Path) -> None:
    wheel, inspected, report = g7_pip_join_fixture(tmp_path)
    report[1]["metadata"]["name"] = "TEXTUAL"
    report[1]["metadata"]["version"] = "1.0.0"
    nodes, _ = installed_snapshot(wheel, inspected, report)
    assert len(nodes) == 2


@pytest.mark.parametrize(
    "tamper",
    [
        "version_mismatch",
        "missing_runtime_record",
        "missing_root_record",
        "duplicated_runtime_record",
        "duplicated_root_record",
        "orphan_report_record",
        "wrong_root_version",
        "malformed_report_sha",
    ],
)
def test_g7_r1_inconsistent_pip_report_fails_closed(
    tmp_path: Path, tamper: str
) -> None:
    import copy

    wheel, inspected, original_report = g7_pip_join_fixture(tmp_path)
    report = copy.deepcopy(original_report)
    if tamper == "version_mismatch":
        report[1]["metadata"]["version"] = "2.0"
    elif tamper == "missing_runtime_record":
        report.pop(1)
    elif tamper == "missing_root_record":
        report.pop(0)
    elif tamper == "duplicated_runtime_record":
        report.append(copy.deepcopy(report[1]))
    elif tamper == "duplicated_root_record":
        report.append(copy.deepcopy(report[0]))
    elif tamper == "orphan_report_record":
        report.append({"metadata": {"name": "not-installed", "version": "1.0"}})
    elif tamper == "wrong_root_version":
        report[0]["metadata"]["version"] = "3.0.1"
    elif tamper == "malformed_report_sha":
        report[1]["download_info"]["archive_info"]["hashes"]["sha256"] = "bad"
    with pytest.raises(ValueError):
        installed_snapshot(wheel, inspected, report)
