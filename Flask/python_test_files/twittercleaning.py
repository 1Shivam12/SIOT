# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:37:06 2019

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

import random

import re
from textblob import TextBlob as tb

from nltk.tokenize import word_tokenize  # to split sentences into words
from nltk.corpus import stopwords  # to get a list of stopwords
from collections import Counter  # to get words-frequency
from nltk import FreqDist


trows = []
sentiment = []
polarity = []
with open('saved_tweetsv2.csv', 'r', encoding = "utf-8") as tweets:
    treader = csv.reader(tweets)
    for row in treader:
        trows.append(row)

trows = trows[0::2]

def clean_tweet(tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

words = []
tweets = []
datetime = []
for elem in trows:
    dt = elem[3]
    datetime.append(dt)
    elem = str(elem)
    elemclean = clean_tweet(elem)
    tweets.append(elemclean)
    elemtb = tb(elemclean)
    elemsent = elemtb.sentiment
    sentiment.append(elemsent)
    elempol = elemsent.polarity
    polarity.append(elempol)

date = []
days = []
for dtime in datetime:
    date.append(dtime[0:10])
    days.append(dtime[8:10])

def sorting(x):
    splitup = x.split('-')
    return splitup[2], splitup[1], splitup[0]
sdate = sorted(date, key= sorting)

bin1 = days.count('04')
bin2 = days.count('05')
bin3 = days.count('06')
bin4 = days.count('07')
bin5 = days.count('08')

for row in trows:
    del row[-1]
    
for i in range(0,len(trows)):
    trows[i].append(sdate[i])
    

    
with open('saved_tweetsv3.csv', 'w', encoding = "utf-8") as tweetsv3:
    a = csv.writer(tweetsv3, delimiter=',')
    a.writerows(trows)
    tweetsv3.close()
    
polarity = list(filter(lambda a: a != 0, polarity))

for tweet in tweets:
  tokens = word_tokenize(tweet)
  words.extend(tokens)
  
stop_words = set(stopwords.words('english'))

words = [word for word in words if word not in stop_words and len(word)>2 ]

words_freq = Counter(words)

fdist = FreqDist(words)
mc = fdist.most_common(5)

wc1 = words.count(str(mc[0][0]))
wc2 = words.count(str(mc[1][0]))
wc3 = words.count(str(mc[2][0]))
wc4 = words.count(str(mc[3][0]))
wc5 = words.count(str(mc[4][0]))