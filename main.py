from predict import analyze
import time, argparse, re

import pandas as pd

from scrape import scrape_reviews
from process import clean_reviews, process_reviews
from visualize import draw_cloud, draw_plot


def extract_data(merchant_no, product_no):
    print("수집 시작")
    REVIEWS = scrape_reviews(merchant_no, product_no)
    df = pd.DataFrame(REVIEWS)
    print("수집 끝")
    return df

def process_data(data_frame):
    print("전처리 시작")
    df = data_frame.drop_duplicates(['rate','date','raw']) # remove duplicates
    df = df.sort_values(by='date')
    cleaned_reviews = clean_reviews(df['raw'])
    processed_reviews = process_reviews(cleaned_reviews)
    df['reviews'] = processed_reviews
    print("전처리 끝")
    return df

def analyze_data(data):
    print("분석 시작")
    results = analyze(data)
    df = pd.DataFrame(results)
    print("분석 끝")
    return df

def visualize_data(data_frame):
    print("시각화 시작")
    # wordcloud
    draw_cloud(data_frame['reviews'])
    # sentiment analysis visualization
    draw_plot(data_frame)
    print("시각화 끝")
    return 0

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(
    #     description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    # )
    # parser.add_argument(
    #     "merchant_no"
    # )
    # parser.add_argument(
    #     "product_no"
    # )
    # args = parser.parse_args()

    df = extract_data('510048626','3219008568')
    df = process_data(df)
    score_df = analyze_data(df['reviews'])
    df = df.join(score_df)
    df.to_csv("result.csv", encoding='utf-8-sig', index=False)
    visualize_data(df)