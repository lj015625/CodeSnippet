"""
You’re given two words begin_word and end_word which are elements of word_list.
Write a function shortest_transformation to find the length of shortest transformation sequence
from begin_word to end_word through the elements of word_list.
Note that only one letter can be changed at a time and each transformed word in the list must exist.
"""
import collections


def shortest_transformation(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    wordList = set(wordList)

    if beginWord in wordList:
        wordList.remove(beginWord)

    # queue of word and level
    queue = collections.deque([(beginWord, 1)])
    while queue:
        word, level = queue.popleft()
        # two for loops replace each character with any of the alphabets
        for i in range(len(word)):
            for c in 'qwertyuiopasdfghjklzxcvbnm':
                # replace a character
                changeOneChar = word[:i] + c + word[i + 1:]
                # found a match
                if changeOneChar in wordList:
                    # add match to the queue
                    queue.append((changeOneChar, level + 1))
                    # remove found word. cannot repeat the same word
                    wordList.remove(changeOneChar)
                    if changeOneChar == endWord:
                        return level + 1
    return 0


begin_word = "same"
end_word = "cost"
word_list = ["same", "came", "case", "cast", "lost", "last", "cost"]
print(shortest_transformation(begin_word, end_word, word_list))
