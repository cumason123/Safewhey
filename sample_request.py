import requests
import math

def test():
    params = (
        ('bottomLeftLat', '42.3545165'),
        ('bottomLeftLon', '-71.1263265'),
        ('topRightLat', '42.3548315'),
        ('topRightLon', '-71.1260115'),
        ('apikey', 'FfFYj6Z02qDq58tNnOySJKZqavjARqI9'),
    )

    response = requests.get('https://apis.solarialabs.com/shine/v1/total-home-scores/area-search', params=params)
    data = response.json()
    print(data)

def boundingRec(start, end):
    '''
    Draws bound rectangle given two coordinates

    :param start: arr of two values, 0 index meaning lat, 1 index meaning long
    :param end: arr of two values, 0 index meaning lat, 1 index meaning long

    '''
    lower_left_coordinate=[min(start[0], end[0]), min(start[1], end[1])]
    upper_right_coordinate = [max(start[0], end[0]), max(start[1], end[1])]

    length = (upper_right_coordinate[0] - lower_left_coordinate[0])
    width = (upper_right_coordinate[1] - lower_left_coordinate[1])

    area =  abs(length * width)

    return lower_left_coordinate, upper_right_coordinate, area

if __name__=='__main__':
    lower_left_coordinate, upper_right_coordinate, area=  boundingRec([-1,-3],[-3,-4])
    print('upper_right_coordinate: {0}'.format(upper_right_coordinate))
    print('lower_left_coordinate: {0}'.format(lower_left_coordinate))
    print('area: {0}'.format(area))
