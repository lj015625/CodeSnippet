"""
Write a class for Min Max Stack.
Pushing and Popping value from the stack;
Peeking value at top of the stack;
Getting both minimum and maximum value in the stack at any time.
"""
from collections import deque


class MinMaxStack:

    def __init__(self):
        # doubly linked list deque is more efficient to implement large sized stack
        self.minMaxStack = deque()

    # O(1) time O(1) space
    def peek(self):
        return self.minMaxStack[-1]['number']

    # O(1) time O(1) space
    def pop(self):
        return self.minMaxStack.pop()['number']

    # O(1) time O(1) space
    def push(self, number):
        # default min and max to current number when stack is empty
        currMinMax = {'min': number, 'max': number, 'number': number}
        if len(self.minMaxStack) > 0:
            lastMinMax = self.minMaxStack[-1]
            currMin = min(number, lastMinMax['min'])
            currMax = max(number, lastMinMax['max'])
            currMinMax = {'min': currMin, 'max': currMax, 'number': number}
        self.minMaxStack.append(currMinMax)

    # O(1) time O(1) space
    def getMin(self):
        lastItem = self.minMaxStack[-1]
        return lastItem['min']

    # O(1) time O(1) space
    def getMax(self):
        lastItem = self.minMaxStack[-1]
        return lastItem['max']


import unittest


def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stack = MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)
