# Install Flint

Flint is installed as a standalone CLI. Project environments and tool execution remain delegated to `uv`.

## Prerequisites

- Python 3.12+
- `pipx`
- `uv`

## Install From The Repository

```bash
pipx install .
```

Verify the CLI:

```bash
flint --help
```

Verify `uv` separately:

```bash
uv --version
```

If Flint reports missing tools later, install project dependencies inside the target repo:

```bash
uv sync --extra dev
```
