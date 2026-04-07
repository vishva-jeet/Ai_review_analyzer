from selenium import webdriver
from bs4 import BeautifulSoup
import time

def scrape_reviews(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    print("Wait... solve captcha/login if needed")
    time.sleep(10)

    
    for i in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    reviews = []

    for review in soup.find_all("div", {"data-hook": "review"}):
        try:
            text = review.find("span", {"data-hook": "review-body"}).text.strip()
            rating = review.find("i", {"data-hook": "review-star-rating"}).text.strip()

            reviews.append({
                "text": text,
                "rating": rating
            })
        except:
            continue

    print("Total reviews found:", len(reviews))

    return reviews