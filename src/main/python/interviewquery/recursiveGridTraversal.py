"""
Given an integer n, write a function traverse_count to determine the number of paths
from the top left corner of an nxn grid to the bottom right. You may only move right or down.
"""


def traverse_count(n):
    def recursive(i, j):
        if i == n - 1 and j == n - 1:
            return 1
        elif i >= n or j >= n:
            return 0

        return recursive(i, j + 1) + recursive(i + 1, j)

    return recursive(0, 0)


print(traverse_count(3))
