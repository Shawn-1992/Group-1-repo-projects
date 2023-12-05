# imports request and json libraries
import requests
import json

# determines where the POST request will be sent
ENDPOINT = "http://127.0.0.1:5000/colleges"

# the data that will be sent to the API
data_to_post = {'name': 'North Carolina Central University', 'abbreviation': 'NCCU', 'year_founded': 1910,
                'nickname': 'Eagles'}

# sends the POST request and prints the response from the server
response = requests.post(ENDPOINT, json=data_to_post)
print(response)

# prints the json data info that was sent back from the server
data = response.json()
print(json.dumps(data, indent=1))
