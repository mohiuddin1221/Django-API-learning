import requests

URL = "https://fakestoreapi.com/products"

response = requests.get(url=URL)
data = response.json()
print(data)
