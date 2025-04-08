# Exercise
import requests


# 1. try another name
name = "David"
url = f"https://api.agify.io?name={name}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"\nExercise 1 - name:{data['name']}, Estimated age: {data['age']}, count: {data['count']}")

# 2. add countru parameter
url = f"https://api.agify.io?name=emma&country_id=ID"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"\nExercise 2 - name:{data['name']} (Indonesia), Estimated age: {data['age']}, count: {data['count']}")

#. 3 try genderize and nationalize apis
# Genderize API
gender_url = "https://api.genderize.io?name=emma"
gender_response = requests.get(gender_url)
if gender_response.status_code == 200:
    gender_data = gender_response.json()
    print(f"\nExercise 3 - Genderize: Name: {gender_data['name']}, Gender: {gender_data['gender']}, Probability: {gender_data['probability']}")

# Nationalize API
Nationalize_url = "https://api.nationalize.io?name=emma"
nationalize_response = requests.get(Nationalize_url)
if nationalize_response.status_code == 200:
    nationalize_data = nationalize_response.json()
    print(f"\nExercise 3 - Nationalize: Name: {nationalize_data['name']}, Country: {nationalize_data['country'][0]['country_id']}, Probability: {nationalize_data['country'][0]['probability']}")