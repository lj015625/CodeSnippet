"""
Encode a string AAAAAAAAAAAA(12A) as 9A3A.
"""


def runLengthEncoding(string):
    encoded = []
    prev = string[0]
    count = 1

    for i in range(1, len(string)):
        curr = string[i]
        prev = string[i - 1]

        if curr != prev or count == 9:
            encoded.append(str(count) + prev)
            count = 0

        count += 1

    encoded.append(str(count) + string[-1])
    return ''.join(encoded)

def runLengthEncoding2(string):
    encoded = []
    prev = string[0]
    count = 1
    for curr in string[1:]:
        if curr != prev:
            encoded.append(str(count) + prev)
            prev = curr
            count = 1
        elif count == 9:
            encoded.append(str(count) + prev)
            count = 1
        else:
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
