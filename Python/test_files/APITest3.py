# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 13:33:39 2018

@author: Shivam Bhatnagar
"""


# =============================================================================
# GUHAjTw17AGUss9kPzu8I9PNB (API key)

# UAyXIwrL1qKSUrB3WaBIlvbH7bYgloj2ejFs247JxcAGD5Rgs4 (API secret key

# 708230098-3kHy4jKQOemzA60pMT49flKPsaQh4XDAe6YnHzWX (Access token)

# oKo8ElBjZr6iuJQaDsMDHxm6BaHcqIO0uSEHLKiFxpB8p (Access token secret)
# =============================================================================

import json

credentials = {}
credentials['CONSUMER_KEY'] = 'GUHAjTw17AGUss9kPzu8I9PNB'
credentials['CONSUMER_SECRET'] = 'UAyXIwrL1qKSUrB3WaBIlvbH7bYgloj2ejFs247JxcAGD5Rgs4'
credentials['ACCESS_TOKEN'] = '708230098-3kHy4jKQOemzA60pMT49flKPsaQh4XDAe6YnHzWX'
credentials['ACCESS_SECRET'] = 'oKo8ElBjZr6iuJQaDsMDHxm6BaHcqIO0uSEHLKiFxpB8p'

with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)


