"""
Write a function that takes in two strings and returns the
minimum number of edit operations (insert, delete, substitute) a char to obtain the second string.
"""


# O(nm) time | O(nm) space
def levenshteinDistance(str1, str2):
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    # [[0, 1, 2, 3, ...],
    #  [0, 1, 2, 3, ...],
    #  [0, 1, 2, 3, ...],
    #  [0, 1, 2, 3, ...],
    #  [0, 1, 2, 3, ...]]

    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            # if row and column matches then use left top diagonal value
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = min(edits[i - 1][j - 1], edits[i][j - 1], edits[i - 1][j]) + 1
    # returns bottom right value in the matrix
    return edits[-1][-1]


# O(nm) time | O(min(n,m) space
def levenshteinDistance2(str1, str2):
    smallStr = str1 if len(str1) < len(str2) else str2
    bigStr = str1 if len(str1) >= len(str2) else str2
    # only store last two rows
    evenEdits = [x for x in range(len(smallStr) + 1)]
    # [0, 1, 2, 3, ...]
    oddEdits = [None for x in range(len(smallStr) + 1)]
    # [None, None, None, None, ...]

    for i in range(1, len(bigStr) + 1):
        # swap last two rows
        if i % 2 == 1:  # odd
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:  # even
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i

        for j in range(1, len(smallStr) + 1):
            # if row and column matches then use left top diagonal value
            if bigStr[i - 1] == smallStr[j - 1]:
                currentEdits[j] = previousEdits[j - 1]
            else:
                currentEdits[j] = min(previousEdits[j - 1], previousEdits[j], currentEdits[j - 1]) + 1

    return evenEdits[-1] if len(bigStr) % 2 == 0 else oddEdits[-1]


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(levenshteinDistance("abc", "yabd"), 2)

    def test_case_2(self):
        self.assertEqual(levenshteinDistance2("abc", "yabd"), 2)
