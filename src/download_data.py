import argparse
import datetime
import pathlib
import sys
from urllib.request import urlretrieve

# NOTE: football-data.co.uk sometimes changes naming.
# For EPL (E0), recent files can follow patterns like E0.csv or E0_2023.csv.
# Start manually if this fails.

BASE = "https://www.football-data.co.uk/mmz4281"


def season_code(year: int) -> str:
    """Convert start year to the mmz4281 code (e.g., 2324 for 2023-24)."""
    y2 = (year + 1) % 100
    return f"{str(year % 100).zfill(2)}{str(y2).zfill(2)}"


def download_season(season_start: int) -> None:
    """Download a single season CSV into data/raw."""
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
        print(
            "Download failed. Try manual download from football-data.co.uk.",
            file=sys.stderr,
        )
        print(e, file=sys.stderr)
        sys.exit(1)


def main(start: int, end: int) -> None:
    """Download a range of seasons (inclusive)."""
    if end < start:
        raise SystemExit("--end must be >= --start")
    for season_start in range(start, end + 1):
        download_season(season_start)


if __name__ == "__main__":
    today = datetime.date.today()
    latest_start = today.year - 1  # last completed season start
    default_start = latest_start - 9  # roughly last 10 seasons
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--start",
        type=int,
        default=default_start,
        help="First season start year, e.g., 2014 for 2014-15.",
    )
    ap.add_argument(
        "--end",
        type=int,
        default=latest_start,
        help="Last season start year (inclusive).",
    )
    ap.add_argument(
        "--season",
        type=int,
        help="Download a single season (deprecated, equivalent to --start YEAR --end YEAR)",
    )
    args = ap.parse_args()
    if args.season is not None:
        main(args.season, args.season)
    else:
        main(args.start, args.end)

