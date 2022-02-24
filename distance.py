from math import radians
from earthquakes_all import lons, lats, title
import haversine as hs


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

