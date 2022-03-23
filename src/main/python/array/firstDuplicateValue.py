"""
Given an array of numbers can only be 1 to n, inclusive, find the first duplicate value in
"""


# O(n) time O(n) space
def firstDuplicateValue(array):
    found = set()
    for n in array:
        if n in found:
            return n
        else:
            found.add(n)
    return -1


# O(n) time O(1) space
def firstDuplicateValue2(array):
    for i in array:
        # make it positive if it is negative
        positive = abs(i)
        # if it was negative then it is already found
        if array[positive - 1] < 0:
            return positive
        else:
            # make value at array index negative
            array[positive - 1] *= -1
    return -1


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = firstDuplicateValue(input)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        input = [2, 1, 1, 2, 3, 3, 4]
        expected = 1
        actual = firstDuplicateValue2(input)
        self.assertEqual(expected, actual)
