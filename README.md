# Home Advantage & Goal Patterns (Premier League) — Starter Project

Zero-budget, beginner-friendly sports analytics project in Python.
You’ll explore whether home advantage is changing over time and how goals are distributed.

## What you’ll learn
- Loading & cleaning CSVs with pandas
- Simple EDA: win rates, goals per game, moving averages
- Clear visualizations with matplotlib/plotly
- A tiny baseline predictor (optional stretch): "home win if home avg goals last N > away avg goals last N"

## Data source (free)
- Historical match results from **football-data.co.uk** → `https://www.football-data.co.uk/englandm.php`
  - Download season CSVs (e.g., `E0_2023.csv`, `E0_2022.csv`, etc.) and place them in `data/raw/`.

> Tip: Start with **one** season to keep it simple, then add more.

## Quickstart
```bash
# 1) Create and activate a virtual environment (example for Windows PowerShell)
python -m venv .venv
. .venv/Scripts/Activate.ps1    # on macOS/Linux: source .venv/bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) (Option A) Manually download CSV(s) to data/raw/
# 3) (Option B) Try the helper script (works if the URL pattern hasn't changed):
python src/download_data.py --season 2023

# 4) Prepare/clean data → data/processed/matches.parquet
python src/prepare_data.py

# 5) Open the notebook and run EDA
jupyter notebook notebooks/01_eda.ipynb
```

## Repo structure
```
.
├─ data/
│  ├─ raw/         # place downloaded CSVs here
│  └─ processed/   # prepared files (auto-created)
├─ notebooks/
│  └─ 01_eda.ipynb # basic EDA
├─ src/
│  ├─ download_data.py
│  └─ prepare_data.py
├─ requirements.txt
├─ Makefile
└─ .gitignore
```

## Stretch goals (optional)
- Add more seasons and make a line chart of **home win rate by season**.
- Build a very simple baseline predictor:
  - Compute last-5 moving averages for home & away teams
  - Predict "Home Win" if home avg GF > away avg GF, else "Not Home Win"
  - Evaluate with accuracy / precision / recall
- Make a tiny **Streamlit** page with 2–3 plots.

## License
This template is MIT-licensed. Check original data source license separately.