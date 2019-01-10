# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:00:08 2018

@author: Shivam Bhatnagar
"""

# =============================================================================
# Package Imports
# =============================================================================

import csv
import json
from datetime import datetime, timedelta
from flask import Flask, render_template, url_for
from scipy import signal
app = Flask(__name__)

from pygal.style import Style
import pygal

import matplotlib.pyplot as plt

from sklearn import preprocessing
import numpy as np
import pandas as pd

from statsmodels.tsa.seasonal import seasonal_decompose
import random

import re
from textblob import TextBlob as tb

from nltk.tokenize import word_tokenize  # to split sentences into words
from nltk.corpus import stopwords  # to get a list of stopwords
from collections import Counter  # to get words-frequency
from nltk import FreqDist

from statistics import mean 
# =============================================================================
# Weather Data
# =============================================================================

rows = []
avg_temp = []
hum = []
date = []
time = []

with open('weather_file.csv', 'r') as weather:
    reader = csv.reader(weather)
    for row in reader:
        rows.append(row)

for col in rows:
    avg_temp.append(col[0])
    hum.append(col[2])
    date.append(col[5])
    time.append(col[6])  
    
for i in range(0,len(hum)):
    hum[i] = int(hum[i])
    
for i in range(0,len(avg_temp)):
    avg_temp[i] = float(avg_temp[i]) - 273.15    

timehum = pd.DataFrame(hum)

humpdseries = pd.Series(hum)
tempseries = pd.Series(avg_temp)
hum = np.array(hum)

sbhum = hum[-1]

humsc = preprocessing.scale(hum)

avg_temp = np.array(avg_temp)

sbtemp = avg_temp[-1]

avg_temp_sc = preprocessing.scale(avg_temp)


# =============================================================================
# Data Analysis within Weather
# =============================================================================
corr = np.corrcoef(humsc, avg_temp_sc)
corr = corr[0][1]
corr = round(corr,2)

autocorrlisthum = []
autocorrlisttemp = []
for i in range(1, len(hum)):
    autocorrlisthum.append(humpdseries.autocorr(lag = i))
for i in range(1, len(avg_temp)):
    autocorrlisttemp.append(tempseries.autocorr(lag = i))

crosscor = signal.correlate(humsc, avg_temp_sc)

   
# =============================================================================
# Twitter Data
# =============================================================================

trows = []
sentiment = []
polarity = []
with open('saved_tweetsv3.csv', 'r', encoding = "utf-8") as tweets:
    treader = csv.reader(tweets)
    for row in treader:
        trows.append(row)
trows = trows = trows[0::2]

def clean_tweet(tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

words = []
tweets = []
dates = []
days = []
for elem in trows:
    dates.append(elem[-1])
    elem = str(elem)
    elemclean = clean_tweet(elem)
    tweets.append(elemclean)
    elemtb = tb(elemclean)
    elemsent = elemtb.sentiment
    sentiment.append(elemsent)
    elempol = elemsent.polarity
    polarity.append(elempol)

polarity = list(filter(lambda a: a != 0, polarity))
pseries = pd.Series(polarity)
autocorrpol = []
for i in range(1, len(polarity)):
    autocorrpol.append(pseries.autocorr(lag = i))

crosscortwit = signal.correlate(humsc, polarity)

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

datetw = []
for dtime in dates:
    datetw.append(dtime[0:10])
    days.append(dtime[8:10])
    
bin1 = days.count('04')
bin2 = days.count('05')
bin3 = days.count('06')
bin4 = days.count('07')
bin5 = days.count('08')

# =============================================================================
# Actuation to determine state of twitter
# =============================================================================
imdb = {"marypop": 7.2,
        "aqua": 7.5,
        "bumblebee": 7.3,
        "spider": 8.7,
        "creed": 7.7,
        "stan":7.4
        }

imdblist = [7.2,7.5,7.3,8.7,7.7,7.4]

# Takes the avergae polarity for a given time frame in twitter
avpol = mean(polarity)

imlist = np.array(imdblist)

imlist = preprocessing.scale(imlist)

flaglist = avpol*imlist

thresh1 = 0
thresh2 = 0.2
 


# =============================================================================
# Flask App routing
# =============================================================================

@app.route("/")
@app.route("/Home")
def Home():   
    
    return render_template('home.html', title='SIOT', thresh1=thresh1, thresh2=thresh2, flaglist=flaglist, temp = round(sbtemp,2), hum=round(sbhum,2), pol=round(avpol,2))
@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/wordcloudpage")
def wordcloudpage():
    return render_template('wordcloudpage.html', title='Word Cloud')

@app.route("/twitter")
def twitter():
    custom_style = Style(
          background='transparent',
          plot_background='white')
    
    
    pie_chart = pygal.Pie(style=custom_style, legend_at_bottom=True)
    pie_chart.title = 'Most tweeted words in Data Set'
    pie_chart.add(str(mc[0][0]), wc1)
    pie_chart.add(str(mc[1][0]), wc2)
    pie_chart.add(str(mc[2][0]), wc3)
    pie_chart.add(str(mc[3][0]), wc4)
    pie_chart.add(str(mc[4][0]), wc5)
    pcdata = pie_chart.render_data_uri()
    
    
    bar_chart = pygal.Bar(style=custom_style, print_values=True, legend_at_bottom=True)
    bar_chart.title = 'Number of tweets per day'
    bar_chart.x_labels = ['2019-01-04', '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08']
    bar_chart.add('Twitter Data', [bin1, bin2, bin3, bin4, bin5])
    bardata = bar_chart.render_data_uri()   
    

    

   
    return render_template('twitter.html', title='Twitter API', graph1_data=pcdata, 
                           graph2_data =bardata,)

@app.route("/weather")
def weather():
    # Style of the pygal plots
    custom_style = Style(
      background='transparent',
      plot_background='white')
    
    wgraph = pygal.Line(legend_at_bottom=True)
    wgraph.title = "Time Series Analysis of Weather Data in London"
    wgraph.add("Humidity", humsc)
    wgraph.add("Average Temperature", avg_temp_sc)
    wgraph_data = wgraph.render_data_uri()
 
    return render_template('weather.html', title='Weather API', graph_data=wgraph_data, corr= corr)


@app.route("/analysis")
def analysis():
    custom_style = Style(
      background='transparent',
      plot_background='white')

    tgraph = pygal.Line(style=custom_style, legend_at_bottom=True)
    tgraph.title = "Autocorrelation functions for Weather Data"
    tgraph.add("Humidity Autocorrelation Function", autocorrlisthum)
    tgraph.add("Temperature Autocorrelation Function", autocorrlisttemp)
    tgraph_data = tgraph.render_data_uri()
    
    tgraph2 = pygal.Line(stroke=False, style=custom_style, legend_at_bottom=True)
    tgraph2.title = "Polarity of Tweets"
    tgraph2.add("Polarity", polarity)
    tgraph2_data = tgraph2.render_data_uri()
    
    tgraph3 = pygal.Line(style=custom_style, legend_at_bottom=True)
    tgraph3.title = "Autocorrelation function for Twitter Data"
    tgraph3.add("Polarity Autocorrelation Function", autocorrpol)
    tgraph3_data = tgraph3.render_data_uri()
    
    tgraph4 = pygal.Line(style=custom_style, legend_at_bottom=True)
    tgraph4.title = "Cross Correlation functions"
    tgraph4.add("Humidity vs Average Temperature" , crosscor)
    tgraph4.add("Twitter vs Humidity", crosscortwit)
    tgraph4_data = tgraph4.render_data_uri()
    
    

    return render_template('analysis.html',  line_data=tgraph2_data, graph_data=tgraph_data
                           , graph3_data = tgraph3_data,
                           graph4_data=tgraph4_data)
                         



@app.route("/word_cloud", methods=['GET'])
def word_cloud():
    words_json = [{'text': word, 'weight': count} for word, count in words_freq.items()]
    return json.dumps(words_json)

if __name__ == "__main__":
    app.run(debug=True)

    