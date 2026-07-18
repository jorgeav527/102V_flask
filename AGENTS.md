# 102V_flask

## Quick start

```bash
uv run flask --app main run --debug     # dev server
```

## Package management

- **uv** (not pip/poetry/virtualenv) — `uv add <pkg>`, `uv sync`, `uv lock`
- Python 3.10+ (`.python-version`, `pyproject.toml`)
- `.venv/` is gitignored

## Project structure

- `main.py` — Flask app entrypoint
- `templates/` — Jinja2 templates (rendered via `render_template`)
- No tests, no CI, no linters, no type checkers
