from perch.utils.basics import unix_time_seconds
import datetime
import random
import json
import math


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


def generate_route1(chain_length=5, initial_points=40):
    # Santa monica area
    max_lat = 34.060134
    min_lat = 33.985593
    max_lon = -118.472203
    min_lon = -118.310396

    points = [generate_random_point_in_bounds(min_lat, min_lon, max_lat, max_lon) for _ in range(initial_points)]
    return generate_chain_of_points(points, chain_length)


def generate_route2(chain_length=5, initial_points=40):
    # Hawthorne area
    min_lat = 33.883134
    max_lat = 33.966694
    min_lon = -118.365959
    max_lon = -118.253633

    points = [generate_random_point_in_bounds(min_lat, min_lon, max_lat, max_lon) for _ in range(initial_points)]
    return generate_chain_of_points(points, chain_length)


def generate_arrival_departures(count, ensure_in_transit=False):
    pairs = []
    current_time = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    if ensure_in_transit:
        # We manually add the first point if we're ensuring in transit
        count -= 1
        pair = [current_time]
        # Increment 55 minutes so we know that they departed 5 minutes ago
        current_time += datetime.timedelta(minutes=55)
        pair.append(current_time)
        pairs.append(pair)
        # Increment for next arrival
        current_time += datetime.timedelta(minutes=random.randint(8, 25))

    for i in range(count):
        pair = [current_time]
        # Increment for departure
        current_time += datetime.timedelta(minutes=random.randint(30, 120))
        pair.append(current_time)
        pairs.append(pair)
        # Increment for next arrival
        current_time += datetime.timedelta(minutes=random.randint(8, 25))
    return pairs


def generate_truck_schedule(truck_count=5):
    trucks = []
    for i in range(truck_count):
        func = random.choice([generate_route1, generate_route2])
        chain = func(random.randint(3, 8), 40)
        if i + 1 == truck_count:
            times = generate_arrival_departures(len(chain), True)
        else:
            times = generate_arrival_departures(len(chain), True)
        stops = []
        for n in range(len(chain)):
            stops.append({
                "lat": chain[n][0],
                "lon": chain[n][1],
                "arrival": int(unix_time_seconds(times[n][0])),
                "departure": int(unix_time_seconds(times[n][1]))
            })
        trucks.append({
            "title": "Truck {}".format(i + 1),
            "stops": stops
        })

    return trucks


if __name__ == '__main__':
    # _chain = generate_route1(5, 40)
    # geojson = geojson_for_points(_chain)
    # print json.dumps(geojson, indent=4)
    print json.dumps(generate_truck_schedule(), indent=4)
