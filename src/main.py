import argparse
from pathlib import Path

import pandas as pd

from scraper import scrape_books
from cleaner import clean_data


BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "output"


def main():
    parser = argparse.ArgumentParser(
        description="Scrape, clean, and export book data."
    )

    parser.add_argument(
        "--url",
        required=True,
        help="Website URL to scrape"
    )
    parser.add_argument(
    "--max-pages",
    type=int,
    default=None,
    help="Maximum number of pages to scrape"
)
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Starting scraper...")
    df = scrape_books(
        args.url,
        args.max_pages
    )
    print(f"\nScraped {len(df)} books.")

    # Save raw data
    raw_path = OUTPUT_DIR / "books_raw.csv"
    df.to_csv(raw_path, index=False, encoding="utf-8-sig")

    print(f"Raw data saved to: {raw_path}")

    # Clean data
    cleaned_df = clean_data(df)

    print(f"Rows after cleaning: {len(cleaned_df)}")

    # Export final files
    csv_path = OUTPUT_DIR / "books_final.csv"
    excel_path = OUTPUT_DIR / "books_final.xlsx"

    cleaned_df.to_csv(
        csv_path,
        index=False,
        encoding="utf-8-sig"
    )

    cleaned_df.to_excel(
        excel_path,
        index=False
    )

    print("\nProcess completed successfully!")
    print(f"CSV: {csv_path}")
    print(f"Excel: {excel_path}")


if __name__ == "__main__":
    main()