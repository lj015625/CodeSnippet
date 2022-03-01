"""
Return whether the array is monotonic.  Monotonic array is either all increasing or all decreasing.
"""


def isMonotonic(array):
    if len(array) <= 2:
        return True

    trendIncreasing = None
    for i in range(1, len(array)):
        # check if trend is found
        if trendIncreasing is None:
            if array[i] < array[i - 1]:
                trendIncreasing = False
            elif array[i] > array[i - 1]:
                trendIncreasing = True
        else:
            if trendIncreasing:
                if array[i] < array[i - 1]:
                    return False
            else:
                if array[i] > array[i - 1]:
                    return False

    return True


# O(n) time O(1) space
def isMonotonic2(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False
    # use or logic
    return isNonDecreasing or isNonIncreasing


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
        expected = True
        actual = isMonotonic2(array)
        self.assertEqual(actual, expected)
