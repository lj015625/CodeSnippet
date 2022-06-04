"""
DoublyLinkedList program has a head and tail.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        # insert nodeToInsert before this node
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # first remove nodeToInsert from the list
        self.remove(nodeToInsert)
        # insert nodeToInsert before node
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            # replace head
            self.head = nodeToInsert
        else:
            # update node prev's next pointer to nodeToInsert
            node.prev.next = nodeToInsert

        node.prev = nodeToInsert

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        # insert nodeToInsert after node
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        # nodeToInsert after node
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            # replace tail
            self.tail = nodeToInsert
        else:
            # update next node's prev pointer to nodeToInsert
            node.next.prev = nodeToInsert

        node.next = nodeToInsert

    # O(p) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        # insert nodeToInsert at position
        if position == 1:
            self.setHead(nodeToInsert)
            return

        currentPosition = 1
        node = self.head
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        # insert before position
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        # or set tail
        else:
            self.setTail(nodeToInsert)

    # O(1) time | O(1) space
    def removeNodesWithValue(self, value):
        # remove node with this value
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            # we could remove multiple nodes with this value therefore keep remove inside the while loop
            # and node = node.next before self.remove because remove changes the node.next pointer
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O(1) time | O(1) space
    def remove(self, node):
        # remove this node
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.__removeNodeBindings(node)

    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        # return whether list contain node with this value
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def __removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest

Node = Node


def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = DoublyLinkedList()
        one = Node(1)
        two = Node(2)
        three = Node(3)
        three2 = Node(3)
        three3 = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        bindNodes(one, two)
        bindNodes(two, three)
        bindNodes(three, four)
        bindNodes(four, five)
        linkedList.head = one
        linkedList.tail = five

        linkedList.setHead(four)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 3, 5])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [5, 3, 2, 1, 4])

        linkedList.setTail(six)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 3, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 3, 2, 1, 4])

        linkedList.insertBefore(six, three)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 3, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 3, 5, 2, 1, 4])

        linkedList.insertAfter(six, three2)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 3, 6, 3])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 6, 3, 5, 2, 1, 4])

        linkedList.insertAtPosition(1, three3)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [3, 4, 1, 2, 5, 3, 6, 3])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 6, 3, 5, 2, 1, 4, 3])

        linkedList.removeNodesWithValue(3)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 2, 1, 4])

        linkedList.remove(two)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 1, 4])

        self.assertEqual(linkedList.containsNodeWithValue(5), True)
