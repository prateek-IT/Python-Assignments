import requests

base_url = "http://www.omdbapi.com/"

params = {"T": "main hoon na", "apikey": "d95bdd9a"}

response = requests.get(base_url, params=params)
print(response.text)
