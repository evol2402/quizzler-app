question_data = []
import requests
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
data = response.json()

for key,value in data.items():
    if key =="results":
        question_data = value

