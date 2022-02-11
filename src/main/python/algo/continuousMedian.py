""" Continuous update median using two HEAPs. """


def MAX_HEAP_FUNC(a, b):
    return a > b


def MIN_HEAP_FUNC(a, b):
    return a < b


class ContinuousMedianHandler:

    def __init__(self):
        # MAX_HEAP_FUNC to make it max heap where root is the maximum
        self.maxHeap = Heap(MAX_HEAP_FUNC, [])
        # MIN_HEAP_FUNC to make it max heap where root is the minimum
        self.minHeap = Heap(MIN_HEAP_FUNC, [])
        self.median = None

    # O(log(n)) time O(n) space
    def insert(self, number):
        if not self.maxHeap.length or number < self.maxHeap.peek():
            self.maxHeap.insert(number)
        else:
            self.minHeap.insert(number)
        self.rebalanceHeaps()
        self.updateMedian()

    def updateMedian(self):
        # even list
        if self.maxHeap.length == self.minHeap.length:
            self.median = (self.maxHeap.peek() + self.minHeap.peek()) / 2
        # odd list
        elif self.maxHeap.length > self.minHeap.length:
            self.median = self.maxHeap.peek()
        else:
            self.median = self.minHeap.peek()

    def rebalanceHeaps(self):
        # only re-balance if two heaps diff by 2
        if self.maxHeap.length - self.minHeap.length == 2:
            self.minHeap.insert(self.maxHeap.remove())
        elif self.minHeap.length - self.maxHeap.length == 2:
            self.maxHeap.insert(self.minHeap.remove())

    def getMedian(self):
        return self.median


class Heap:
    def __init__(self, comparisonFunc, array):
        self.comparisonFunc = comparisonFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in range(firstParentIdx + 1, 0, -1):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1:
                if self.comparisonFunc(heap[childTwoIdx], heap[childOneIdx]):
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
            else:
                idxToSwap = childOneIdx
            if self.comparisonFunc(heap[idxToSwap], heap[currentIdx]):
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0:
            if self.comparisonFunc(heap[currentIdx], heap[parentIdx]):
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1) // 2
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, self.length - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.length - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.length - 1, self.heap)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        handler = ContinuousMedianHandler()
        handler.insert(5)
        handler.insert(10)
        self.assertEqual(handler.getMedian(), 7.5)
        handler.insert(100)
        self.assertEqual(handler.getMedian(), 10)
