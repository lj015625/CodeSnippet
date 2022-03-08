"""
Take an array and return the length of the longest peak in the array.
A peak is at least three integers, the integer increasing until peak then all decreasing.
"""


# O(n) tine O(1) space
def longestPeak(array):
    if len(array) < 3:
        return 0
    prev = array[0]
    foundIncreasing = False
    foundDecreasing = False
    longestLen = 0
    currentLength = 1
    for curr in array[1:]:
        # increasing
        if curr > prev:
            # reset peak because it should be decreasing
            if foundDecreasing:
                longestLen = max(currentLength, longestLen)
                currentLength = 2
            else:
                currentLength += 1
            foundIncreasing = True
        # decreasing
        elif curr < prev:
            if foundIncreasing:
                if not foundDecreasing:
                    foundDecreasing = True
                currentLength += 1
        else:
            if foundIncreasing and foundDecreasing:
                longestLen = max(currentLength, longestLen)
            currentLength = 1
            foundIncreasing = False
            foundDecreasing = False

        # reassign prev to curr
        prev = curr
    # don't forget last iteration
    if foundIncreasing and foundDecreasing:
        longestLen = max(currentLength, longestLen)
    return longestLen


def longestPeak2(array):
    longestPeakLen = 0
    i = 1
    while i < len(array) - 1:
        # identify the peak only
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if isPeak:
            # extend to left to check all are decreasing
            leftIdx = i - 2
            while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
                leftIdx -= 1

            # extend to right to check all are increasing
            rightIdx = i + 2
            while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
                rightIdx += 1

            currentPeakLen = rightIdx - leftIdx - 1
            longestPeakLen = max(currentPeakLen, longestPeakLen)
            # start at end of rightIdx
            i = rightIdx
        else:
            i += 1

    return longestPeakLen


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(longestPeak(array), expected)
        self.assertEqual(longestPeak2(array), expected)

    def test_case_2(self):
        array = [1, 3, 2]
        expected = 3
        self.assertEqual(longestPeak(array), expected)
        self.assertEqual(longestPeak2(array), expected)

    def test_case_3(self):
        array = [5, 4, 3, 2, 1, 2, 1]
        expected = 3
        # self.assertEqual(longestPeak(array), expected)
        self.assertEqual(longestPeak2(array), expected)

    def test_case_4(self):
        array = [5, 4, 3, 2, 1, 2, 10, 12]
        expected = 0
        self.assertEqual(longestPeak(array), expected)
        self.assertEqual(longestPeak2(array), expected)

    def test_case_5(self):
        array = [1, 2, 3, 3, 2, 1]
        expected = 0
        self.assertEqual(longestPeak(array), expected)
        self.assertEqual(longestPeak2(array), expected)
