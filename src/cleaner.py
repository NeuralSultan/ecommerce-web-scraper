import pandas as pd


def clean_data(df):
    """Clean and transform scraped book data."""

    df = df.copy()

    # Remove extra spaces from text columns
    df["Title"] = df["Title"].str.strip()
    df["Availability"] = df["Availability"].str.strip()

    # Convert price from text to numeric
    df["Price"] = (
        df["Price"]
        .str.replace("£", "", regex=False)
        .str.replace("Â", "", regex=False)
        .str.strip()
        .astype(float)
)

    # Convert rating words to numbers
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["Rating"] = df["Rating"].map(rating_map)

    # Remove duplicate products
    df = df.drop_duplicates(subset=["Product URL"])

    # Reset index
    df = df.reset_index(drop=True)

    return df


if __name__ == "__main__":

    input_path = "output/books_raw.csv"
    output_path = "output/books_cleaned.csv"

    df = pd.read_csv(input_path)

    cleaned_df = clean_data(df)

    cleaned_df.to_csv(output_path, index=False)

    print("Cleaning completed!")
    print(f"Rows after cleaning: {len(cleaned_df)}")