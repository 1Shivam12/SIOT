import requests
import json

# Make a get request to get the latest position of the international space station from the opennotify api.

parameters = {"lat": 40.71, "lon": -74, "alt": 5000} #Example lat, long of NYC at altitude of 5000m

response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)

data_1 = response.content


# JSON Example##########################

fplayers = ["messi", "ronaldo", "iniesta"] # List of player names, type python object

print(type(fplayers))

fp_string = json.dumps(fplayers) # Converted into a JSON String

print(type(fp_string))

print(type(json.loads(fp_string))) # Converted into a python list

p_age = {        
        "messi": 31,
        "ronaldo": 34,
        "iniesta": 34,
        }               # Take dictionary and convert to JSON string

p_age_string = json.dumps(p_age)

print(type(p_age_string))

# Handling the ISS Example with JSON Library

data_2 = response.json()
data_2 = json.dumps(data_2)
print(data_2)

#print(response.headers)

# Number of people in space right now
result = requests.get("http://api.open-notify.org/astros.json")
data_3 = result.json()
data_3 = json.dumps(data_3)
print(data_3)

