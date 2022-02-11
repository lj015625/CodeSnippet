"""Calculate the sum of binary tree node depth."""

def depthFirstSearch(node, depth=0):
    if node is None:
        return 0
    return depth + depthFirstSearch(node.left, depth + 1) + depthFirstSearch(node.right, depth + 1)

# O(n) time O(h).  n = number of node.  h = height of binary tree
def nodeDepths(root):
    depth = depthFirstSearch(root, 0)
    return depth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        actual = nodeDepths(root)
        self.assertEqual(16, actual)
