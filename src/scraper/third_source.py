from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

def scrape_trustpilot_reviews(product_name, start_date, end_date):
    options = Options()
    driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)

    reviews = []
    while True:
        url = f"https://www.trustpilot.com/review/{product_name}.com"
        driver.get(url)
        time.sleep(5)  # Wait for page to load
        element = driver.find_elements(By.CSS_SELECTOR, '.styles_reviewContentwrapper__K2aRu')
        for el in element:
            lines = el.text.split('\n')
            review = {
                "title": lines[0] if len(lines) > 0 else "",
                "description": lines[1] if len(lines) > 1 else "",
            }
            reviews.append(review)
        driver.quit()
        return reviews