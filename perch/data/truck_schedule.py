import datetime
import random
import json
import math

test_schedule = {
    "trucks": [
        {
            "truck_name": "Truck 1",
            "stops": [
                {
                    "lat": 31,
                    "lon": 41,
                    "arrival": 1,
                    "departure": 1
                },
            ]
        },

    ]
}

max_lat = 34.060134
min_lat = 33.985593
max_lon = -118.472203
min_lon = -118.310396


def generate_fake_trucks():
    pass


def generate_fake_stops():
    pass


def generate_random_point_in_bounds(min_x, min_y, max_x, max_y):
    return [random.uniform(min_x, max_x), random.uniform(min_y, max_y)]


def geojson_for_points(points, reverse=True):
    features = []
    for point in points:
        if reverse:
            point = point[::-1]
        feature = {
            "type": "Feature",
            "properties": {
                "_id": "{},{}".format(point[1], point[0]),
            },
            "geometry": {
                "type": "Point",
                "coordinates": point
            }
        }
        features.append(feature)
    geo_json = {
        "type": "FeatureCollection",
        "features": features
    }
    return geo_json


def generate_chain_of_points(points, chain_length=5):
    start_point = random.choice(points)
    chain = [start_point]
    for i in range(chain_length):
        chain.append(find_closest_point(start_point, points, chain))
    return chain


def find_closest_point(cur_point, all_points, excluded_points):
    closet_point = None
    closet_dist = 0
    for point in all_points:
        if any([set(p) == set(point) for p in excluded_points]):
            continue
        dist = euclidean_distance(cur_point, point)
        if dist < closet_dist or closet_point is None:
            closet_point = point
            closet_dist = dist
    return closet_point


def euclidean_distance(coord_1, coord_2):
    return math.sqrt((coord_1[0] - coord_2[0]) ** 2 + (coord_1[1] - coord_2[1]) ** 2)


def generate_route(chain_length=5, initial_points=40):
    points = [generate_random_point_in_bounds(min_lat, min_lon, max_lat, max_lon) for _ in range(initial_points)]
    return generate_chain_of_points(points, chain_length)


if __name__ == '__main__':
    _chain = generate_route(5, 40)
    geojson = geojson_for_points(_chain)
    print json.dumps(geojson, indent=4)
