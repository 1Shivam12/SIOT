# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 18:10:49 2019

@author: Shivam Bhatnagar
"""

import csv
import json
from datetime import datetime, timedelta
from flask import Flask, render_template, url_for
app = Flask(__name__)

from pygal.style import Style
import pygal

from sklearn import preprocessing
import numpy as np
from nltk import FreqDist
from random import randint

import pandas as pd

import re
from textblob import TextBlob as tb

from nltk.tokenize import word_tokenize  # to split sentences into words
from nltk.corpus import stopwords  # to get a list of stopwords
from collections import Counter  # to get words-frequency

trows = []
sentiment = []
polarity = []
date1 = '2019-1-4'
date2 = '2019-1-8'
mydates = pd.date_range(date1, date2).tolist() 

with open('saved_tweets.csv', 'r', encoding = "utf-8") as tweets:
    treader = csv.reader(tweets)
    for row in treader:
        flag = randint(0,len(mydates)-1)
        add = mydates[flag]
        row.append(add)
        trows.append(row)
        
print(trows)

with open('saved_tweetsv2.csv', 'w', encoding = "utf-8") as tweetsv2:
    a = csv.writer(tweetsv2, delimiter=',')
    a.writerows(trows)
    tweetsv2.close()
        

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

words = []
tweets = []
for elem in trows:
    elem = str(elem)
    elemclean = clean_tweet(elem)
# =============================================================================
#     for ec in elemclean:
#         ecs.append(ec)
#         tokens = word_tokenize(ec)
#         words.extend(tokens)
# =============================================================================
    tweets.append(elemclean)
    elemtb = tb(elemclean)
    elemsent = elemtb.sentiment
    sentiment.append(elemsent)
    elempol = elemsent.polarity
    polarity.append(elempol)
    
    

polarity = list(filter(lambda a: a != 0, polarity))

for tweet in tweets:
  tokens = word_tokenize(tweet)
  words.extend(tokens)    


stop_words = set(stopwords.words('english'))

words = [word for word in words if word not in stop_words and len(word)>3]

words_freq = Counter(words)

fdist = FreqDist(words)
mc = fdist.most_common(5)


lon = words.count('uk')


