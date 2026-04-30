# Sample LongLink app

<br />

## Setup using pip

<br />

## Setup with uv

```bash
uv sync 
# To upgrade the packages
# uv sync --upgrade
```

Start the app in development mode:

```bash
uv run longlink dev
```

Build the application using docker:

```bash
uv run longlink build
```

## TODO

- Add `ruff` for linting and formatting
- Add `mypy` or `pyright` for type checking
- Add a dependency lockfile for reproducible installs
- Add pre-commit hooks for local automation
- Add CI for tests, linting, and type checks
- Add coverage reporting and a test matrix
