# MAP GENERATOR TEST, will be triggered by external view

import math
import json
import csv
import folium
from ubication import *
import ubication

# SUPPOSED PARAMETER VALUE OF RANGE (in meters)
SUPPOSEDRANGE = 5000000000

def coordenatesToMeters(latFrom, lonFrom, latTo, lonTo):
    latFrom = math.radians(latFrom)
    lonFrom = math.radians(lonFrom)
    latTo = math.radians(latTo)
    lonTo = math.radians(lonTo)
    earthRadius = 6371000
    latDelta = latTo - latFrom
    lonDelta = lonTo - lonFrom
    angle = 2 * math.asin(math.sqrt(math.pow(math.sin(lonDelta/2), 2) + math.cos(latFrom) * math.cos(latTo) * math.pow(math.sin(lonDelta / 2), 2)))
    return angle * earthRadius

def IsOnCircleList(lat, longit):
    for row in circleList:
        if (coordenatesToMeters(lat, longit, row["LAT"], row["LNG"]) <= SUPPOSEDRANGE):
            return True
    return False


map_mataro = folium.Map(location=[41.528514, 2.434395], zoom_start=14, width='95%', height='95%', position="relative") #tiles="cartodbpositron"

# If used w/ JSON:

#with open("territori_ussol.json", "r") as jsonFile:
#    data = json.load(jsonFile)

# Get it on CSV
with open('territori_ussol.csv', 'r') as f:
    next(f)
    data = csv.reader(f, delimiter=',')

    # Copy the JSON/CSV data from the external file to the full_list
    full_list = data

    # Forced examples:
    folium.Marker([41.532888, 2.429576], popup='<i>Laura Navarro</i>').add_to(map_mataro)
    folium.Marker([41.529033, 2.423450], popup='<b>Xavi Ortega</b>').add_to(map_mataro)


    ubication_list = ubication.get_ubicacions_zona_verda()
    for ubication in ubication_list:
        print("Nom: "+ubication.nom)
        folium.Marker([float(ubication.latitude), float(ubication.longitude)],
        popup = ubication.nom).add_to(map_mataro)



    # Get distance between to positions in meters:
    print(coordenatesToMeters(41.529033, 2.423450, 41.532888, 2.429576))

    # JUST TO SHOW IT -> Generate a circle:
    folium.CircleMarker(
        location=[41.532123, 2.4295456],
        radius=25,
        fill=True,
        popup=folium.Popup('inline explicit Popup')
    ).add_to(map_mataro)

    # WILL BE CALLED BY INCLUDED BY 'select_map.html'
    map_mataro.save('../../templates/layouts/folium_output.html')