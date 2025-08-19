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
# 3) (Option B) Use the helper script to pull multiple seasons:
python src/download_data.py                 # downloads last ~10 seasons
# python src/download_data.py --start 2010 --end 2024  # custom range example

# 4) Prepare/clean data → data/processed/matches.parquet
python src/prepare_data.py

# 5) Open the notebook and run EDA
jupyter notebook notebooks/01_eda.ipynb
```

## Repo structure
```
.
.
├─ assets/                # PNG charts/screenshots for README
│  ├─ home_away_goals.png
│  └─ rolling_home_win_rate.png
├─ data/
│  ├─ raw/                # place downloaded CSVs here
│  │  └─ .keep
│  └─ processed/          # prepared files (auto-created)
│     └─ .keep
├─ notebooks/
│  └─ 01_eda.ipynb        # basic EDA
├─ src/
│  ├─ download_data.py    # helper to fetch CSV from football-data.co.uk
│  └─ prepare_data.py     # cleans & prepares dataset
├─ requirements.txt       # Python dependencies
├─ Makefile               # quick commands for setup & data prep
├─ .gitignore
└─ README.md

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


This version will:
- Render correctly on GitHub without extra edits.
- Display your charts directly from the `assets/` folder.
- Show the updated folder structure exactly as it will appear in your repo.

---

Do you want me to also add a **"Key Insights"** section under Results with 3–4 bullet points from your actual charts so the README instantly communicates your findings? That’s the part recruiters usually notice first.
