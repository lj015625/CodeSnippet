"""Construct a min heap.  The parent value is smaller than child.  Heap array is not necessarily sorted. """
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # O(n) time O(1) space
    def buildHeap(self, array):
        lowestParentIdx = (len(array) - 2) // 2
        # print(*reversed(range(lowestParentIdx + 1)))
        for currentIdx in range(lowestParentIdx, -1, -1):
            # sift down check for all parents
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        # in an array left child index = current index * 2 + 1
        # right child index = current index * 2 + 2
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            # swap if one child if child is smaller than parent
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.__swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    # O(log(n)) time O(1) space
    def siftUp(self, currentIdx, heap):
        # in an array parent index = Math.floor((child index - 1) / 2)
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0:
            if heap[currentIdx] < heap[parentIdx]:
                self.__swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1) // 2
            else:
                return

    def peek(self):
        return self.heap[0]

    # # O(log(n)) time O(1) space
    def remove(self):
        self.__swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    # O(log(n)) time O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def __swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]


import unittest


def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False
    return True


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
        minHeap.insert(76)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), -5)
        self.assertEqual(minHeap.remove(), -5)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 2)
        self.assertEqual(minHeap.remove(), 2)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 6)
        minHeap.insert(87)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
