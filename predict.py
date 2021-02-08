"""Demonstrates how to make a simple call to the Natural Language API."""
import time

from google.cloud import language_v1

def save_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    result = {
        'score': score,
        'magnitude': magnitude
    }
    print(result)
    return result

def analyze(reviews):
    results = []

    client = language_v1.LanguageServiceClient()

    for review in reviews:
        document = language_v1.Document(content=review, type_=language_v1.Document.Type.PLAIN_TEXT, language="ko")
        annotations = client.analyze_sentiment(request={'document': document})
        results.append(save_result(annotations))
        time.sleep(0.5)
    return results