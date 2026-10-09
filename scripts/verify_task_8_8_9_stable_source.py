#!/usr/bin/env python3
"""Fail-closed, offline Task 8.8/8.9 stable source consistency gate.

This verifies source preparation ONLY. It does not authorize stable GO,
release tags, GitHub publication, packages or production readiness.
"""
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> None:
    version = read("src/version.py")
    assert '__version__ = "3.0.0"' in version
    assert 'SEMVER_VERSION = "3.0.0"' in version
    assert 'RELEASE_CHANNEL = "stable"' in version
    meta = read("pyproject.toml")
    assert 'Development Status :: 5 - Production/Stable' in meta
    assert 'Development Status :: 4 - Beta' not in meta
    assert 'requires-python = ">=3.10,<3.14"' in meta
    workflow = read(".github/workflows/ci.yml")
    assert 'RELEASE_ARTIFACT_NAME: cicadaport-3.0.0-linux-x86_64' in workflow
    assert 'name: Go 1.26.8' in workflow  # required legacy ruleset label
    assert 'go-version: "1.26.9"' in workflow
    assert workflow.count('go-version: "1.26.9"') == 5
    assert 'python -I -S scripts/verify_task_8_8_9_stable_source.py' in workflow
    assert '"contract": "EIVRC-CICADAPORT-5.6-001"' in read("scripts/generate_release_manifest.py")
    assert '"release_candidate": SEMVER_VERSION' in read("scripts/generate_release_manifest.py")
    assert '"contract": "EIVRC-CICADAPORT-5.6-001"' in read("scripts/build_release_artifacts.sh")
    assert '"version": SEMVER_VERSION' in read("scripts/generate_cyclonedx_sbom.py")
    assert 'verification_not_performed_observation_mode' in read("SECURITY.md")
    assert 'CodeQL' in read("SECURITY.md")
    acceptance = read("docs/audits/task-8-8-9-stable-source-prepublication.md")
    for marker in (
        'STABLE_GO_NO_GO=NOT_AUTHORIZED',
        'STABLE_PUBLICATION=NOT_AUTHORIZED',
        'STABLE_TAG=NOT_CREATED',
        'CODEQL_ALERT_2=OPEN_HIGH',
        'OPEN_BLOCKERS=NOT_CLEARED_FOR_STABLE',
        'PRODUCTION_DURATION_SOAK=NOT_DEMONSTRATED',
        'SUBTASK_8_7=COMPLETED_CONSOLIDATED_CLOSED_FROZEN',
    ):
        assert marker in acceptance, marker
    assert '3.0.0-rc.3' in read("docs/task-8-rc3-release.md")
    print("TASK889_STABLE_SOURCE_CONSISTENCY=PASS")
    print("TASK889_STABLE_GO=NOT_AUTHORIZED")
    print("TASK889_STABLE_PUBLICATION=NOT_AUTHORIZED")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError) as error:
        print(f"TASK889_STABLE_SOURCE_CONSISTENCY=FAIL:{error}", file=sys.stderr)
        raise SystemExit(1) from error
