# Web Scraper — Books to Scrape

## Project Overview
A Python web scraping project that collects book information from the Books to Scrape website and stores it in a structured CSV file.

## Features
- Extracts book titles, prices, ratings, and URLs.
- Scrapes two catalogue pages using pagination.
- Saves the extracted information to `books.csv`.
- Handles HTTP request errors and missing HTML fields.
- Adds a 2-second delay between page requests.
- Uses a custom User-Agent for HTTP requests.

## Technologies Used
- Python
- Requests
- Beautiful Soup 4
- CSV module

## Installation

Install the required dependencies:

```bash
python -m pip install requests beautifulsoup4
```

## How to Run

Run the following command from the project directory:

```bash
python scraper.py
```

The program creates `books.csv` containing the scraped records.

## Extracted Fields
- `title`: Book title
- `price`: Listed book price
- `rating`: Star rating represented as a word
- `url`: Absolute URL of the book

## Pagination
The scraper follows the website's Next-page link and stops after two pages.

## Responsible Scraping
The website's `robots.txt` endpoint returned HTTP 404 when checked manually. This does not establish permission by itself. The scraper uses a conservative two-second delay between page requests and is limited to two pages.

## Project Files
- `scraper.py` — Scraping logic
- `books.csv` — Scraped output

## Learning Outcomes
Practiced HTTP requests, HTML parsing, pagination, exception handling, missing-field handling, and CSV file generation.