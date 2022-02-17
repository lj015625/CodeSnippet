"""
Check if characters can generate the document.
"""

from collections import defaultdict


# O(n+m) time
def generateDocument(characters, document):
    wordDict = defaultdict(int)
    for c in characters:
        wordDict[c] = wordDict[c] + 1

    for c in document:
        if wordDict[c] == 0:
            return False
        else:
            wordDict[c] = wordDict[c] - 1

    return True


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        characters = "Bste!hetsi ogEAxpelrt x "
        document = "AlgoExpert is the Best!"
        expected = True
        actual = generateDocument(characters, document)
        self.assertEqual(expected, actual)
