"""Given two strings, string1 and string2, write a function is_subsequence to find out if string1 is a subsequence of string2.
A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
"""
from collections import deque

def is_a_subSeq_b(a, b):
    queue = deque(list(a))
    i = queue.popleft()
    for j in b:
        if i == j:
            if len(queue) == 0:
                return True
            i = queue.popleft()
    return False

def is_subsequence(string1, string2):
    return is_a_subSeq_b(string2, string1) if len(string1) >= len(string2) else is_a_subSeq_b(string1, string2)






string1 = 'abc'
string2 = 'asbsc'
string3 = 'acedb'
print(is_subsequence(string1, string2))
print(is_subsequence(string1, string3))
