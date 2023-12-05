# imports request and json libraries
import requests
import json

# Select a new endpoint to send our PUT request to
ENDPOINT = "http://127.0.0.1:5000/colleges/UNC"

# Deletes UNC from the database and prints the server response
response = requests.delete(ENDPOINT)
print(response)

# Sends GET request to server and prints response
ENDPOINT = "http://127.0.0.1:5000/colleges"
response = requests.get(ENDPOINT)

# Prints the JSON data received from the GET request to verify that UNC has successfully been deleted
data = response.json()
print(json.dumps(data, indent=1))
