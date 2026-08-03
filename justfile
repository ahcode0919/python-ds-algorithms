lint:
    uv run ruff check . --fix
    uv run ruff format .
sync:
    uv sync --all-groups
test:
    uv run pytest
test-coverage:
    uv run pytest --cov=src --cov-report=term-missing
test-coverage-percentage:
    uv run pytest --cov=src --cov-report=term --cov-fail-under=98