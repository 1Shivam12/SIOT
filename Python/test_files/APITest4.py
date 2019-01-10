# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:22:52 2018

@author: Shivam Bhatnagar

Example for a ONE-OFF TWITTER SEARCH
"""

from twython import Twython  
import json
import pandas as pd

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'movie',  
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        }

dict_= {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])
    
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)

print(df)