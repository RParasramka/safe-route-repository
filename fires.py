import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()  # reads your .env file
MAP_KEY = os.getenv("NASA_MAP_KEY")

# Bounding box below is roughly the UK: min_lon,min_lat,max_lon,max_lat
area_url = f'https://firms.modaps.eosdis.nasa.gov/api/area/csv/{MAP_KEY}/VIIRS_NOAA20_NRT/-10,49,2,61/3'
df = pd.read_csv(area_url)
print(df.head())
print(df.columns)
