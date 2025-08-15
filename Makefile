.PHONY: setup data prepare

setup:
	python -m venv .venv
	. .venv/Scripts/Activate.ps1 || true
	pip install -r requirements.txt

data:
	python src/download_data.py --season 2023

prepare:
	python src/prepare_data.py