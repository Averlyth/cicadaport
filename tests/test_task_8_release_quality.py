"""TASK 8 stable source identity and quality gates (history remains intact)."""

from pathlib import Path

from src.version import RELEASE_CHANNEL, SEMVER_VERSION, __version__

ROOT = Path(__file__).resolve().parent.parent


def test_stable_source_identity_is_canonical_and_not_published() -> None:
    assert SEMVER_VERSION == "3.0.0"
    assert __version__ == "3.0.0"
    assert RELEASE_CHANNEL == "stable"
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert "cicadaport-3.0.0-linux-x86_64" in workflow


def test_quality_coverage_and_resource_gates_are_required() -> None:
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    for marker in (
        "name: Python quality and resource hygiene",
        "python -m black --check src tests",
        "python -m flake8 src tests",
        "python -m mypy src",
        "--cov-fail-under=82",
        "PytestUnraisableExceptionWarning",
        "name: Operational acceptance and bounded-resource soak",
        "SYNTHETIC_SOAK_10_ITERATIONS=PASS",
        "needs: [supply-chain-policy, secret-scan, python-quality, operational-acceptance]",
    ):
        assert marker in workflow


def test_historical_rc2_evidence_is_not_rebranded() -> None:
    historical = ROOT / "docs/contracts/task-5-6-enterprise-validation-rc2-candidate.md"
    assert historical.is_file()
    text = historical.read_text(encoding="utf-8")
    assert "3.0.0-rc.2" in text
    status = (ROOT / "docs/task-8-status.md").read_text(encoding="utf-8")
    assert "RC3_TAG=NOT_CREATED" in status
    assert "STABLE_RELEASE_PUBLICATION=NOT_AUTHORIZED" in status


def test_security_go_toolchain_is_pinned_across_entrypoints() -> None:
    """Do not reintroduce the reachable Go 1.26.8 stdlib TLS advisory."""
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    setup = (ROOT / "setup.py").read_text(encoding="utf-8")
    check_tools = (ROOT / "scripts/check_tools.sh").read_text(encoding="utf-8")
    audit = (ROOT / "scripts/audit_dependencies.sh").read_text(encoding="utf-8")
    go_pin = (ROOT / ".go-version").read_text(encoding="utf-8")

    assert go_pin == "1.26.9\n"
    assert 'GO_VERSION: "1.26.9"' in workflow
    assert workflow.count('go-version: "1.26.9"') == 5
    assert 'go-version: "1.26.8"' not in workflow
    assert "name: Go 1.26.8" in workflow  # Legacy required status context.
    assert 'GO_VERSION = "go1.26.9"' in setup
    assert "go1.26.9" in check_tools
    assert '"go1.26.9"' in audit
