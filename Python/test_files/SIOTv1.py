# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:44:54 2018

@author: Shivam Bhatnagar
"""

# =============================================================================
# ############## Package and other Imports#####################################
# =============================================================================
import requests
import json

# =============================================================================
# APPID=41e2e9ad43942f85fc31674e84585a45
# city key = 1273293 Delhi
# =============================================================================
# =============================================================================
# ############API CALL#########################################################
# =============================================================================






class weather:
    response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=1273293&APPID=41e2e9ad43942f85fc31674e84585a45")

    data = response.content
    
    data = json.loads(data)

  
    keys = list(data.keys())
    

    
    vals = list(data.values())
    

    
    
    mkeys = list(vals[3].keys())
    mvals = list(vals[3].values())
    
    def temp(self):
        print('The average ' + str(mkeys[0]) + ' is', str(mvals[0] - 273.15) + ' Celsius')
        
    def pressure(self):
        print('The average ' + str(mkeys[1]) + ' is', str(mvals[1]) + ' Pa')
        
    def hum(self):
        print('The average ' + str(mkeys[2]) + ' is', str(mvals[2]) + '%')
    
    def tempmin(self):
        print('The average ' + str(mkeys[3]) + ' is', str(mvals[3]-273.15) + ' Celsius')
        
    def tempmax(self):
        print('The average ' + str(mkeys[4]) + ' is', str(mvals[4] - 273.15) + ' Celsius')
        
        
delhi = weather()
delhi.temp()
delhi.hum()
delhi.pressure()