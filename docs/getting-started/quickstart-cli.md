# CLI Quickstart

[Project README](../../README.md) · [Docs Index](../README.md) · [Getting Started](README.md)

Goal: create and validate your first Flint Python CLI project.

Need CLI installation first? Use the [Install guide](install.md).

## Prerequisites

- Python 3.12+
- `uv` installed and available in `PATH`

## 1) Create a new CLI project

```bash
flint new mycli --profile cli
cd mycli
```

Expected result:

- `src/` package scaffold generated with CLI entrypoint
- baseline test file generated
- `flint.toml` contains `profile = "cli"`

## 2) Install dependencies

```bash
flint install
```

Expected result:

- virtual environment created
- dev tooling installed (`pytest`, `ruff`, `pyright`)

## 3) Run baseline quality flow

```bash
flint test
flint check
```

Expected result:

- baseline CLI test passes
- `check` pipeline completes with deterministic status output

Note: profile-aware `flint run`/`flint dev` behavior for CLI projects is tracked in issue #34.

## Success checklist

- [ ] `flint new --profile cli` generated project successfully
- [ ] dependencies installed with `flint install`
- [ ] `flint test` passes
- [ ] `flint check` passes

## See Also

- [Getting Started index](README.md)
- [Install guide](install.md)
- [Alpha troubleshooting](troubleshooting-alpha.md)
