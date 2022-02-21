"""
Given an array of integers and integer. Write a function move all instance of toMove integer to end of the array.
"""


# O(n) times | O(1) space
def moveElementToEnd(array, toMove):
    left, right = 0, len(array) - 1
    while left < right:
        # only move when left is target, right is not the target then swap.
        if toMove == array[left] and toMove != array[right]:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        else:
            # increments the pointer when left is not target, right is the target.
            if toMove != array[left]:
                left += 1
            if toMove == array[right]:
                right -= 1

    return array


# O(n) times | O(1) space
def moveElementToEnd2(array, toMove):
    left, right = 0, len(array) - 1
    while left < right:
        # find an index on the right to move
        while left < right and toMove == array[right]:
            right -= 1
        if toMove == array[left]:
            array[left], array[right] = array[right], array[left]
        left += 1

    return array


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        expectedStart = [1, 3, 4]
        expectedEnd = [2, 2, 2, 2, 2]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:3])
        outputEnd = output[3:]
        self.assertEqual(expectedStart, outputStart)
        self.assertEqual(expectedEnd, outputEnd)


    def test_case_2(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        expectedStart = [1, 3, 4]
        expectedEnd = [2, 2, 2, 2, 2]
        output = moveElementToEnd2(array, toMove)
        outputStart = sorted(output[0:3])
        outputEnd = output[3:]
        self.assertEqual(expectedStart, outputStart)
        self.assertEqual(expectedEnd, outputEnd)
