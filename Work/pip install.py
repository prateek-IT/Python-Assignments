import requests
base_url = "http://www.omdbapi.com/"

movie_name= input("Enter the movie title: ")

params = {
    "T": movie_name,
    "apikey": "d95bdd9a"
}

response = requests.get(base_url, params=params)
print(f"response in status : {response.status_code}")
print(response.json())