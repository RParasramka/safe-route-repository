import requests

response = requests.get("https://environment.data.gov.uk/flood-monitoring/id/floods")
data = response.json()

print(type(data))
print(data.keys())
print(data["items"][0])