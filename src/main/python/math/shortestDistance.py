"""
Let’s say we have a group of N friends represented by a list of dictionaries
where each value is a friend name and their location on a three dimensional scale of (x, y, z).
The friends want to host a party but want the friend with the optimal location
(least distance to travel as a group) to host it.

Write a function pick_host to return the friend that should host the party.
"""
import sys
import math


def pick_host(friends):
    assert len(friends) > 0
    best_host = None
    best_cost = sys.maxsize

    for potential_host in friends:
        l = potential_host['location']

        cost = sum(math.sqrt((l[0] - person['location'][0]) ** 2 +
                             (l[1] - person['location'][1]) ** 2 +
                             (l[2] - person['location'][2]) ** 2) for person in friends)

        if cost < best_cost:
            best_cost = cost
            best_host = potential_host['name']

    return best_host


import numpy as np


def pick_host2(friends):
    # the best location for everyone is the centroid of all the points in 3-D space.
    centroid = sum(np.array(person['location']) for person in friends) * 1 / len(friends)
    best_dist = sys.maxsize
    best_host = None
    for p in friends:
        # we can loop through each friend and calculate the distance from the centroid,
        dist_to_center = sum((p['location'][i] - centroid[i]) ** 2 for i in range(3))
        if dist_to_center < best_dist:
            best_dist = dist_to_center
            best_host = p['name']
    return best_host


friends = [
    {'name': 'Bob', 'location': (5, 2, 10)},
    {'name': 'David', 'location': (2, 3, 5)},
    {'name': 'Mary', 'location': (19, 3, 4)},
    {'name': 'Skyler', 'location': (3, 5, 1)},
]
print(pick_host(friends))
print(pick_host2(friends))
