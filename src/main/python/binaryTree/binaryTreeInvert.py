"""
Swap every left node with right node.
"""

def swapLeftRight(node):
    node.left, node.right = node.right, node.left

# O(n) time O(d) space
def invertBinaryTree(tree):
    swapLeftRight(tree)
    if tree.left is not None:
        invertBinaryTree(tree.left)
    if tree.right is not None:
        invertBinaryTree(tree.right)

# O(n) time O(n) space
def invertBinaryTreeBreadthFirst(tree):
    queue = [tree]
    while queue:
        current = queue.pop(0)
        swapLeftRight(current)
        invertBinaryTreeBreadthFirst(current.left) if current.left is not None else None
        invertBinaryTreeBreadthFirst(current.right) if current.right is not None else None

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


import unittest


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def invertedInsert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
        self.invertedInsert(values, i + 1)
        return self


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
        invertedTree = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9])
        invertBinaryTree(tree)
        self.assertTrue(tree.__eq__(invertedTree))
        invertBinaryTreeBreadthFirst(tree)
        self.assertTrue(tree.__eq__(invertedTree))
