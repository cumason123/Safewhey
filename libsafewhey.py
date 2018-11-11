import requests
import googlemaps
from datetime import datetime
import pprint
gmaps_key = "AIzaSyA-L1-CDamtVsUcngy65o54omBY_wn9TT0"
gmaps = googlemaps.Client(key = gmaps_key)
now = datetime.now()

def getStartEndStepCoordinates(start_coord, end_coord):
	'''
	Finds and returns lat-long coordinates for every movement along 
	steps found through google maps api
	'''
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


def testPoints(start, end):
	start, end = boundRec(start, end)
	params = (
		(
			('bottomLeftLat', start[0]),
			('bottomLeftLon', start[1]),
			('topRightLat', end[0]),
			('topRightLon', end[1]),
			('apikey', 'FfFYj6Z02qDq58tNnOySJKZqavjARqI9'),
		)
	)
	response = requests.get('https://apis.solarialabs.com/shine/v1/total-home-scores/area-search',
		params = params)
	data = response.json()
	print(data)

def getAreaVal(start, end):
	start, end = getStartEndStepCoordinates(start, end)
	vals = []
	for i in range(len(start)):
		lower_left_coordinate, upper_right_coordinate = boundRec(start[i], end[i])
		params = (
			(
				('bottomLeftLat', str(lower_left_coordinate[0])),
				('bottomLeftLon', str(lower_left_coordinate[1])),
				('topRightLat', str(upper_right_coordinate[0])),
				('topRightLon', str(upper_right_coordinate[1])),
				('apikey', 'FfFYj6Z02qDq58tNnOySJKZqavjARqI9'),
			)
		)
		response = requests.get('https://apis.solarialabs.com/shine/v1/total-home-scores/area-search',
			params = params)
		data = response.json()
		if data['num_results_returned'] > 0:
			results = data['results']
			subresult = 0
			for item in results:
				totalHomeScores = item['totalHomeScores']['safety']
				valueSum = 0
				for key in totalHomeScores:
					valueSum += totalHomeScores[key]['value']
				valueSum = valueSum/len(totalHomeScores)
				subresult += valueSum
			vals += [subresult/data['num_results_returned']]
	avgval = sum(vals)/len(vals)
	return avgval

def boundRec(start, end):
	lower_left_coordinate = [min(start[0], end[0]), min(start[1], end[1])]
	upper_right_coordinate = [max(start[0], end[0]), max(start[1], end[1])]
	return lower_left_coordinate, upper_right_coordinate

if __name__ == '__main__':
	print(getAreaVal([42.3509, -71.108852], [42.349359, -71.09612]))
	# testPoints([40.638982, -74.082301], [40.642608, -74.075460])


