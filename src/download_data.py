import argparse
import pathlib
import sys
from urllib.request import urlretrieve

# NOTE: football-data.co.uk sometimes changes naming.
# For EPL (E0), recent files can follow patterns like E0.csv or E0_2023.csv.
# Start manually if this fails.

BASE = "https://www.football-data.co.uk/mmz4281"

def season_code(year: int):
    # Convert calendar start year to YYYYYY code used by mmz4281 (e.g., 2324 for 2023-24)
    y2 = (year + 1) % 100
    return f"{str(year%100).zfill(2)}{str(y2).zfill(2)}"

def main(season_start: int):
    code = season_code(season_start)
    # E0 = Premier League. For other leagues see the site.
    path = f"{BASE}/{code}/E0.csv"
    out = pathlib.Path("data/raw") / f"E0_{season_start}.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {path} -> {out}")
    try:
        urlretrieve(path, out.as_posix())
        print("Done.")
    except Exception as e:
        print("Download failed. Try manual download from football-data.co.uk.", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=2023, help="Season start year, e.g., 2023 for 2023-24")
    args = ap.parse_args()
    main(args.season)