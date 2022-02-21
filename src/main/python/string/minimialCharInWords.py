"""
Return the smallest array of characters needed to form words.  Includes punctuations and/or special characters.
"""

from collections import Counter, defaultdict

# O(n * l) time and O(c) space.
# n is number of words, l is length of the longest word, c is number of unique characters across all words.
def minimumCharactersForWords(words):
    # use a hashmap of chars and frequencies.
    minChars = defaultdict(int)
    for word in words:
        wordChars = Counter(word)
        for char, count in wordChars.items():
            minChars[char] = max(count, minChars[char])

    charArray = []
    for key, count in minChars.items():
        charArray.extend([key] * count)

    return charArray


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["this", "that", "did", "deed", "them!", "a"]
        expected = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
        actual = minimumCharactersForWords(input)
        self.assertEqual(expected, actual)
