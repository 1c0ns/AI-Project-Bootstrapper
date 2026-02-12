
# my_ai_project

## Quickstart

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python demo/run_demo.py
```

This template keeps the focus on AI/NLP tasks. `python3 -m venv .venv` is not run
automatically so you stay in control of environment creation.

## Layout

- `src/my_ai_project` – package with a tiny runnable example using scikit-learn.
- `demo/run_demo.py` – CLI entry that imports the package and prints metrics.
- `scripts/check_env.py` – environment sanity checks.
- `requirements.txt` + `pyproject.toml` – editable installation and curated baseline.

## Troubleshooting

- **python vs python3**: macOS/Linux may need `python3` if `python` is 2.7.
- **pip vs pip3**: match the interpreter (`python3 -m pip install ...`).
- **Activating the venv**: `source .venv/bin/activate` (or `.\.venv\Scripts\activate` on Windows).
- **Missing deps**: run `python scripts/check_env.py` to get guided fixes.

## What’s next?

1. Edit `src/my_ai_project/main.py` to replace the toy classifier with your own data/model/workflow.
2. Keep `requirements.txt` aligned with your experiment and rerun `pip install -r requirements.txt` inside the project venv after changing dependencies.
3. Run `python demo/run_demo.py` to sanity check the package and `aiboot doctor` (which executes `scripts/check_env.py`) whenever the environment drift.
4. Commit the generated files plus your new code; teammates can then clone, create `.venv`, and repeat the Quickstart to reproduce the project.
