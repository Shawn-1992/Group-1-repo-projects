# imports request and json libraries
import requests
import json

# Select a new endpoint to send our PUT request to
ENDPOINT = "http://127.0.0.1:5000/colleges/UNC"

# Input the data we want to send
data_to_put = {"nickname": "Tar Holes"}

# Send PUT request to API
response = requests.put(ENDPOINT, json=data_to_put)

# Print the response from the server
print(response)

# Print the JSON data that we received back from the server
data = response.json()
print(json.dumps(data, indent=1))
