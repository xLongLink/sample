# Sample LongLink app

## Setup with uv

1. Install `uv` if you do not already have it: <https://docs.astral.sh/uv/getting-started/installation/>
2. Create and sync the virtual environment:

```bash
uv sync
```

3. Activate the environment if you want to run commands manually:

```bash
source .venv/bin/activate
```

4. Start the app or run project commands with `uv run`, for example:

```bash
uv run python main.py
```

## Build and publish to a k3d registry

```bash
longlink build
uv run longlink build
```


### Build and push using default registry

From `sdk/sample`:

```bash
longlink build
```