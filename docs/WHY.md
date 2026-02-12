# Why aiboot?

AI and NLP projects balloon quickly: custom folders, drifting requirements, and unclear setup steps.
`aiboot` answers that by creating a reproducible layout and curated dependency list so you can focus on modeling.

## Pain we solve
1. **Environment entropy:** Many tutorials rely on unresolved transitive dependencies or outdated instructions. The template keeps `requirements.txt`, `.gitignore`, and `pyproject.toml` aligned, and `scripts/check_env.py` locks in version checks.
2. **New project overhead:** Copying folders, licensing, and boilerplate wastes time. One command makes a complete scaffold, including MIT license and simple runnable demos.
3. **Fragile documentation:** The generated `README.md` includes ready-to-run commands and common troubleshooting tips, ensuring collaborators know exactly how to bootstrap.

`aiboot` is intentionally small so it remains a drop-in dependency for any AI/NLP experiment.
