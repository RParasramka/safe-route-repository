import requests

url = "https://api.opentopodata.org/v1/srtm90m"
params = {
    "locations": "52.7666,-1.2039|52.7700,-1.2100|52.7600,-1.1900"
}

response = requests.get(url, params=params)
data = response.json()
print(data)
elevations = data["results"]
highest = max(elevations, key=lambda e: e["elevation"])
print(f"Highest point: {highest['location']}, elevation {highest['elevation']}m")