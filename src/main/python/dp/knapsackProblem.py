"""
Given an array of arrays where each subarray hold two integer values represent an item.
The first value is item's value, the second value is item's weight.
You are also given maximum capacity.
Your goal is find maximum combined value of items without exceed capacity.
"""


def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]
        for c in range(capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue)
    return [knapsackValues[-1][-1], getKnapsackValues(knapsackValues, items)]


def getKnapsackValues(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        expected = [10, [1, 3]]
        self.assertEqual(expected, knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))
