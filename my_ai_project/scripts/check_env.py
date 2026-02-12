
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
            print("
Missing packages detected:")
            for pkg in missing:
                print(f" - {pkg}")
            print("
Install them with: python -m pip install -r requirements.txt")
            sys.exit(1)

        print("
Environment looks healthy. Run `python demo/run_demo.py` to verify.")

    if __name__ == "__main__":
        _main()
