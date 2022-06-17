import requests

BASE = "http://numberapi.com"
k = ""
response = requests.get(BASE + "/2/6?json")
data = response.json()
for info in data["text"]:
    k = k + info
print(k)
