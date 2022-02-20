"""

"""
import re


def isValid(string):
    if len(string) == 0 or len(string) > 3:
        return False
        # check leading 0
    if re.match(r'[0][0-9]', string):
        return False
    if int(string) > 255:
        return False
    return True


def validIPAddresses(string):
    valid = []
    # use min to check on shorter length string and do not index error
    for i in range(1, min(4, len(string))):
        firstPart = string[0:i]
        # more efficient to break out of loop
        if not isValid(string[0:i]):
            continue
        for j in range(i+1, i + min(4, len(string) - i)):
            secondPart = string[i:j]
            if not isValid(string[i:j]):
                continue
            for k in range(j+1, j + min(4, len(string) - j)):
                thirdPart = string[j:k]
                fourthPart = string[k:]
                if isValid(string[j:k]) and isValid(string[k:]):
                    valid.append(firstPart + '.' + secondPart + '.' + thirdPart + '.' + fourthPart)

    return valid


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "3700100"
        expected = [
            "3.70.0.100", "37.0.0.100"
        ]
        actual = validIPAddresses(input)
        self.assertEqual(expected, actual)
