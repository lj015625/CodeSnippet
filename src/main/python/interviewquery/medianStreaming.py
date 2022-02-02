"""
Write a function get_stream_median to calculate the median from a stream of integers.
"""
from heapq import *
class MedianFinder:
    def __init__(self):
        self.maxh = []  # max heap for smaller half
        self.minh = []  # min heap for larger half

    def addNum(self, num):
        # if max-heap is empty or top element > given number
        if not self.maxh or (-1 * self.maxh[0] > num):
            # push number to max-heap (reverse sign)
            heappush(self.maxh, -1 * num)
        # otherwise
        else:
            # push number to min-heap
            heappush(self.minh, num)
        # if max-heap is too long
        if len(self.maxh) > len(self.minh) + 1:
            # push largest element to min-heap
            heappush(self.minh, -1 * heappop(self.maxh))
        # if min-heap is too long
        if len(self.minh) > len(self.maxh) + 1:
            # push smallest element to max-heap
            heappush(self.maxh, -1 * heappop(self.minh))

    def findMedian(self):
        # if two heaps are of equal length which means it is a even size list
        if len(self.maxh) == len(self.minh):
            # median is the mean of two middle values
            return float(self.minh[0] - self.maxh[0]) / 2.0
        # if max-heap is longer, median is its top element which means it is odd size list
        elif len(self.maxh) > len(self.minh):
            return float(-1 * self.maxh[0])
        # otherwise
        else:
            # median is smallest number in min heap
            return float(self.minh[0])


nums = [1, 2, 3, 4, 5, 6, 7]
stream = MedianFinder()
for i in nums:
    stream.addNum(i)
print(stream.findMedian())
stream.addNum(5)
print(stream.findMedian())
