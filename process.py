import re, time
from json.decoder import JSONDecodeError

import pandas as pd
from kss import split_sentences
from pykospacing import spacing
from hanspell import spell_checker
from soynlp.normalizer import repeat_normalize

def clean_reviews(reviews):
    cleaned_reviews = []
    for review in reviews:
        review = re.sub(r'\s+','', review)
        review = re.sub(r"^\s+", '', review) #remove space from start
        review = re.sub(r'\s+$', '', review) #remove space from the end
        cleaned_reviews.append(review)
    return cleaned_reviews

def process_reviews(reviews):
    processed_reviews = []
    for review in reviews:
        review = repeat_normalize(review, num_repeats=2) # normalize repeats by two
        review = spacing(review) # space by words
        review = ('.').join(split_sentences(review)) # split by sentence
        try:
            review = spell_checker.check(review).as_dict()['checked']
        except:
            print('pass')
            pass
        print(review)
        processed_reviews.append(review)
        time.sleep(0.5)
    return processed_reviews
