from __future__ import annotations

from pathlib import Path
import tomllib


def test_pyproject_declares_console_script() -> None:
    data = tomllib.loads(Path("pyproject.toml").read_text())

    assert data["project"]["name"] == "flint-dev"
    assert data["project"]["scripts"]["flint"] == "flint.cli:main"


def test_install_doc_references_pipx_and_uv() -> None:
    content = Path("docs/getting-started/install.md").read_text()

    assert "pipx install ." in content
    assert "uv sync --extra dev" in content
