# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is the **NSDDD v3.5 installer** — a self-contained Python installer and launcher for the National Security and Defence Documents Dataset (671 documents, 118 countries, 1987–2025). Users run `python3 install.py` once, then use platform launchers (Launch.command / Launch.vbs) to start a local Voilà web interface at `http://127.0.0.1:8867`.

## Key commands

```bash
# Run the installer (creates .venv, downloads dataset files from Edinburgh DataShare)
python3 install.py

# Launch the search interface directly (bypasses launchers)
python3 launch.py

# Launch without checking for updates
python3 launch.py --no-update

# Launch in background, open browser, then exit
python3 launch.py --detach
```

There is no build step, test suite, or linter configured in this repo.

## Versioning

Version is stored in `VERSION` (project root) as a date-stamp string: `YYYY.MM.DD.N` where `N` is a counter starting at 1 that increments for multiple releases on the same day.

**The `VERSION` file MUST be bumped for every change that affects user-facing behaviour**, including:
- Any edit to `document_metadata_search_voila.ipynb` (the notebook is the search UI)
- Changes to `_library/` (search engine logic)
- Changes to `launch.py`, `install.py`, or `config.py`

The auto-update mechanism in `launch.py` compares the local `VERSION` against the remote `VERSION` on GitHub. If they differ, the installer self-updates from GitHub. **If you change the notebook or any runtime file without bumping `VERSION`, users will not receive the update.**

### How to bump

1. Open `VERSION`.
2. If today's date already appears, increment `N` (e.g. `2026.04.10.1` → `2026.04.10.2`).
3. Otherwise, write today's date with `N=1` (e.g. `2026.04.11.1`).
4. Save and commit alongside your other changes.

## Bundled data files

`document_metadata_3.5.csv` is committed to the repo root and is part of the installer package itself. It is **not** downloaded by `install.py` — users receive it when they clone the repo or download the ZIP from GitHub.

It contains one row per document (672 rows): country, year, page length, word count, document type, language, and publishing ministry. The notebook loads this file at startup to compute per-country summary statistics (`COUNTRY_NORM_STATS`) used to render the normalisation context panel alongside search results.

**Any change to `document_metadata_3.5.csv` must be accompanied by a VERSION bump** so that existing users receive the updated file via the auto-update mechanism.

## Architecture

**Entry points:**
- `install.py` — one-time setup: checks Python/disk/RAM, downloads files from Edinburgh DataShare, creates `.venv`, installs pip dependencies (including `voila`), downloads the MPNet encoder model, writes `install_config.json`.
- `launch.py` — runtime launcher: checks for installer updates (git pull or ZIP overlay), finds the correct Python/venv, starts Voilà serving `document_metadata_search_voila.ipynb` on port 8867, opens the browser.

**Configuration hub — `config.py`:**
All installer-level constants live here: `PYTHON_VERSION_MIN`, `DOWNLOADS` dict (filenames, sizes, extract targets, required/optional flags), DataShare API endpoints, `DEFAULT_INSTALL_DIR`, disk/RAM thresholds. This is the first place to update when adding downloads or changing requirements.

**`utils/` — installer utilities:**
- `datashare.py` — `DataShareClient`: resolves filenames to Edinburgh DataShare bitstream UUIDs and download URLs via the DSpace REST API. Falls back through `requests` → stdlib `urllib` → `curl`.
- `download.py` — `download_file()` with resume, retry (3×), progress callback, and size validation. Falls back through `requests` → `curl` → stdlib `urllib`.
- `extract.py` — ZIP extraction with path-component stripping (handles deeply nested archives).
- `setup.py` — directory structure creation and installation validation.
- `verify.py` — SHA-256 file verification utilities.

**`_library/` — search engine (used by the notebook at runtime):**
- `boolean_parser.py` — recursive-descent parser producing an AST (`TermNode`, `AndNode`, `OrNode`, `NotNode`). Supports `AND`/`OR`/`NOT`/`&`/`|`/`!`, quoted phrases, wildcards, and grouping with `()`.
- `boolean_executor.py` — walks the AST, calls a caller-supplied `keyword_search_func(term, model_dict)` at each leaf, combines scores using `match_count` (default), `avg_score`, or `max_score` strategies.

**Workspace (created at install time, not in this repo):**
```
NSDDD_v3.5_workspace/
├── model/          # MPNet embeddings + segment/document/country dicts
├── metadata/       # document_metadata.csv, Country_metadata.csv
├── documents/      # optional text/PDF/spaCy files
└── documentation/  # README, CITATION, LICENSE, WHATS_NEW
```

**Auto-update mechanism (`launch.py`):**
- Git installs: `git fetch` + compare HEAD vs origin, then `git pull --ff-only`.
- ZIP/download installs: fetches `VERSION` from GitHub raw, compares with local `VERSION`, downloads and overlays the repo ZIP if different. `PRESERVE_TOP_LEVEL` controls which directories are never overwritten (`.git`, `.venv`, `NSDDD_v3.5_workspace`, `outputs`).
- Disable with env var: `NSDDD_AUTO_UPDATE=0`.

**Python environment resolution (both scripts):**
`install_config.json` (written by `install.py`) records the chosen venv Python path. `launch.py::find_python()` reads it first, then searches standard venv locations, then falls back to `sys.executable`. The first Python that can `import voila` wins.

## Important constraints

- **Minimum Python: 3.10** — `install.py` uses `X | Y` union type hints (PEP 604). `PYTHON_VERSION_MIN = (3, 10)` in `config.py`.
- **Windows: Python 3.13+ is blocked** — PyTorch/sentence-transformers wheels are not reliably available. The installer enforces Python 3.11 or 3.12 on Windows.
- **Windows UNC/network paths are blocked** — the installer exits early if run from a `\\server\share` path.
- The `_library/` package is imported by the Jupyter notebook at runtime using `sys.path` manipulation; it is not installed as a package.
