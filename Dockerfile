FROM ghcr.io/astral-sh/uv:python3.12-bookworm

COPY . /workspace

WORKDIR /workspace/sample

RUN uv sync --frozen

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--log-level", "debug"]
