# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:39:28 2018

@author: Shivam Bhatnagar
"""

import requests
import json

response = requests.get("http://api.openweathermap.org/data/2.5/weather?id=2643743&APPID=41e2e9ad43942f85fc31674e84585a45")

data = response.content

#print(data)
    
data = json.loads(data)

  
keys = list(data.keys())   

    
vals = list(data.values())

print(vals[3])


