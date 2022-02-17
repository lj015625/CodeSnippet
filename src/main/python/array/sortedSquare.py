"""Take an array of sorted integers (including negative integers) and return squared array in sorted order. """


# O(n) time O(n) space
def sortedSquaredArray(array):
    sortedSquared = [None] * len(array)
    index = len(array) - 1
    beg = 0
    end = len(array) - 1
    while beg <= end:
        if abs(array[beg]) > abs(array[end]):
            sortedSquared[index] = array[beg] ** 2
            index -= 1
            beg += 1
        else:
            sortedSquared[index] = array[end] ** 2
            index -= 1
            end -= 1

    return sortedSquared


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [-5, -4, -3, -2, -1]
        expected = [1, 4, 9, 16, 25]
        actual = sortedSquaredArray(input)
        self.assertEqual(expected, actual)
