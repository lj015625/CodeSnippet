# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Hint linked List is sorted O(n) time O(1) space
def removeDuplicatesFromLinkedList(node):
    currentNode = node
    while currentNode is not None:
        # starting at next node and find a duplicate then skip it
        temp = currentNode.next
        while temp is not None and temp.value == currentNode.value:
            temp = temp.next
        # set pointer to found duplicate
        currentNode.next = temp

        # restart from duplicate
        currentNode = temp

    return node


import unittest


class LinkedList(LinkedList):
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
        test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        expected = LinkedList(1).addMany([3, 4, 5, 6])
        actual = removeDuplicatesFromLinkedList(test)
        self.assertEqual(actual.getNodesInArray(), expected.getNodesInArray())
