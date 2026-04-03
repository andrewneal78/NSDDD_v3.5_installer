# NSDDD v3.5 — National Security Documents Search

Local semantic search across the National Security and Defence Documents Dataset (NSDDD) v3.5: **671 national security strategy documents from 118 countries, 1987–2025**, with 787,844 pre-computed text segment embeddings.

Search by concept, filter by country, region, organisation, year, and more — entirely offline after installation.

---

## Requirements

| | Minimum | Recommended |
|---|---|---|
| Python | 3.9 | 3.11+ |
| Disk space | 15 GB | 20 GB |
| RAM | 8 GB | 16 GB |

---

## Installation

### Before you start

**Opening a terminal:**
- **Mac:** press `Cmd + Space`, type `Terminal`, press Enter
- **Windows:** press `Win + R`, type `cmd`, press Enter

**Do you have Python 3.9+?**
Most Macs do. Windows usually does not. To check, open a terminal and type:

```
python3 --version
```

If you see `Python 3.9` or higher, you're ready. If not (or if the command isn't found), install Python from https://www.python.org/downloads/ — on Windows, tick **Add Python to PATH** during install.

---

### Step 1 — Download the installer

Click the green **Code** button on this page, then **Download ZIP**. Extract the ZIP — GitHub will usually create a folder called `NSDDD_v3.5_installer-main`.

---

### Step 2 — Open a terminal in that folder

- **Mac, easiest:** in Finder, open the extracted installer folder. Then right-click inside that folder and choose **New Terminal at Folder** or **New Terminal Tab at Folder** if that option is available.
- **Mac, alternative:** open Terminal, type `cd ` (with a space), drag the extracted installer folder into the Terminal window, and press Enter.
- **Mac, important:** do not paste the folder path by itself. For example, this is wrong: `/Users/you/NSDDD_v3.5_installer-main`. Terminal will try to run the folder as a program and show `permission denied`.
- **Windows, easiest:** in File Explorer, open the extracted installer folder. Click the address bar once so the full folder path appears, copy it, open Command Prompt, type `cd /d `, paste the copied path, and press Enter. Example:

```bat
cd /d "C:\Users\your-name\Downloads\NSDDD_v3.5_installer-main"
```
- **Windows, alternative:** in File Explorer, open the extracted installer folder, click the address bar, type `cmd`, and press Enter. On some Windows or Parallels setups this may still open in `C:\Windows\System32`, so check the prompt before running anything.
- **Windows, important:** do not run the installer from `C:\Windows\System32`. If that happens, run `cd /d "C:\path\to\NSDDD_v3.5_installer-main"` first.

---

### Step 3 — Run the installer

| Platform | Command |
|---|---|
| **Mac / Linux** | `python3 install.py` |
| **Windows** | `python install.py` |

When prompted for the install directory, press Enter to accept the default location, or type a different path and press Enter.

The installer will walk you through:

- Setting up an isolated Python environment (nothing changed system-wide)
- Downloading dataset files from Edinburgh DataShare (~5 GB) and the sentence encoder from HuggingFace (~420 MB)
- Installing Python dependencies

**Estimated time: 20–45 minutes** depending on internet speed. Downloads can be interrupted and resumed.

---

### Step 4 — Launch

| Platform | How |
|---|---|
| **Mac** | Double-click `Launch.command` in the installer folder |
| **Windows** | Double-click `Launch.vbs` in the installer folder |
| **Terminal** | `python3 launch.py` |

Your browser opens at `http://localhost:8867`. The search interface loads automatically.

If macOS says `"Launch.command" Not Opened` because Apple could not verify it, open **System Settings > Privacy & Security**, scroll to the security message about `Launch.command`, click **Open Anyway**, then run it again. If needed, you can also Control-click `Launch.command`, choose **Open**, then confirm.

> On startup, the launcher checks for installer updates before opening the interface.

> The browser may briefly show "server not found" for a few seconds while Voilà starts.

---

## Automatic updates

The launcher checks for updates each time you start:

- **Git installs (cloned repo):** `git fetch` + fast-forward pull from `origin/main` when newer.
- **Download/ZIP installs:** compares local `VERSION` with GitHub `VERSION`; if newer, downloads and overlays latest installer files while preserving local data folders (`NSDDD_v3.5_workspace`, `outputs`, `.venv`, etc.).

After applying an update, the launcher restarts automatically.

Disable auto-update for a single run:

```bash
python3 launch.py --no-update
```

Disable auto-update via environment variable:

```bash
NSDDD_AUTO_UPDATE=0 python3 launch.py
```

---

## Search Interface

The browser-based interface provides:

**Two search modes:**
- **Semantic search** — AI-powered conceptual matching (finds documents about an idea, not just exact words)
- **Keyword search** — regex-based, with optional Boolean operators (AND, OR, NOT) and fuzzy matching

**Filters:**
- Country (all 118, individually selectable)
- UN region and subregion
- International organisations (NATO, EU, ASEAN, AU, G7, G20, BRICS, Commonwealth, and more)
- Income group (World Bank classification)
- Democracy status (Freedom House)
- Document type (national security strategy, defence white paper, strategic review)
- Year range (1987–2025)
- Most recent document per country only

**Output:**
- Results grouped into semantic clusters with auto-generated labels
- Export to CSV
- Visualisations: results by year, top countries, cluster overview

---

## Dataset

| | |
|---|---|
| Documents | 671 |
| Countries | 118 |
| Coverage | 1987–2025 |
| Segments | 787,844 sentence-level |
| Embedding model | `all-mpnet-base-v2` (768-dimensional) |
| Languages | English + translations for 80+ countries |
| DataShare | https://datashare.ed.ac.uk/handle/10283/9182 |

Document types included: national security strategies (NSS), defence white papers (WP), defence and security reviews (DD), and treaty/alignment documents (TA).

---

## Advanced Use

For scripting, custom analysis, or direct access to the notebook:

```bash
jupyter notebook document_metadata_search.ipynb
```

This is the same interface without the browser launcher. Use it if you want to modify the search logic, access results programmatically, or integrate with other notebooks.

To verify your installation or diagnose issues, run:

```bash
jupyter notebook VERIFY.ipynb
```

---

## Citation

If you use NSDDD v3.5 in research, please cite:

> Neal, A. W., & Gardner, R. B. (2026). *National Security and Defence Documents Dataset (1987–2025) v3.5*. University of Edinburgh. Edinburgh DataShare. https://datashare.ed.ac.uk/handle/10283/9182

```bibtex
@dataset{neal_gardner_2026_nsddd_v3.5,
  author      = {Neal, Andrew W. and Gardner, Roy B.},
  title       = {National Security and Defence Documents Dataset (1987--2025) v3.5},
  year        = {2026},
  publisher   = {Edinburgh DataShare},
  institution = {University of Edinburgh},
  url         = {https://datashare.ed.ac.uk/handle/10283/9182}
}
```

---

## Troubleshooting

**`python3` not found**
Install Python 3.9+ from https://www.python.org/downloads/ (tick "Add to PATH" on Windows).

**Windows says it cannot open `install.py`**
This usually means Command Prompt or Terminal was opened in the wrong folder, often `C:\Windows\System32`. To fix it:

1. Open the extracted installer folder in File Explorer.
2. Click the address bar once so the full folder path appears.
3. Copy that path.
4. In Command Prompt, run:

```bat
cd /d "PASTE-THE-COPIED-FOLDER-PATH-HERE"
python install.py
```

**`permission denied` after dragging the folder into Terminal (Mac)**
This usually means the folder path was pasted on its own, so Terminal tried to run the folder as a program. Instead, use:

```bash
cd /path/to/NSDDD_v3.5_installer-main
```

or type `cd ` first, then drag the folder in and press Enter.

**`"Launch.command" Not Opened` on Mac**
This is usually macOS Gatekeeper blocking a file downloaded from the internet. To allow it:

1. Try opening `Launch.command` once.
2. Open **System Settings > Privacy & Security**.
3. Scroll down to the message saying `Launch.command` was blocked.
4. Click **Open Anyway**.
5. Run `Launch.command` again.

If that still does not work, Control-click `Launch.command`, choose **Open**, then confirm.

**Loading message doesn't clear / interface doesn't appear**
Wait briefly after launch. The server can take a few seconds to start. If needed, close the tab, wait 10 seconds, and reopen `http://localhost:8867`.

**Multiple browser tabs open / interface freezes**
Each launch starts a fresh server; old sessions are stopped automatically. If you experience freezing, close all browser tabs, wait 10 seconds, and reopen `http://localhost:8867`.

**FileNotFoundError during installation**
Check your internet connection. Re-run `python3 install.py` — downloads resume automatically.

**Memory error when loading**
Close other applications. 16 GB RAM recommended for comfortable use.

**Other issues**
Open an issue at https://github.com/andrewneal78/NSDDD_v3.5_installer/issues or email andrew.neal@ed.ac.uk

---

## License

The installer code (this repository) is released under the **MIT License**.
The NSDDD v3.5 dataset is released under **CC-BY 4.0**.
The documents in NSDDD v3.5 are official government publications in the public domain.
