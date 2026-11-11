# EnvíaYa · Parcial 3 · Ingeniería de Software I

Estudiante: Jhonar David De Arco Mejia · Código 1029860263

- `envios.py`: código heredado v1.0.0 (CONFIG ya llenado).
- `tests/`: pruebas (pytest). `docs/`: especificación, trazabilidad y defectos.
- `CHANGELOG.md`: Keep a Changelog.

## Entorno (fish)
    python -m venv .venv
    source .venv/bin/activate.fish
    pip install -r requirements.txt
    pytest
    pytest --cov=envios --cov-branch --cov-report=term-missing
