"""
You are given a list of lists where each group represents a friendship.

For example, given the list:

list = [[2,3],[3,4],[5]]
Person 2 is friends with person 3, person 3 is friends with person 4, etc.

Write a function to find how many friends each person has.
"""
from collections import defaultdict


def how_many_friends(relations):
    # dict of sets
    out = defaultdict(set)
    for r in relations:
        if len(r) > 1:
            for i in range(len(r)):
                for j in range(len(r)):
                    if i != j:
                        out[r[i]].add(r[j])
        else:
            out[r[0]] = set()
    return sorted([(key, len(values)) for key, values in dict(out).items()])


friends = [[1, 3], [2, 3], [3, 5], [4]]
print(how_many_friends(friends))
friends = [[1, 2, 3], [2, 3], [2, 3, 4], [4, 5], [4, 2]]
print(how_many_friends(friends))
