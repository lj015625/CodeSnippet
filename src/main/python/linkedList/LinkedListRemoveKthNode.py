"""
Take head of the singly linked list and remove kth node from the list.
Assume at least k node.

Sample input:
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
k = 4

Sample output:
// 4the element from the end is removed which is 6
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    firstPointer = head
    secondPointer = head
    counter = 0
    while counter < k and secondPointer is not None:
        secondPointer = secondPointer.next
        counter += 1
    # edge case if list is smaller than k then we can remove the first value since kth element would be the head
    if secondPointer is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    # increment both first and second until second reach the end then k node between first and second
    while secondPointer.next is not None:
        firstPointer = firstPointer.next
        secondPointer = secondPointer.next

    # remove the first node
    firstPointer.next = firstPointer.next.next


import unittest

linkedListClass = LinkedList


class LinkedList(linkedListClass):

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = LinkedList(0).addMany([1, 2, 3, 4, 5, 7, 8, 9])
        removeKthNodeFromEnd(test, 4)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())
