"""Entry point for the aiboot CLI."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from textwrap import dedent

VERSION = "0.1.0"

_GITIGNORE = dedent(
    """
    __pycache__/
    *.py[cod]
    .venv/
    .mypy_cache/
    .pytest_cache/
    .DS_Store
    venv/
    """
)

_LICENSE = dedent(
    """
    MIT License

    Copyright (c) 2024 Rico Reinbacher and Julius Troegele

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """
)

_REQUIREMENTS_TXT = """# Minimal baseline for embedding/classification workflows (trim as you go)
numpy
scipy
scikit-learn
requests
tqdm
torch
transformers
sentence-transformers
"""

_CHECK_SCRIPT = dedent(
    """
    '''Simple environment validator for the project.'''

    import importlib.util
    import sys
    from pathlib import Path

    REQUIRED = [
        "numpy",
        "scipy",
        "sklearn",
        "requests",
        "tqdm",
        "torch",
        "transformers",
        "sentence_transformers",
    ]

    def _module_exists(name: str) -> bool:
        return importlib.util.find_spec(name) is not None

    def _main() -> None:
        print(f"Python: {sys.version.splitlines()[0]}")
        print(f"Executable: {sys.executable}")
        pip_path = Path(sys.executable).parent / "pip"
        print(f"Pip: {pip_path}")

        missing = [pkg for pkg in REQUIRED if not _module_exists(pkg)]
        if missing:
            print("\nMissing packages detected:")
            for pkg in missing:
                print(f" - {pkg}")
            print("\nInstall them with: python -m pip install -r requirements.txt")
            sys.exit(1)

        print("\nEnvironment looks healthy. Run `python demo/run_demo.py` to verify.")

    if __name__ == "__main__":
        _main()
    """
)


def _write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _build_readme(project: str) -> str:
    return dedent(
        f"""
        # {project}

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

        - `src/{project}` – package with a tiny runnable example using scikit-learn.
        - `demo/run_demo.py` – CLI entry that imports the package and prints metrics.
        - `scripts/check_env.py` – environment sanity checks.
        - `requirements.txt` + `pyproject.toml` – editable installation and curated baseline.

        ## Troubleshooting

        - **python vs python3**: macOS/Linux may need `python3` if `python` is 2.7.
        - **pip vs pip3**: match the interpreter (`python3 -m pip install ...`).
        - **Activating the venv**: `source .venv/bin/activate` (or `.\\.venv\\Scripts\\activate` on Windows).
        - **Missing deps**: run `python scripts/check_env.py` to get guided fixes.

        ## What’s next?

        1. Edit `src/{project}/main.py` to replace the toy classifier with your own data/model/workflow.
        2. Keep `requirements.txt` aligned with your experiment and rerun `pip install -r requirements.txt` inside the project venv after changing dependencies.
        3. Run `python demo/run_demo.py` to sanity check the package and `aiboot doctor` (which executes `scripts/check_env.py`) whenever the environment drift.
        4. Commit the generated files plus your new code; teammates can then clone, create `.venv`, and repeat the Quickstart to reproduce the project.
        """
    )


def _build_pyproject(project: str) -> str:
    deps_block = [
        "numpy",
        "scipy",
        "scikit-learn",
        "requests",
        "tqdm",
        "torch",
        "transformers",
        "sentence-transformers",
    ]
    deps_lines = "\n".join(f'    "{dep}",' for dep in deps_block)
    return (
        f"""[project]
name = "{project}"
version = "0.1.0"
description = "Small reproducible AI/NLP starter."
authors = [{{ name = "Rico Reinbacher" }}, {{ name = "Julius Troegele" }}]
readme = "README.md"
requires-python = ">=3.10"
license = "MIT"
dependencies = [
{deps_lines}
]

[project.urls]
Homepage = "https://github.com/1c0ns/AI-Project-Bootstrapper"
Repository = "https://github.com/1c0ns/AI-Project-Bootstrapper"

[tool.setuptools]
package-dir = {{ "": "src" }}

[tool.setuptools.packages.find]
where = ["src"]

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
"""
    )


def _build_main(project: str) -> str:
    return dedent(
        f"""
        '''Example AI/NLP entry point.'''

        from sklearn import datasets
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import classification_report
        from sklearn.model_selection import train_test_split


        def run_demo() -> None:
            '''Train a tiny classifier and print a report.'''
            data = datasets.load_iris()
            X_train, X_test, y_train, y_test = train_test_split(
                data.data, data.target, test_size=0.2, random_state=42
            )
            model = RandomForestClassifier(n_estimators=20, random_state=42)
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            report = classification_report(y_test, predictions, zero_division=0)
            print("Iris classification report:\n", report)


        if __name__ == "__main__":
            run_demo()
        """
    )


def _build_demo_run(project: str) -> str:
    return dedent(
        f"""
        '''Demo runner that imports the project package.'''

        from {project} import run_demo


        def main() -> None:
            run_demo()


        if __name__ == "__main__":
            main()
        """
    )


def _build_init(project: str) -> str:
    return dedent(
        """
        '''Top-level package initializer.'''

        from .main import run_demo

        __all__ = ["run_demo"]
        """
    )


def init_project(name: str) -> int:
    project_dir = Path(name)
    if project_dir.exists():
        print(f"Error: '{name}' already exists.")
        return 1
    if not name.isidentifier():
        print("Project name must be a valid Python identifier.")
        return 1

    _write_file(project_dir / "README.md", _build_readme(name))
    _write_file(project_dir / "requirements.txt", _REQUIREMENTS_TXT)
    _write_file(project_dir / "LICENSE", _LICENSE)
    _write_file(project_dir / "pyproject.toml", _build_pyproject(name))
    _write_file(project_dir / ".gitignore", _GITIGNORE)
    _write_file(project_dir / "scripts" / "check_env.py", _CHECK_SCRIPT)
    _write_file(project_dir / "src" / name / "__init__.py", _build_init(name))
    _write_file(project_dir / "src" / name / "main.py", _build_main(name))
    _write_file(project_dir / "demo" / "run_demo.py", _build_demo_run(name))

    print(f"Project '{name}' created. Run `cd {name}` then:")
    print("  python3 -m venv .venv")
    print("  source .venv/bin/activate")
    print("  python -m pip install -r requirements.txt")
    return 0


def doctor() -> int:
    script = Path.cwd() / "scripts" / "check_env.py"
    if not script.exists():
        print("No scripts/check_env.py found in the current directory.")
        return 1
    result = subprocess.run([sys.executable, str(script)])
    return result.returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="aiboot",
        description="Scaffold and check reproducible AI/NLP projects.",
    )
    parser.add_argument("--version", action="version", version=f"aiboot {VERSION}")
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Create a new project.")
    init_parser.add_argument("name", help="Name of the new AI project (Python identifier).")
    init_parser.set_defaults(func=lambda args: init_project(args.name))

    doctor_parser = subparsers.add_parser("doctor", help="Run scripts/check_env.py in the current folder.")
    doctor_parser.set_defaults(func=lambda args: doctor())

    args = parser.parse_args(argv)
    if hasattr(args, "func"):
        return args.func(args)
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
