import requests
import googlemaps
from datetime import datetime

gmaps_key = "AIzaSyA-L1-CDamtVsUcngy65o54omBY_wn9TT0"
gmaps = googlemaps.Client(key = gmaps_key)
now = datetime.now()

def getStartEndStepCoordinates(start_coord, end_coord):
	origin = str(start_coord[0]) + "," + str(start_coord[1])
	dest = str(end_coord[0]) + "," + str(end_coord[1])
	directions_result = gmaps.directions(origin, dest, 
		mode="walking", departure_time=now)
	if 'legs' in directions_result[0] and 'steps' in directions_result[0]['legs'][0]:
		steps = directions_result[0]['legs'][0]['steps']
	else:
		return [], []
	start = []
	end = []
	for step in steps:
		start += [[step['start_location']['lat'], step['start_location']['lng']]] if 'start_location' in step else None
		end += [[step['end_location']['lat'], step['end_location']['lng']]] if 'end_location' in step else None
	return start, end

def getAreaVal(start, end):
	p1, p2 = boundRec(start, end)
	start, end = getStartEndStepCoordinates(start, end)
	for i in range(len(start)):
		lower_left_coordinate, upper_right_coordinate = boundRec(start[i], end[i])
		params = (
			(
				('bottomLeftLat', str(lower_left_coordinate[0])),
				('bottomLeftLon', str(lower_left_coordinate[1])),
				('topRightLat', str(upper_right_coordinate[0])),
				('topRightLon', str(upper_right_coordinate[1])),
				('apiKey', 'FfFYj6z02qDq58tNnOySJKZqavjARqI9'),
			)
		)
		response = requests.get('https://apis.solarislabs.com/shine/v1/total-home-scores/area-search',
			params = params)
		data = response.json()
		print(data)
		break

def boundRec(start, end):
	lower_left_coordinate = [min(start[0], end[0]), min(start[1], end[1])]
	upper_right_coordinate = [max(start[0], end[0]), max(start[1], end[1])]
	return lower_left_coordinate, upper_right_coordinate

if __name__ == '__main__':
	getAreaVal([40.638982, -74.082301], [40.642608, -74.075460])