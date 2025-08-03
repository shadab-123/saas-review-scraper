import json
from datetime import datetime
from scraper import g2, capterra, third_source

def main():
    company_name = input("Enter the company name: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    source = input("Enter the source (G2, Capterra, trustpilot): ")

    # Validate dates
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        if start_date > end_date:
            raise ValueError("Start date must be before end date.")
    except ValueError as e:
        print(f"Date error: {e}")
        return

    reviews = []

    if source.lower() == 'g2':
        reviews = g2.scrape_g2_reviews(company_name, start_date, end_date)
    elif source.lower() == 'trustpilot':
        reviews = third_source.scrape_trustpilot_reviews(company_name, start_date, end_date)
    elif source.lower() == 'capterra':
        # For Slack, company_id is "135003" and company_name is "Slack"
        company_id = "135003"
        reviews = capterra.scrape_capterra_reviews(company_id, company_name, start_date, end_date)
    else:
        print("Invalid source. Please choose G2, Capterra, or Trustpilot.")
        return

    # Output to JSON file
    with open('reviews_output.json', 'w') as json_file:
        json.dump(reviews, json_file, indent=4)

    print(f"Scraping completed. Reviews saved to 'reviews_output.json'.")

if __name__ == "__main__":
    main()