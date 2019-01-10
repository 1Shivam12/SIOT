# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 06:10:39 2019

@author: Shivam Bhatnagar
"""
import re
import csv
from textblob import TextBlob as tb

trows = []
sentiment = []
polarity = []
with open('saved_tweets.csv', 'r', encoding = "utf-8") as tweets:
    treader = csv.reader(tweets)
    for row in treader:
        trows.append(row)

def clean_tweet(tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 


for elem in trows:
    elem = str(elem)
    elemclean = clean_tweet(elem)
    elemtb = tb(elemclean)
    elemsent = elemtb.sentiment
    sentiment.append(elemsent)
    elempol = elemsent.polarity
    polarity.append(elempol)


