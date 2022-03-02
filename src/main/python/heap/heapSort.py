def heapSort(array):
    buildMaxHeap(array)
    for endIdx in range(len(array) - 1, -1, -1):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# O(n) time O(1) space
def buildMaxHeap(array):
    lowestParentIdx = (len(array) - 2) // 2
    # print(*reversed(range(lowestParentIdx + 1)))
    for currentIdx in range(lowestParentIdx, -1, -1):
        # sift down check for all parents
        siftDown(currentIdx, len(array) - 1, array)
    return array


# O(log(n)) time O(1) space
def siftDown(currentIdx, endIdx, heap):
    # in an array left child index = current index * 2 + 1
    # right child index = current index * 2 + 2
    childOneIdx = currentIdx * 2 + 1
    # if child is not leaf
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        # swap smaller child with parent
        if childTwoIdx != -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(heapSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])
