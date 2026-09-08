import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": 52.7666,
    "lon": -1.2039,
    "appid": API_KEY,
    "units": "metric"  # gives Celsius and m/s instead of Kelvin
}

response = requests.get(url, params=params)
data = response.json()
print(data)  # add this line temporarily
print(data["wind"])
print(data["main"]["temp"], data["main"]["humidity"])