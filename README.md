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
The target website's robots.txt endpoint returned HTTP 404 when checked. A missing robots.txt file does not, by itself, establish permission to scrape. This project uses Books to Scrape as a practice website for learning web scraping. The scraper uses a custom User-Agent and a two-second delay between catalogue page requests to reduce request frequency.

## Project Files
- `scraper.py` — Scraping logic
- `books.csv` — CSV output containing 40 book records with four fields: title, price, rating, and URL
- `website.png` — Screenshot of the target website
- `output.png` — Screenshot of the scraped CSV output

## Learning Outcomes
Practiced HTTP requests, HTML parsing, pagination, exception handling, missing-field handling, and CSV file generation.