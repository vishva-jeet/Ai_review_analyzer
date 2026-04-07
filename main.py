#from scraper import scrape_reviews
from model_llm import summarize_review
from utils import clean_text
import pandas as pd

#URL = "https://www.amazon.in/product-reviews/B091HTLXL3/ref=cm_cr_dp_d_show_all_btm?ie=UTF8"

def main():
    #reviews = scrape_reviews(URL)
    print("Using sample data...")
    reviews = [
    {"text": "Great product, very fast delivery and works perfectly!", "rating": "5.0 out of 5 stars"},
    {"text": "Average quality, expected better for the price paid.", "rating": "3.0 out of 5 stars"},
    {"text": "Stopped working after 2 weeks. Very disappointed with quality.", "rating": "1.0 out of 5 stars"},
    {"text": "Absolutely love it! Best purchase I made this year.", "rating": "5.0 out of 5 stars"},
    {"text": "Decent product but packaging was damaged on arrival.", "rating": "3.0 out of 5 stars"},
]

    results = []

    for review in reviews:
        clean = clean_text(review["text"])
        summary = summarize_review(clean)


        results.append({
            "review": clean,
            "rating": review["rating"],
            "summary": summary
        })

    df = pd.DataFrame(results)
    df.to_csv("output.csv", index=False)

    print("Done! Check output.csv")

if __name__ == "__main__":
    main()