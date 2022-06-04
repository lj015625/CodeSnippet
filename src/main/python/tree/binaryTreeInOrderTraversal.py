"""
Node has additional pointer to parent.  Successor is next node to be visited in-order traversal.
tree =   1
       /   \
      2     3
     /       \
    4         5
   /
  6
node = 5

output 1
6 -> 4 -> 2 -> 5 -> 1 -> 3

"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(n) time | O(1) space n is number of node
def findSuccessor1(tree, node):
    inOrderTraversalOrder = getInOrderTraversalOrder(tree)

    for i, currentNode in enumerate(inOrderTraversalOrder):
        if currentNode != node:
            continue
        # last node
        if i == len(inOrderTraversalOrder) - 1:
            return None
        # return next node
        return inOrderTraversalOrder[i + 1]


def getInOrderTraversalOrder(node, order=[]):
    if node is None:
        return order
    # traverse to left most child node as first node
    getInOrderTraversalOrder(node.left, order)
    # add current node
    order.append(node)
    # then traverse to right most child node
    getInOrderTraversalOrder(node.right, order)

    return order


# if a tree has no right subtree then next node is left most child
# else traverse up ancestor's right most parent.
# O(h) time | O(1) space h is height of tree
def findSuccessor2(tree, node):
    if node.right is not None:
        return getLeftMostChild(node.right)
    else:
        return getRightMostParent(node)


def getLeftMostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode


def getRightMostParent(node):
    currentNode = node
    # get top parent node as long as right node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    return currentNode.parent


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.parent = root
        root.right = BinaryTree(3)
        root.right.parent = root
        root.left.left = BinaryTree(4)
        root.left.left.parent = root.left
        root.left.right = BinaryTree(5)
        root.left.right.parent = root.left
        root.left.left.left = BinaryTree(6)
        root.left.left.left.parent = root.left.left
        # 5
        node = root.left.right
        expected = root
        actual = findSuccessor1(root, node)
        self.assertEqual(actual, expected)
        actual = findSuccessor2(root, node)
        self.assertEqual(actual, expected)
