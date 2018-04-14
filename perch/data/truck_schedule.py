import datetime
import random
import json

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
                {
                    "coord": [33.9885892996, -118.471458908]
                },
                {
                    "coord": [33.9885892996, -118.471458908]
                },
                {
                    "coord": [33.9885892996, -118.471458908]
                },
                {
                    "coord": [33.9885892996, -118.471458908]
                },
                {
                    "coord": [33.9885892996, -118.471458908]
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


if __name__ == '__main__':
    points = [generate_random_point_in_bounds(min_lat, min_lon, max_lat, max_lon) for _ in range(40)]
    geojson = geojson_for_points(points)
    print json.dumps(geojson, indent=4)
