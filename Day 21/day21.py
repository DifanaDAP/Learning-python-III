# Day 21 : Requests API Handilng
import requests

# 1. Send a get request to a public api

url = "https://api.agify.io?name=michael"
response = requests.get(url)

# 2. Check status and parse json data
if response.status_code == 200:
    data = response.json()
    print("API Result:")
    print(f"Name: {data['name']}")
    print(f"Etimated Age:{data['age']}")
    print(f"Sample size: {data['count']}")
else:
    print("Failed to fetch data from API")