""" Longest Palindromic Substring
"""
# def isPalindromic(subStr):
#     """
#     subStr: str
#     """
#     palindromic = any([j == j[::-1] for j in subStr.split()])
#     return palindromic
#
# def longestPalindrome(s):
#     """
#     s: str
#     """
#     # Get all substrings of string Using list comprehension + string slicing
#     s_length = len(s)
#     # res = [s[i:j] for i in range(s_length) for j in range(i + 1, s_length + 1)]
#     dp = []
#     maxLen = 0
#     longestPalindrome = ''
#     for i in range(0, s_length):
#         for j in range(s_length, i, -1):
#             # print(s[i:j])
#             if s[i:j] not in dp and isPalindromic(s[i:j]):
#                 dp.append(s[i:j])
#                 if j-i > maxLen:
#                     longestPalindrome = s[i:j]
#                     maxLen = j-i
#     return longestPalindrome
#
# print(longestPalindrome("babad"))


def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

print(longestPalindrome("babad"))
