import requests

ENDPOINT = "http://127.0.0.1:5000/colleges"
data_to_post = {'name': 'North Carolina Central University', 'abbreviation': 'NCCU', 'year_founded': 1910, 'nickname': 'Eagles'}
response = requests.post(ENDPOINT, json = data_to_post)
print(response)

data = response.json()
print(data)


response = requests.get(ENDPOINT)
print(response)

data = response.json()
print(data)

ENDPOINT = "http://127.0.0.1:5000/colleges/UNC"
data_to_put = {"nickname": "Tar Holes"}
response = requests.put(ENDPOINT, json=data_to_put)
print(response)

data = response.content
print(data)

response = requests.delete(ENDPOINT)
print(response)

ENDPOINT = "http://127.0.0.1:5000/colleges"
response = requests.get(ENDPOINT)
print(response)

data = response.json()
print(data)
