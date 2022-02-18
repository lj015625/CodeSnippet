"""
Given two lists of speeds. tandem_speed = max(speedA, speedB).
Pair one blue shirt with one red shirt and maximum total speed.
"""

# O(log(n)) time O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if len(redShirtSpeeds) != len(blueShirtSpeeds):
        return -1
    # sort in reverse order then start with tallest pairing up one from each front row and back row.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)

    sumOfSpeed = 0
    for i, j in zip(redShirtSpeeds, blueShirtSpeeds):
        sumOfSpeed += max(i, j)

    return sumOfSpeed


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        redShirtSpeeds = [5, 5, 3, 9, 2]
        blueShirtSpeeds = [3, 6, 7, 2, 1]
        fastest = True
        expected = 32
        actual = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
        self.assertEqual(actual, expected)
