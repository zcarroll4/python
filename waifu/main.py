import requests


base_url = "https://waifu.it/api"
access_token = "NTU4MDE5MTQ0MTQzMDc3NDE4.MTczMTQ2OTgzOA--.197fc8dee94c"

url = f"{base_url}/v4/quote"
response = requests.get(url, headers={
        "Authorization" : access_token,
    })

data = response.json()

print(data["quote"])
print(f"-{data["author"]}")