# aiboot

[![Tests](https://github.com/1c0ns/AI-Project-Bootstrapper/actions/workflows/ci.yml/badge.svg)](https://github.com/1c0ns/AI-Project-Bootstrapper/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?logo=open-source-initiative&logoColor=white)](LICENSE)

**Quickstart (10s)**
```sh
git clone https://github.com/1c0ns/AI-Project-Bootstrapper.git
cd AI-Project-Bootstrapper
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
aiboot init my_ai_project
cd my_ai_project
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
pip install -r requirements.txt
python demo/run_demo.py
```

`aiboot` scaffolds a tiny reproducible AI/NLP project with sensible defaults.

## Commands

- `aiboot init <name>` — create `<name>/` with a minimal source tree, README, env checker, and editable `pyproject.toml`.
- `aiboot doctor` — run `scripts/check_env.py` in the current folder to confirm your Python/npm setup.
- `aiboot --version` — show the CLI version.
- `aiboot --help` — show usage hints.

## What’s next?

1. Tweak the generated `src/<project>/main.py` so the toy demo reflects your dataset or model idea.
2. Keep `requirements.txt` aligned with your experiment and rerun `pip install -r requirements.txt` inside the project venv whenever dependencies change.
3. Use `python demo/run_demo.py` to sanity-check the package and call `aiboot doctor` (which runs `scripts/check_env.py`) if the environment drifts.
4. Commit the scaffold plus your code so collaborators can clone, activate a venv, and repeat the Quickstart for reproducibility.

## Philosophy
- Minimal code (under 500 lines) and only standard library.
- Consistent templates so you can focus on modeling, not scaffolding.
- Doctor command keeps each project honest about its environment.

See `docs/WHY.md` for motivation.
