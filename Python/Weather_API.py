# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 09:06:38 2019

@author: Shivam Bhatnagar
"""

import requests
import json
import csv
import datetime
import collections
from collections import OrderedDict

response = requests.get("http://api.openweathermap.org/data/2.5/weather?id=2643743&APPID=41e2e9ad43942f85fc31674e84585a45")
now = datetime.datetime.now()
date = str(now)[:10]
time = str(now)[11:19]

w_data = response.content.decode('utf-8')

wj_data = json.loads(w_data, object_pairs_hook=OrderedDict)


keys = list(wj_data.keys())   

    
vals = list(wj_data.values())

print('Raw vals are:' , vals)



main = vals[3]

print('Main vals are:', main)

main_data = list(main.values())


main_data.append(date)

main_data.append(time)

print('Main data is:', main_data)

with open('weather_file.csv', mode='a') as file:
    writer = csv.writer(file)
    writer.writerow(main_data)
