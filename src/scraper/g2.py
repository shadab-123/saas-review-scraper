from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

def scrape_g2_reviews(product_name, start_date, end_date):
    options = Options()
    driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)

    reviews = []
    page = 1
    while True:
        url = f"https://www.g2.com/products/{product_name}/reviews"
        driver.get(url)
        time.sleep(5)  # Wait for page to load
        element = driver.find_elements(By.CSS_SELECTOR, '.e1xzmg0z.c1ofrhif.typo-10.mb-6.space-y-4.p-6.lg\\:space-y-8')
        for el in element:
            lines = el.text.split('\n')
            review = {
                "name": lines[1] if len(lines) > 1 else "",
                "designation": lines[2] if len(lines) > 2 else "",
                "field": lines[3] if len(lines) > 3 else "",
                "userStaying": lines[4] if len(lines) > 4 else "",
                "title": lines[5] if len(lines) > 5 else "",
                "date": lines[6] if len(lines) > 6 else "",
                "rating": lines[7] if len(lines) > 7 else "",
                "description": lines[8] if len(lines) > 8 else "",
            }
            reviews.append(review)
        driver.quit()
        return reviews