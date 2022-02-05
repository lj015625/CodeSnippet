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

    queue = collections.deque([(beginWord, 1)])
    while queue:
        cur, level = queue.popleft()
        for i in range(len(cur)):
            for c in 'qwertyuiopasdfghjklzxcvbnm':
                trans = cur[:i] + c + cur[i + 1:]
                if trans in wordList:
                    queue.append((trans, level + 1))
                    wordList.remove(trans)
                    if trans == endWord:
                        return level + 1
    return 0


begin_word = "same"
end_word = "cost"
word_list = ["same", "came", "case", "cast", "lost", "last", "cost"]
print(shortest_transformation(begin_word, end_word, word_list))
