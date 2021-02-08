import time, re

from ReviewScraper import SmartStoreReviewScraper

def scrape_reviews(merchant_no, product_no):
    REVIEWS = []
    app = SmartStoreReviewScraper()
    # store_data = app.get_store_data(link) #스토어 정보 
    json_review = app.get_review_json(merchant_no, product_no, 1) #리뷰 정보 리퀘스트 
    review_data = app.get_review_data(json_review) #해당 아이템 리뷰 (총 아이템수 + 총 페이지수) 정보 
    total_elements = review_data['totalElements'] #총 아이템수
    content = app.get_review_content(json_review)
    app.scrape_review_contents(REVIEWS, content) #첫 페이지 크롤링
    p=2
    while len(REVIEWS) < total_elements:
        print(len(REVIEWS))
        json_review = app.get_review_json(merchant_no, product_no, p)
        content = app.get_review_content(json_review)
        app.scrape_review_contents(REVIEWS, content)
        p=p+1
        time.sleep(0.5)
        if len(REVIEWS) >= total_elements:
            break
    return REVIEWS