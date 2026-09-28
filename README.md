# E-commerce Web Scraper

A reusable Python web scraping tool that extracts product information from e-commerce websites and exports the cleaned data to CSV and Excel files.

## Features

* Scrapes product data using Requests and BeautifulSoup
* Supports multi-page scraping
* Optional maximum page limit
* Cleans and transforms scraped data
* Removes duplicate products
* Exports data to CSV and Excel
* Uses project-relative paths for portability
* Command-line interface for flexible usage

## Data Collected

The scraper extracts:

* Product Title
* Price
* Rating
* Availability
* Product URL

## Technologies

* Python
* Requests
* BeautifulSoup
* Pandas
* OpenPyXL

## Project Structure

```text
ecommerce-web-scraper/
│
├── data/
│   └── raw/
│
├── output/
│
├── src/
│   ├── scraper.py
│   ├── cleaner.py
│   ├── exporter.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper:

```bash
python src/main.py --url "https://books.toscrape.com/"
```

Limit the number of pages:

```bash
python src/main.py --url "https://books.toscrape.com/" --max-pages 5
```

The generated files are saved in the `output/` directory:

```text
books_raw.csv
books_final.csv
books_final.xlsx
```

## Example

Using the Books to Scrape demo website, the scraper can process all available pages and extract 1,000 books.

Example output fields:

| Title                | Price | Rating | Availability | Product URL |
| -------------------- | ----: | -----: | ------------ | ----------- |
| A Light in the Attic | 51.77 |      3 | In stock     | Product URL |
| Tipping the Velvet   | 53.74 |      1 | In stock     | Product URL |

## Data Source

This project uses [Books to Scrape](https://books.toscrape.com/), a website specifically designed for practicing web scraping.

## Workflow

```text
Website
   ↓
Requests
   ↓
BeautifulSoup
   ↓
Raw Data
   ↓
Pandas Cleaning
   ↓
CSV + Excel
```

## Purpose

This project demonstrates practical skills in:

* Web scraping
* HTML parsing
* Data extraction
* Data cleaning
* Data transformation
* CSV/Excel processing
* Python scripting
* Command-line tools

It is designed as a small, reusable automation tool rather than a one-time scraping script.
