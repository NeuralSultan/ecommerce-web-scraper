from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_PATH = BASE_DIR / "output" / "books_cleaned.csv"
CSV_OUTPUT = BASE_DIR / "output" / "books_final.csv"
EXCEL_OUTPUT = BASE_DIR / "output" / "books_final.xlsx"


def export_data(df):
    """Export cleaned data to CSV and Excel."""

    df.to_csv(CSV_OUTPUT, index=False, encoding="utf-8-sig")
    df.to_excel(EXCEL_OUTPUT, index=False)

    print("Export completed!")
    print(f"CSV: {CSV_OUTPUT}")
    print(f"Excel: {EXCEL_OUTPUT}")


if __name__ == "__main__":

    df = pd.read_csv(INPUT_PATH)

    export_data(df)