import time

import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_books(start_url, max_pages=None):
    """Scrape books from all available pages."""

    books = []
    current_url = start_url
    page_number = 1

    session = requests.Session()

    session.headers.update({
        "User-Agent": "Mozilla/5.0"
    })

    while current_url:
        if max_pages is not None and page_number > max_pages:
            break
        print(f"Scraping page {page_number}...")

        try:
            response = session.get(
                current_url,
                timeout=15
            )

            response.raise_for_status()

        except requests.RequestException as error:

            print(f"Failed to scrape page {page_number}.")
            print(f"Error: {error}")

            print("Stopping scraper safely...")

            break

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for book in soup.select("article.product_pod"):

            title = book.h3.a["title"]

            price = book.select_one(
                ".price_color"
            ).text.strip()

            rating = book.select_one(
                "p.star-rating"
            )["class"][1]

            availability = book.select_one(
                ".availability"
            ).text.strip()

            product_url = urljoin(
                current_url,
                book.h3.a["href"]
            )

            books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability,
                "Product URL": product_url
            })

        next_button = soup.select_one(
            "li.next a"
        )

        if next_button:

            current_url = urljoin(
                current_url,
                next_button["href"]
            )

            page_number += 1

            # Small delay between requests
            time.sleep(1)

        else:

            current_url = None

    return pd.DataFrame(books)