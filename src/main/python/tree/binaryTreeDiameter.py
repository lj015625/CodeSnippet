"""
Diameter is length of the longest path even if path does not pass through the root.
A path is collection of connected nodes in a tree, where no node is connected to no more than two other nodes.
The length is of a path is the number of edges between path's first node and last node.
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def depthFirstDiameter(tree):
    if tree is None:
        return 0, 0

    leftPath, leftDiameter = depthFirstDiameter(tree.left)
    rightPath, rightDiameter = depthFirstDiameter(tree.right)
    # current node's path is its children's path
    path = leftPath + rightPath
    # max of current node's path, left or right branch's diameter
    maxDiameter = max(path, leftDiameter, rightDiameter)
    # maxPath is 1 + max path of left or right branch path
    maxPath = 1 + max(leftPath, rightPath)
    # always recursively pass back maxPath, maxDiameter to current node's parent
    return maxPath, maxDiameter


def binaryTreeDiameter(tree):
    maxPath, maxDiameter = depthFirstDiameter(tree)
    return maxDiameter


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.right = BinaryTree(2)
        expected = 6
        actual = binaryTreeDiameter(root)
        self.assertEqual(expected, actual)
