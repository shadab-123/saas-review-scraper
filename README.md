# SaaS Review Scraper

A Python tool to scrape reviews for SaaS products from G2, Capterra, and Trustpilot using Selenium.

## Features

- Scrapes reviews for a given company from:
  - G2
  - Capterra
  - Trustpilot
- Outputs reviews in structured JSON format
- Supports date range filtering
- Easy to extend for other sources

## Requirements

- Python 3.8+
- Google Chrome browser
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (matching your Chrome version)
- Selenium
- pandas, beautifulsoup4, lxml (for some sources)

Install dependencies:
```sh
pip install -r requirements.txt
```

## Setup

1. **Download ChromeDriver**  
   - [Get ChromeDriver](https://chromedriver.chromium.org/downloads) for your Chrome version.
   - Place `chromedriver.exe` in your project folder.

2. **Configure your environment**  
   - (Optional) Use Anaconda for easy package management.

## Usage

Run the scraper from the command line:

```sh
python src/index.py
```

You will be prompted for:
- Company name (e.g., `Slack`)
- Start date (`YYYY-MM-DD`)
- End date (`YYYY-MM-DD`)
- Source (`G2`, `Capterra`, or `trustpilot`)

Example:
```
Enter the company name: Slack
Enter the start date (YYYY-MM-DD): 2024-01-01
Enter the end date (YYYY-MM-DD): 2025-01-01
Enter the source (G2, Capterra, trustpilot): capterra
```

Reviews will be saved to `reviews_output.json`.

## Project Structure

```
pulse/
├── requirements.txt
├── reviews_output.json
└── src/
    ├── index.py
    └── scraper/
        ├── g2.py
        ├── capterra.py
        └── third_source.py
```

## Notes

- For Capterra, the product ID for Slack is hardcoded as `135003`. Update this for other products as needed.
- CSS selectors may need adjustment if the review sites change their HTML structure.
- Respect the terms of service of each site.

## License

MIT License

---

**Happy scraping!**