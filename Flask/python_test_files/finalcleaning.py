# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:22:22 2019

@author: Shivam Bhatnagar
"""

import csv
import json
from datetime import datetime, timedelta
from flask import Flask, render_template, url_for
app = Flask(__name__)

from statsmodels.tsa.seasonal import seasonal_decompose
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
with open('saved_tweetsv3.csv', 'r', encoding = "utf-8") as tweets:
    treader = csv.reader(tweets)
    for row in treader:
        trows.append(row)
        
trows = trows[0::2]

dates = []
avg_temp = []
hum = []
date =[]
time =[]
for col in trows:
    dates.append(col[-1])

for col in rows:
    avg_temp.append(col[0])
    hum.append(col[2])
    date.append(col[5])
    time.append(col[6]) 

timehum = pd.DataFrame(hum)
print(timehum.index)
hum = np.array(hum)
