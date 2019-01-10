# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:39:04 2018

@author: Shivam Bhatnagar

Twitter Twython Streamer Class
"""
import json
from twython import TwythonStreamer  
import csv

# Load credentials from json file
with open("twitter_credentials.json", "r", encoding='utf-8') as file:  
    creds = json.load(file)

def process_tweet(tweet):  
    d = {}
#    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen_name']
    d['user_loc'] = tweet['user']['location']
    return d



class MyStreamer(TwythonStreamer):
    
    
    #Succesful data received
    def on_success(self, data):        
        # Only english tweets
        if data['lang'] == 'en':
            tweet_data = process_tweet(data)
            self.save_to_csv(tweet_data)
            
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()
        
    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))
        

stream = MyStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],  
                    creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'], timeout = 5)

# =============================================================================
# Keywords to track are:
# 1) Movies
# 2) Film
# 3) Cinema
# =============================================================================

stream.statuses.filter(track='movie, film, cinema')

