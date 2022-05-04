import requests, json
import haversine as hs


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

lat1 = float(input("Enter latitude: "))
lon1 = float(input("Enter longitude: "))
loc1 = (lat1,lon1)
locs = []
for i in range(len(lons)):
    locs.append((lats[i], lons[i]))

dis = []
for loc2 in locs:
    dis.append(hs.haversine(loc1,loc2))

dis = [int(x) for x in dis]
    
dis, title = zip(*sorted(zip(dis, title)))

for i in range(0,9):
    print((title[i]) + " || "+ str(dis[i]))


