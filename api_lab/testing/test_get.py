# imports request and json libraries
import requests
import json

# determines where the POST request will be sent
ENDPOINT = "http://127.0.0.1:5000/colleges"

# Sends the GET request to the server and prints the response
response = requests.get(ENDPOINT)
print(response)

# Prints the JSON data sent back from the Flask server
data = response.json()
print(json.dumps(data, indent=1))
