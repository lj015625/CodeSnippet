"""Calculate the sum of binary tree node depth."""


def depthFirst(node, depth=0):
    if node is None:
        return 0
    return depth + depthFirst(node.left, depth + 1) + depthFirst(node.right, depth + 1)


# O(n) time O(h).  n = number of node.  h = height of binary tree
def nodeDepths(root):
    depth = depthFirst(root, 0)
    return depth


# O(n) time O(h).  n = number of node.  h = height of binary tree
def nodeDepthsBreadthFirst(root):
    sumOfDepth = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        # breadth first add parent
        sumOfDepth += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumOfDepth


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
        actual = nodeDepthsBreadthFirst(root)
        self.assertEqual(16, actual)
