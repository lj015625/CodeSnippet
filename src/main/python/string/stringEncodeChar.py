"""
Encode a string AAAAAAAAAAAA(12A) as 9A3A. There are 9 'A's and 3 'A's.
"""


def runLengthEncoding(string):
    encoded = []
    prev = string[0]
    count = 1

    for i in range(1, len(string)):
        curr = string[i]
        prev = string[i - 1]
        # max of count of 9
        if curr != prev or count == 9:
            encoded.append(str(count) + prev)
            count = 0
        count += 1
    # the last iteration prev is not set in loop if string has only 1 char Get last character of string
    encoded.append(str(count) + string[-1])
    return ''.join(encoded)


def runLengthEncoding2(string):
    encoded = []
    prev = string[0]
    count = 1
    for curr in string[1:]:
        if curr != prev:
            # reset if a different char
            encoded.append(str(count) + prev)
            prev = curr
            count = 1
        elif count == 9:
            # reset if count is 9
            encoded.append(str(count) + prev)
            count = 1
        else:
            # increment count
            count += 1

    encoded.append(str(count) + prev)
    return ''.join(encoded)


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "AAAAAAAAAAAAABBCCCCDD"
        expected = "9A4A2B4C2D"
        actual = runLengthEncoding(string)
        self.assertEqual(expected, actual)
        actual = runLengthEncoding2(string)
        self.assertEqual(expected, actual)
