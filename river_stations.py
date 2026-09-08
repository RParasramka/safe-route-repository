import requests

# Get all monitoring stations with a river level/flow measure near Loughborough
url = "https://environment.data.gov.uk/flood-monitoring/id/stations"
params = {
    "lat": 52.7666,
    "long": -1.2039,
    "dist": 15  # search radius in km
}

response = requests.get(url, params=params)
data = response.json()

print(f"Found {len(data['items'])} stations nearby")
print(data["items"][0])  # look at the shape of one station's data
# Grab the measure IDs from the station data we just saw
flow_measure_url = "https://environment.data.gov.uk/flood-monitoring/id/measures/4074-flow--i-15_min-m3_s/readings"
level_measure_url = "https://environment.data.gov.uk/flood-monitoring/id/measures/4074-level-stage-i-15_min-mASD/readings"

params = {"latest": ""}  # gets just the most recent reading

flow_response = requests.get(flow_measure_url, params=params)
flow_data = flow_response.json()
print("Flow:", flow_data["items"])

level_response = requests.get(level_measure_url, params=params)
level_data = level_response.json()
print("Level:", level_data["items"])