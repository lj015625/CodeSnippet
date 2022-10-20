"""
Travelling Salesman Problem (TSP) : Given a set of cities and distances between every pair of cities,
the problem is to find the shortest possible route that visits every city exactly once
and returns to the starting point.
For example, consider the graph shown in the figure on the right side. A TSP tour in the graph is 1-2-4-3-1.
The cost of the tour is 10+25+30+15 which is 80.
The problem is a famous NP-hard problem. There is no polynomial-time known solution for this problem.
https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
"""
import unittest

from sys import maxsize
from itertools import permutations

V = 4


# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for edges in range(V):
        if edges != s:
            vertex.append(edges)

    # store minimum weight Hamiltonian Cycle
    min_dis = maxsize
    min_edge = None
    next_permutation = permutations(vertex)
    for edges in next_permutation:

        # store current Path weight(cost)
        current_dis = 0

        # compute current path weight
        k = s
        for j in edges:
            current_dis += graph[k][j]
            k = j
        current_dis += graph[k][s]

        # update minimum
        # min_path = min(min_path, current_pathweight)
        if current_dis < min_dis:
            min_dis = current_dis
            min_edge = edges

    return min_dis, min_edge


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        # matrix representation of graph distance to all nodes from current node
        graph = [[0, 10, 15, 20], [10, 0, 35, 25],
                 [15, 35, 0, 30], [20, 25, 30, 0]]
        starting = 0
        result_tuple = travellingSalesmanProblem(graph, starting)
        print("min total distance traveled: ", result_tuple[0])
        print("min total distance traveled edges: ", result_tuple[1])
