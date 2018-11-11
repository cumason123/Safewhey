import requests
import googlemaps
from datetime import datetime
import pprint
gmaps_key = "AIzaSyA-L1-CDamtVsUcngy65o54omBY_wn9TT0"
gmaps = googlemaps.Client(key = gmaps_key)

def getStartEndStepCoordinates(route):
	'''
	Finds and returns lat-long coordinates for every movement along 
	steps found through google maps api
	'''
	start = []
	end = []
	if 'legs' in route and 'steps' in route['legs'][0]:
		steps = route['legs'][0]['steps']
	else:
		return [], []
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

def getRouteValue(route):
	start, end = getStartEndStepCoordinates(route)
	vals = []
	toggle = True
	box = []
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

		if 'num_results_returned' in data:
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
				box += [{'north': upper_right_coordinate[1], 'south':lower_left_coordinate[1],
				'west': lower_left_coordinate[0], 'east':upper_right_coordinate[0], 'avg': vals[-1]}]
	if len(vals) == 0:
		return -1
	avgval = sum(vals)/len(vals)
	return {'avgval': avgval, 'box': box}


def getSomeRouteValues(start, end, max_num=3):
	if 'lat' in start:
		origin = str(start['lat']) + "," + str(start['lng'])
		dest = str(end['lat']) + "," + str(end['lng'])
	else:
		origin = str(start[0]) + "," + str(start[1])
		dest = str(end[0]) + "," + str(end[1])
	now = datetime.now()
	directions_result = gmaps.directions(origin, dest, 
		mode="walking", departure_time=now, alternatives=True)
	routeValues = []
	iter = 0
	routeBoxes = {}
	for route in directions_result:
		if iter > max_num:
			break
		num = getRouteValue(route)
		if num == -1:
			routeValues += ['Unknown']
		else:
			routeValues += [num['avgval']]
			routeBoxes[iter-1] = num['box']
		iter += 1
	iter += -1
	return routeValues, iter, routeBoxes

def SafeWhey(start_addr, dest_addr):
	try:
		start_coord = gmaps.geocode(start_addr)[0]['geometry']['location']
		end_coord = gmaps.geocode(dest_addr)[0]['geometry']['location']
	except:
		return {'err': 'unknown location'}
	ret = getSomeRouteValues(start_coord, end_coord)
	return {'safety_vals':ret[0], 
	'num_routes':ret[1], 'routeBoxes': ret[2]}

def boundRec(start, end):
	lower_left_coordinate = [min(start[0], end[0]), min(start[1], end[1])]
	upper_right_coordinate = [max(start[0], end[0]), max(start[1], end[1])]
	return lower_left_coordinate, upper_right_coordinate

if __name__ == '__main__':
	print(SafeWhey('16 winter ave', 'staten island technical highschool'))
	# testPoints([40.638982, -74.082301], [40.642608, -74.075460])
