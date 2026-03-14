# Dogfood Checklist

Use this checklist when trying Flint on a real repo.

## Setup

- Install Flint with `pipx install .`
- Confirm `uv --version`
- In the target repo, run `uv sync --extra dev`

## Trial 1: Canonical `src/` Layout

- `flint run` prints the resolved app target and starts the app
- `flint dev` starts the app and reports cycle summaries
- editing `src/` restarts the server and reruns checks
- editing `tests/` reruns checks without restarting the server
- `flint check` runs lint, tests, and optional typecheck in order

## Trial 2: Flat Layout

- `flint run` resolves `main:app`
- `flint dev` watches the flat repo correctly
- `flint check` behaves identically to the canonical layout

## Failure Recovery

- Missing tool errors point to `uv sync --extra dev`
- Discovery errors explain whether `flint.toml` or a supported layout is required
