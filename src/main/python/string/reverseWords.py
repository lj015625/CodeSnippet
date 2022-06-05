# O(N) time O(N) space
def reverseWordsInString(string):
    reversedWords = []
    # reverse the whole string
    for word in string[::-1].split(' '):
        # re-reverse the word
        reversedWords.append(word[::-1])
    return " ".join(reversedWords)


# O(N) time O(N) space  at character level
def reverseWordsInString2(string):

    def reverseList(l):
        start, end = 0, len(l) - 1
        while start < end:
            l[start], l[end] = l[end], l[start]
            start += 1
            end -= 1

    words = []
    startOfWord = 0
    # break up string to words
    for idx in range(len(string)):
        char = string[idx]
        if char == " ":
            words.append(string[startOfWord:idx])
            # reset startOfWord to idx
            startOfWord = idx
        # skip empty spaces
        elif string[startOfWord] == " ":
            words.append(" ")
            startOfWord = idx
    # one last iteration
    words.append(string[startOfWord:])
    # reverse the words
    reverseList(words)
    return "".join(words)

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "AlgoExpert is the best!"
        expected = "best! the is AlgoExpert"
        actual = reverseWordsInString(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = "AlgoExpert is the best!"
        expected = "best! the is AlgoExpert"
        actual = reverseWordsInString2(input)
        self.assertEqual(actual, expected)
