# EnvíaYa · Parcial 3 · Ingeniería de Software I

Estudiante: Jhonar David De Arco Mejia · Código 1029860263

- `envios.py`: versión 3.0.0 con recargo de hora pico.
- Versión heredada v1.0.0 disponible con etiqueta v1.0.0.
- `tests/`: pruebas (pytest). `docs/`: especificación, trazabilidad, defectos y análisis del cambio.
- `CHANGELOG.md`: Keep a Changelog.

## Entorno (fish)
    python -m venv .venv
    source .venv/bin/activate.fish
    pip install -r requirements.txt
    pytest
    pytest --cov=envios --cov-branch --cov-report=term-missing
