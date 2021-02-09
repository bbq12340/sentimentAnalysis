# -*- coding: utf-8 -*-
from collections import Counter
import random
from konlpy.tag import Hannanum
from stylecloud import gen_stylecloud
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd

def draw_cloud(reviews):
    tags = {}
    # r = lambda: random.randint(0,255)
    # color = lambda: (r(), r(), r())
    for review in reviews:
        h = Hannanum()
        nouns = h.nouns(review)
        count = dict(Counter(nouns))
        tags = {k: tags.get(k, 0) + count.get(k, 0) for k in set(tags) | set(count)}
    gen_stylecloud(text=tags, 
                    output_name="wordcloud.png", 
                    icon_name="fas fa-square-full",
                    background_color="white", 
                    font_path="Jua-Regular.ttf", 
                    size=1024)

def draw_plot(data_frame):
    sns.set_theme()

    data_frame['date'] = pd.to_datetime(data_frame['date'], format='%Y-%m-%d')
    data_frame['sentiment'] = (data_frame['score'].round(3))*(df['magnitude'].round(3))
    plot = sns.scatterplot(data=data_frame, x='date', y='sentiment', hue='rate', palette="deep", s=10)
    plot.set(xlabel='Date', ylabel='Sentiment', ylim=[-3, 3])
    plot.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    plot.figure.savefig('sentiment.png')
