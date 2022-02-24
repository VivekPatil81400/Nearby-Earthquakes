from operator import le
import requests, json


api_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
response = requests.get(api_url)
data = response.text
parsed = json.loads(data)
all_data = parsed["features"]
lons, lats, title, id = [], [], [], []
for eq_dict in all_data:
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    title.append(eq_dict['properties']['title'])
    id.append(eq_dict['id'])

#print earthquake data closer to user location