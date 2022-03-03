"""
Given an array of arrays where each subarray hold two integer values represent an item.
The first value is item's value, the second value is item's weight.
You are also given maximum capacity.
Your goal is find maximum combined value of items without exceed capacity.
"""


# O(nc) time O(c) space where n is number of item, c is capacity
def knapsackProblem(items, capacity):
    # columns are [0, 1, 2...capacity + 1] capacity, rows are items
    knapsackValues = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]
    # iterate over each items
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]
        # iterate over each capacities
        for c in range(capacity + 1):
            # do no use this item
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            # use this item
            else:
                # max value from either replace with current item or not with current item
                knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue)
            # the final value of knapsackValues which is capacity
    return [knapsackValues[-1][-1], getKnapsackValues(knapsackValues, items)]


def getKnapsackValues(knapsackValues, items):
    sequence = []
    # start from the end and decrement
    i = len(knapsackValues) - 1
    # capacity
    c = len(knapsackValues[0]) - 1
    while i > 0:
        # current equal to previous row
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    # return order in descending
    return list(reversed(sequence))


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        expected = [10, [1, 3]]
        self.assertEqual(expected, knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))
