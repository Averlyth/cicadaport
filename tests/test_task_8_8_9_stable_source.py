"""Task 8.8/8.9 stable-source identity (not publication or GO)."""

from pathlib import Path
import subprocess
import sys

from src.version import RELEASE_CHANNEL, SEMVER_VERSION, __version__

ROOT = Path(__file__).resolve().parent.parent


def test_stable_source_version_is_canonical_without_publication() -> None:
    assert (__version__, SEMVER_VERSION, RELEASE_CHANNEL) == (
        "3.0.0",
        "3.0.0",
        "stable",
    )
    assert "STABLE_PUBLICATION=NOT_AUTHORIZED" in (
        ROOT / "docs/audits/task-8-8-9-stable-source-prepublication.md"
    ).read_text(encoding="utf-8")


def test_stable_gate_uses_stdlib_in_isolated_mode() -> None:
    result = subprocess.run(
        [sys.executable, "-I", "-S", "scripts/verify_task_8_8_9_stable_source.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    assert "TASK889_STABLE_SOURCE_CONSISTENCY=PASS" in result.stdout
    assert "TASK889_STABLE_PUBLICATION=NOT_AUTHORIZED" in result.stdout
