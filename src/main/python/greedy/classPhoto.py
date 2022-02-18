"""
Given two arrays redShirtHeights and blueShirtHeights arrange rows such that
All students in red shirts must be in the same row.
All students in blue shirts must be in the same row.
Each student in back row must be taller than the student directly in front.
"""

# O(log(n)) time O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    if len(redShirtHeights) != len(blueShirtHeights):
        return False
    # sort in reverse order then start with tallest pairing up one from each front row and back row.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    if redShirtHeights[0] > blueShirtHeights[0]:
        for i, j in zip(redShirtHeights, blueShirtHeights):
            # if back row's tallest student is shorter than front row student then return false
            # because none of the other student will be taller than that.
            if i <= j:
                return False
    else:
        for i, j in zip(blueShirtHeights, redShirtHeights):
            if i <= j:
                return False

    return True


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        blueShirtHeights = [5, 6, 7, 2, 3, 1, 2, 3]
        redShirtHeights = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = True
        actual = classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)
