from predict import analyze
import time, argparse, re

import pandas as pd

from scrape import scrape_reviews
from process import clean_reviews, process_reviews


def extract_data(merchant_no, product_no):
    REVIEWS = scrape_reviews(merchant_no, product_no)
    df = pd.DataFrame(REVIEWS)
    return df

def process_data(data_frame):
    print("start processing")
    df = data_frame.drop_duplicates(['rate','date','raw']) # remove duplicates
    cleaned_reviews = clean_reviews(df['raw'])
    processed_reviews = process_reviews(cleaned_reviews)
    df['reviews'] = processed_reviews
    return df

def analyze_data(data):
    print("start analyzing")
    results = analyze(data)
    df = pd.DataFrame(results)
    return df

def visualize_data(data):
    # wordcloud

    # sentiment analysis visualization

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
    print(df.head())
    score_df = analyze_data(df['reviews'])
    df = df.join(score_df)
    df.to_csv("result.csv")