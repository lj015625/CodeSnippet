"""
Given a positive integer array find maximum sum of not adjacent numbers in the array.
"""


# O(n) time O(n) space
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    # use an array to store max sum at each index
    maxSumDp = [0] * len(array)
    maxSumDp[0] = array[0]
    maxSumDp[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        # either previous is bigger or i - 2
        maxSumDp[i] = max(maxSumDp[i - 1], maxSumDp[i - 2] + array[i])
    return maxSumDp[-1]


# O(n) time O(1) space
def maxSubsetSumNoAdjacent2(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
        # only store i-2 array index's max sum and i-1 array index's max sum as dp.
    prevprev = array[0]
    prev = max(prevprev, array[1])
    for i in range(2, len(array)):
        current = max(prev, prevprev + array[i])
        # iterate
        prevprev = prev
        prev = current
    return prev


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)

    def test_case_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent2([75, 105, 120, 75, 90, 135]), 330)
