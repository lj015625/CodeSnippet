"""
Take an array of strings and group anagram together return an array.
"""

# O(w * n * log(n)) time O(wn) space where w is number of words and n is the length of the longest word
def groupAnagrams(words):
    wordsMap = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord not in wordsMap:
            wordsMap[sortedWord] = [word]
        else:
            wordsMap[sortedWord].append(word)
    # convert dict values to array then return it
    # [wordsMap[key] for key in wordsMap]
    return list(wordsMap.values())


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
        # sorted to keep the same order as expected
        output = list(map(lambda x: sorted(x), groupAnagrams(words)))

        self.compare(expected, output)

    def compare(self, expected, output):
        if len(expected) == 0:
            self.assertEqual(output, expected)
            return
        self.assertEqual(len(expected), len(output))
        for group in expected:
            self.assertTrue(sorted(group) in output)
