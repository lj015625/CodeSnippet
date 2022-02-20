"""
Find pair of number in two arrays with the smallest absolute difference between them.
"""


# O(n log(n) + m log(m)) time O(1) space  n is arrayOne length, m is arrayTwo length
def smallestDifference(arrayOne, arrayTwo):
    pair = []
    arrayOne.sort()
    arrayTwo.sort()
    oneIndex, twoIndex = 0, 0
    smallestDiff = abs(arrayOne[0] - arrayTwo[0])
    while oneIndex <= len(arrayOne) - 1 and twoIndex <= len(arrayTwo) - 1:
        diff = abs(arrayOne[oneIndex] - arrayTwo[twoIndex])
        if diff < smallestDiff:
            # zero is the smallest absolute diff
            if diff == 0:
                return [arrayOne[oneIndex], arrayTwo[twoIndex]]
            smallestDiff = diff
            pair = [arrayOne[oneIndex], arrayTwo[twoIndex]]

        if arrayOne[oneIndex] < arrayTwo[twoIndex]:
            oneIndex += 1
        else:
            twoIndex += 1

    return pair


def smallestDifference2(arrayOne, arrayTwo):
    pair = []
    arrayOne.sort()
    arrayTwo.sort()
    oneIndex, twoIndex = 0, 0
    smallestDiff = float("inf")
    while oneIndex < len(arrayOne) and twoIndex < len(arrayTwo):
        firstNum = arrayOne[oneIndex]
        secondNum = arrayTwo[twoIndex]
        if firstNum < secondNum:
            diff = secondNum - firstNum
            oneIndex += 1
        elif arrayOne[oneIndex] > arrayTwo[twoIndex]:
            diff = firstNum - secondNum
            twoIndex += 1
        else:
            # zero is the smallest absolute diff
            return [firstNum, secondNum]

        if smallestDiff > diff:
            smallestDiff = diff
            pair = [firstNum, secondNum]

    return pair

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])
        self.assertEqual(smallestDifference2([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])

