"""
Traverse a N*M matrix and return a single dimensional array in spiral order.
Spiral order starts at top left goes to the right then down then left then up until all elements is traversed.
"""


# O(n) time O(n) space
def spiralTraverse(array):
    startRow, startCol = 0, 0
    endRow, endCol = len(array) - 1, len(array[0]) - 1

    result = []
    while startRow <= endRow and startCol <= endCol:
        # move right
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # move down
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # move left decrement from endCol - 1 to startCol
        for col in range(endCol - 1, startCol - 1, -1):
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        # move up decrement from endRow - 1 to startRow
        for row in range(endRow - 1, startRow, -1):
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        # after we done four loop time to increment or decrements all four pointers
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result


# recursive same implementation
def spiralTraverse2(array):
    result = []
    startRow, startCol = 0, 0
    endRow, endCol = len(array) - 1, len(array[0]) - 1
    spiralRecursive(array, startRow, endRow, startCol, endCol, result)
    return result


def spiralRecursive(array, startRow, endRow, startCol, endCol, result):
    if startRow > endRow or startCol > endCol:
        return

    # move right
    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])

    # move down
    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])

    # move left
    for col in range(endCol - 1, startCol - 1, -1):
        if startRow == endRow:
            break
        result.append(array[endRow][col])

    # move up
    for row in range(endRow - 1, startRow, -1):
        if startCol == endCol:
            break
        result.append(array[row][startCol])

    # after we done four loop time to increment or decrements all four pointers
    spiralRecursive(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 2, 3, 4],
                  [12, 13, 14, 5],
                  [11, 16, 15, 6],
                  [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(expected, spiralTraverse(matrix))

    def test_case_2(self):
        matrix = [[1, 2, 3, 4],
                  [10, 11, 12, 5],
                  [9, 8, 7, 6]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(expected, spiralTraverse(matrix))

    def test_case_3(self):
        matrix = [[1, 2, 3],
                  [12, 13, 4],
                  [11, 14, 5],
                  [10, 15, 6],
                  [9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(expected, spiralTraverse(matrix))

    def test_case_4(self):
        matrix = [[1, 2, 3, 4],
                  [12, 13, 14, 5],
                  [11, 16, 15, 6],
                  [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(expected, spiralTraverse2(matrix))
