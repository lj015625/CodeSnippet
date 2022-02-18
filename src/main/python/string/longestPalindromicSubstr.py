""" Find the longest Palindromic Substring.
"""


def isPalindromic(subStr):
    """
    subStr: str
    """
    palindromic = any([j == j[::-1] for j in subStr.split()])
    return palindromic


# O(n^3) time O(n) space. Use dynamic programming.
def longestPalindromicSubstring1(s):
    """
    s: str
    """
    # Get all substrings of string Using list comprehension + string slicing
    s_length = len(s)
    # res = [s[i:j] for i in range(s_length) for j in range(i + 1, s_length + 1)]
    dp = []
    maxLen = 0
    # saved longest palindrome
    longestPalindrome = ''
    for i in range(0, s_length):
        for j in range(s_length, i, -1):
            # print(s[i:j])
            if s[i:j] not in dp and isPalindromic(s[i:j]):
                dp.append(s[i:j])
                if j - i > maxLen:
                    longestPalindrome = s[i:j]
                    maxLen = j - i
    return longestPalindrome



# from inner to outer get the longest palindrome, leftIdx, rightIdx are the middle indexes
def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string) and string[leftIdx] == string[rightIdx]:
        leftIdx -= 1
        rightIdx += 1
    return string[leftIdx + 1: rightIdx]


# O(n^2) time O(n) space
def longestPalindromicSubstring2(s):
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        odd = getLongestPalindromeFrom(s, i, i)
        # even case, like "abba"
        even = getLongestPalindromeFrom(s, i, i + 1)
        res = max(res, odd, even, key=len)
    return res


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(longestPalindromicSubstring1("abaxyzzyxf"), "xyzzyx")

    def test_case_2(self):
        self.assertEqual(longestPalindromicSubstring2("abaxyzzyxf"), "xyzzyx")
