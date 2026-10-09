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
