# Sentiment Analysis

how it works

1. query an item in Naver shopping mall

2. scrape more than 1,000 reviews

3. process/clean the data
    - remove special characters (emoji maybe...)
    - remove duplicate (keys: date, rate, review)
    - remove english, digits
    - normalize repeated words (soynlp)
    - divide via words (PyKoSpacing)
    - divide via sentences (kss)
    - process by spellcheck (hanspell)


4. save it into csv

5. predict sentiment score
    - export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"

6. visualize
    - wordcloud (konlpy)
    - sentiment analysis scatter-plot (ggplot2)

# requirements
pandas
numpy
requests
bs4
konlpy
pykospacing
kss
hanspell
google-cloud-storage
google-cloud-language
