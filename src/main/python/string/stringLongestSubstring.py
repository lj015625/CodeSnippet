"""
Given a string finding the longest length substring in the string.
"""


def longestSubstringWithoutDuplication(string):
    seenChar = {}
    startIdx = 0
    longest = [0, 1]
    for currIdx, currChar in enumerate(string):
        # found repeating char
        if currChar in seenChar:
            # overwrite longest substring
            if currIdx - startIdx > longest[1] - longest[0]:
                longest = [startIdx, currIdx]

            # reset start pointer at previous repeated char's next char
            startIdx = seenChar[currChar] + 1
            seenChar = {k: v for k, v in seenChar.items() if v >= startIdx}

        # add char to map
        seenChar[currChar] = currIdx

    # the last iteration
    if len(string) - startIdx > longest[1] - longest[0]:
        return string[startIdx:]
    elif longest[1] - longest[0]:
        return string[longest[0]:longest[1]]


# O(n) time O(min(n,a)) space
def longestSubstringWithoutDuplication2(string):
    seenChar = {}
    startIdx = 0
    longest = [0, 1]
    for currIdx, currChar in enumerate(string):
        # found repeating char
        if currChar in seenChar:
            # find the next index of seen char after current startIdx
            # startIdx = max(startIdx, seenChar[currChar] + 1)
            if seenChar[currChar] + 1 > startIdx:
                startIdx = seenChar[currChar] + 1
        # overwrite longest substring with string[startIdx:currIdx+1]
        if currIdx + 1 - startIdx > longest[1] - longest[0]:
            longest = [startIdx, currIdx + 1]

        # add char to map
        seenChar[currChar] = currIdx

    return string[longest[0]:longest[1]]


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual("mentisac", longestSubstringWithoutDuplication("clementisacap"))
        self.assertEqual("abc", longestSubstringWithoutDuplication("abc"))
        self.assertEqual("abcdef", longestSubstringWithoutDuplication("abcdeabcdefc"))
        self.assertEqual("cbde", longestSubstringWithoutDuplication("abcbde"))
        self.assertEqual("cdea", longestSubstringWithoutDuplication("abccdeaabbcddef"))

    def test_case_2(self):
        self.assertEqual("mentisac", longestSubstringWithoutDuplication2("clementisacap"))
        self.assertEqual("abc", longestSubstringWithoutDuplication2("abc"))
        self.assertEqual("abcdef", longestSubstringWithoutDuplication2("abcdeabcdefc"))
        self.assertEqual("cbde", longestSubstringWithoutDuplication2("abcbde"))
        self.assertEqual("cdea", longestSubstringWithoutDuplication2("abccdeaabbcddef"))
