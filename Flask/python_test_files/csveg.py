# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:03:40 2019

@author: Shivam Bhatnagar
"""

import csv
rows = []
avg_temp = []
hum = []
date = []
time = []

with open('weather_file.csv', 'r') as weather:
    reader = csv.reader(weather)
    for row in reader:
        rows.append(row)

print(rows)

for col in rows:
    avg_temp.append(col[0])
    hum.append(col[2])
    date.append(col[5])
    time.append(col[6])
    
    
for i in range(0,len(hum)):
    hum[i] = int(hum[i])
    
for i in range(0,len(avg_temp)):
    avg_temp[i] = int(avg_temp[i])
    
for i in range(0,len(date)):
    date[i] = int(date[i])
    
for i in range(0,len(time)):
    time[i] = int(time[i])
    
