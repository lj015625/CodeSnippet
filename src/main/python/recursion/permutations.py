"""
Returns array of permutations from the integers in array.
"""
import itertools as it


# Upper bound O(n^2*n!) time O(n*n!) space
# Avg O(n*n!) time O(n*n!) space
def getPermutations(array):
    if len(array) == 0:
        return [[]]
    return [list(tup) for tup in it.permutations(array)]


# O(n*n!) time O(n*n!) space
def getPermutations2(array):
    perms = []
    permutationsRecursive2(array, [], perms)
    return perms


def permutationsRecursive2(array, currentPerm, allPerms):
    # if array is empty then we have a permutation because we used all numbers
    if len(array) == 0 and len(currentPerm) > 0:
        allPerms.append(currentPerm)
    else:
        for i in range(len(array)):
            # remove item i from the array
            newArray = array[:i] + array[i + 1:]
            # add removed item to end of currentPerm
            newPerm = currentPerm + [array[i]]
            # call recursive function
            permutationsRecursive2(newArray, newPerm, allPerms)


# O(n*n!) time O(n*n!) space
def getPermutations3(array):
    permutations = []
    # start with current index at 0
    permutationsRecursive3(0, array, permutations)
    return permutations


def permutationsRecursive3(currIdx, array, allPerms):
    if currIdx == len(array) - 1:
        allPerms.append(array[:])
    else:
        for j in range(currIdx, len(array)):
            # swap current index with j
            swap(array, currIdx, j)
            # increment by currentIdx + 1
            permutationsRecursive3(currIdx + 1, array, allPerms)
            # swap back j and current index
            swap(array, currIdx, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        perms = getPermutations([1, 2, 3])
        self.assertTrue(len(perms) == 6)
        self.assertTrue([1, 2, 3] in perms)
        self.assertTrue([1, 3, 2] in perms)
        self.assertTrue([2, 1, 3] in perms)
        self.assertTrue([2, 3, 1] in perms)
        self.assertTrue([3, 1, 2] in perms)
        self.assertTrue([3, 2, 1] in perms)

    def test_case_2(self):
        perms = getPermutations2([1, 2, 3])
        self.assertTrue(len(perms) == 6)
        self.assertTrue([1, 2, 3] in perms)
        self.assertTrue([1, 3, 2] in perms)
        self.assertTrue([2, 1, 3] in perms)
        self.assertTrue([2, 3, 1] in perms)
        self.assertTrue([3, 1, 2] in perms)
        self.assertTrue([3, 2, 1] in perms)

    def test_case_3(self):
        perms = getPermutations3([1, 2, 3])
        self.assertTrue(len(perms) == 6)
        self.assertTrue([1, 2, 3] in perms)
        self.assertTrue([1, 3, 2] in perms)
        self.assertTrue([2, 1, 3] in perms)
        self.assertTrue([2, 3, 1] in perms)
        self.assertTrue([3, 1, 2] in perms)
        self.assertTrue([3, 2, 1] in perms)
