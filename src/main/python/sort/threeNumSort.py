"""
Given two array. Sort the first array given the second array order.
If order is [x,y,z], then array will be sorted to [x,x,...x,y,y,...y,z,z,...z]
"""
from collections import Counter


# O(n) times | O(1) space
# easy to understand
def threeNumberSort1(array, order):
    # use a map of item and count
    valueCount = Counter(array)
    idx = 0
    for i in range(len(order)):
        value = order[i]
        count = valueCount[value]

        for j in range(count):
            array[idx + j] = value
        idx += count

    return array


# O(n) times | O(1) space
def threeNumberSort2(array, order):
    # move all first item to firstIndex and increment firstIndex
    firstIndex = 0
    for i in range(len(array)):
        if array[i] == order[0]:
            array[firstIndex], array[i] = array[i], array[firstIndex]
            firstIndex += 1

    # move all third item to thirdIndex and decrement thirdIndex
    thirdIndex = len(array) - 1
    # Traverse from last index to 0
    for j in range(len(array) - 1, -1, -1):
        if array[j] == order[2]:
            array[thirdIndex], array[j] = array[j], array[thirdIndex]
            thirdIndex -= 1

    return array


# O(n) times | O(1) space
def threeNumberSort3(array, order):
    # track sorted index of first items, second items, third items
    # both firstIndex and secondIndex start at 0
    firstIndex = 0
    secondIndex = 0
    thirdIndex = len(array) - 1

    while secondIndex <= thirdIndex:
        value = array[secondIndex]
        if value == order[0]:
            array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]
            firstIndex += 1
            secondIndex += 1
        elif value == order[1]:
            secondIndex += 1
        elif value == order[2]:
            array[thirdIndex], array[secondIndex] = array[secondIndex], array[thirdIndex]
            thirdIndex -= 1

    return array


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 0, 0, -1, -1, 0, 1, 1]
        order = [0, 1, -1]
        expected = [0, 0, 0, 1, 1, 1, -1, -1]
        actual = threeNumberSort1(array, order)
        self.assertEqual(expected, actual)
        array = [1, 0, 0, -1, -1, 0, 1, 1]
        actual = threeNumberSort2(array, order)
        self.assertEqual(expected, actual)
        array = [1, 0, 0, -1, -1, 0, 1, 1]
        actual = threeNumberSort3(array, order)
        self.assertEqual(expected, actual)
