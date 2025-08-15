import pandas as pd
import pathlib

RAW_DIR = pathlib.Path("data/raw")
OUT = pathlib.Path("data/processed/matches.parquet")

def load_raw():
    files = sorted(RAW_DIR.glob("E0_*.csv"))
    if not files:
        raise SystemExit("No raw CSVs found in data/raw/. Download first.")
    frames = []
    for fp in files:
        df = pd.read_csv(fp)
        df["season_start"] = int(fp.stem.split("_")[1])
        frames.append(df)
    return pd.concat(frames, ignore_index=True)

def standardize(df: pd.DataFrame) -> pd.DataFrame:
    # Minimal columns: Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR
    # Convert Date to datetime (day-first on this site)
    df = df.rename(columns=str.strip)
    for col in ["Date","HomeTeam","AwayTeam","FTHG","FTAG","FTR"]:
        if col not in df.columns:
            raise SystemExit(f"Missing expected column: {col}")
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["Date"])
    # Types
    df["FTHG"] = pd.to_numeric(df["FTHG"], errors="coerce")
    df["FTAG"] = pd.to_numeric(df["FTAG"], errors="coerce")
    df = df.dropna(subset=["FTHG","FTAG"])
    df["season"] = df["season_start"].astype(int).astype(str) + "-" + (df["season_start"]+1).astype(str).str[-2:]
    # Basic engineered fields
    df["home_win"] = (df["FTR"] == "H").astype(int)
    df["away_win"] = (df["FTR"] == "A").astype(int)
    df["draw"] = (df["FTR"] == "D").astype(int)
    df["total_goals"] = df["FTHG"] + df["FTAG"]
    return df[["Date","season","HomeTeam","AwayTeam","FTHG","FTAG","total_goals","home_win","draw","away_win"]].copy()

def main():
    df = load_raw()
    df = standardize(df)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUT, index=False)
    print(f"Wrote {OUT} with {len(df):,} rows.")

if __name__ == "__main__":
    main()