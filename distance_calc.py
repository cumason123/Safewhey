import googlemaps
from datetime import datetime
import pprint
gmaps_key = "AIzaSyA-L1-CDamtVsUcngy65o54omBY_wn9TT0"
gmaps = googlemaps.Client(key = gmaps_key)
now = datetime.now()

def gen(start_coord, end_coord):
	origin = str(start_coord[0]) + "," + str(start_coord[1])
	dest = str(end_coord[0]) + "," + str(end_coord[1])
	directions_result = gmaps.directions(origin, dest, 
		mode="walking", departure_time=now)
	steps = directions_result[0]['legs'][0]['steps']
	for step in steps:
		start = [step['start_location']['lat'], step['start_location']['lng']] if 'start_location' in step else None
		end = [step['end_location']['lat'], step['end_location']['lng']] if 'end_location' in step else None
		print(start)
		print(end)
		print()


if __name__ == '__main__':
	origin_lat = 40.638982
	origin_long = -74.082301

	dest_lat = 40.642608
	dest_long = -74.075460
	gen([origin_lat, origin_long], [dest_lat, dest_long])
