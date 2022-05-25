"""
Given an array of numbers return all subsets.
For example, [1,2]'s subset is [[], [1], [2], [1,2]].
"""


# Iterative O(2^n *n) time O(2^n *n) space
def powerset(array):
    subsets = [[]]
    for num in array:
        # for each existing subsets add a new element to it
        for j in range(len(subsets)):
            currentSubset = subsets[j]
            subsets.append(currentSubset + [num])
    return subsets


# Recursive O(2^n *n) time O(2^n *n) space
def powerset_recursive(array, index=None):
    if index is None:
        index = len(array) - 1
    if index < 0:
        return [[]]
    num = array[index]
    # powerset([1,2,3,4,...x]) = powerset([1,2,3,4,...x-1]) + [x], therefore add [x] to each subsets
    subsets = powerset_recursive(array, index - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [num])
    return subsets

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = list(map(lambda x: set(x), powerset([1, 2, 3])))
        self.assertTrue(len(output) == 8)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)
        self.assertTrue(set([3]) in output)
        self.assertTrue(set([1, 3]) in output)
        self.assertTrue(set([2, 3]) in output)
        self.assertTrue(set([1, 2, 3]) in output)

    def test_case_2(self):
        output = list(map(lambda x: set(x), powerset_recursive([1, 2, 3])))
        self.assertTrue(len(output) == 8)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)
        self.assertTrue(set([3]) in output)
        self.assertTrue(set([1, 3]) in output)
        self.assertTrue(set([2, 3]) in output)
        self.assertTrue(set([1, 2, 3]) in output)
