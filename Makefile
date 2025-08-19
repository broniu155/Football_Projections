.PHONY: setup data prepare

setup:
	python -m venv .venv
	. .venv/Scripts/Activate.ps1 || true
	pip install -r requirements.txt

data:
        # Download last 15 Premier League seasons
        python src/download_data.py --start 2010 --end 2024

prepare:
        python src/prepare_data.py
