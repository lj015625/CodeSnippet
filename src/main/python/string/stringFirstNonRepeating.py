""" Find first non repeating character in a string.  Return index of it or -1 if not exist."""
# O(n) time O(1) space
def firstNonRepeatingCharacter(string):
    charFreq = dict()
    for i, char in enumerate(string):
        charFreq[char] = charFreq.get(char, 0) + 1
        # if char in charFreq:
        #     charFreq[char] += 1
        # else:
        #     charFreq[char] = 1

    for i, char in enumerate(string):
        if charFreq[char] == 1:
            return i
    return -1


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "abcdcaf"
        expected = 1
        actual = firstNonRepeatingCharacter(input)
        self.assertEqual(expected, actual)
