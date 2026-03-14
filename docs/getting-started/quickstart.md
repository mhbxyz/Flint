# Quickstart

This quickstart assumes:

- Flint was installed with `pipx`
- `uv` is available in `PATH`
- you are using an existing ASGI repo

## Canonical `src/` Layout

Expected shape:

- `src/<package>/main.py`
- exported `app`
- `tests/`
- `pyproject.toml`

Run the loop:

```bash
uv sync --extra dev
flint run
flint dev
flint check
```

## Adjacent Flat Layout

Also supported:

- `main.py`
- exported `app`
- `tests/`
- `pyproject.toml`

If your repo does not match either layout, add:

```toml
[app]
module = "your_package.main:app"
```
