import requests

base_url = "https://bible-api.com/john 3:16"

response = requests.get(base_url)


data = response.json()

print(data["text"])
print(data["reference"])
