import googlemaps
from datetime import datetime
import pprint
gmaps_key = "AIzaSyA-L1-CDamtVsUcngy65o54omBY_wn9TT0"
gmaps = googlemaps.Client(key = gmaps_key)
now = datetime.now()

origin_lat = 42.346707
origin_long = -71.097074
dest_lat = 42.373486
dest_long = -71.120346

origin = str(origin_lat) + ", " + str(origin_long)
destination = str(dest_lat) + ", " + str(dest_long)

def create_directions_result():
    directions_result = gmaps.directions(origin, destination, mode="walking", alternatives=True)
    return directions_result

def create_directions_url(): # use to embed in webpage
    directions_url = "https://maps.google.com/maps/api/js?origin=" + origin + "&destination=" + destination + "&key=" + gmaps_key + "&callback=initMap"
    return directions_url

