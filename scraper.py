import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
OUTPUT_FILE = "books.csv"

session = requests.Session()

session.headers.update({
    "User-Agent": "WeInternEducationalScraper/1.0"
})

def fetch_page(url):
    """Fetch a webpage and return its HTML content."""
    try:
        response = session.get(url, timeout=15)
        response.raise_for_status()
        return response.text

    except requests.RequestException as error:
        print(f"Error fetching {url}: {error}")
        return None
    
def parse_books(html, page_url):
    """Extract book details from a page's HTML."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for item in soup.select("article.product_pod"):
        title_element = item.select_one("h3 a")
        price_element = item.select_one(".price_color")
        rating_element = item.select_one(".star-rating")

        book = {
            "title": (
                title_element.get("title", "").strip()
                if title_element else ""
            ),
            "price": (
                price_element.get_text(strip=True).replace("Â£", "£")
                if price_element else ""
            ),
            "rating": (
                next(
                    (
                        name for name in
                        ["One", "Two", "Three", "Four", "Five"]
                        if name in rating_element.get("class", [])
                    ),
                    ""
                )
                if rating_element else ""
            ),
            "url": (
                urljoin(page_url, title_element.get("href", ""))
                if title_element else ""
            ),
        }

        books.append(book)

    return books

def get_next_page(html, current_url):
    """Return the next page URL, or None if no next page exists."""
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next a")

    if next_link:
        return urljoin(current_url, next_link.get("href", ""))

    return None

def save_to_csv(books, filename):
    """Save scraped book details to a CSV file."""
    fieldnames = ["title", "price", "rating", "url"]

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

    print(f"Saved {len(books)} books to {filename}")
    
def scrape_books():
    """Scrape books from multiple pages with a delay between requests."""
    all_books = []
    current_url = BASE_URL

    pages_scraped = 0
    max_pages = 2

    while current_url and pages_scraped < max_pages:
        print(f"Scraping: {current_url}")

        html = fetch_page(current_url)

        if html is None:
            print("Stopping because the page could not be fetched.")
            break

        books = parse_books(html, current_url)
        all_books.extend(books)

        print(f"Found {len(books)} books on this page.")
        pages_scraped += 1

        current_url = get_next_page(html, current_url)

        if current_url:
            time.sleep(2)

    return all_books

if __name__ == "__main__":
    books = scrape_books()

    if books:
        save_to_csv(books, OUTPUT_FILE)
    else:
        print("No books were scraped. CSV file was not created.")