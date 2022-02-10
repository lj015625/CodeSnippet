# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depthFirstSearch(node, branchSum, array):
    branchSum += node.value
    if node.left is None and node.right is None:
        array.append(branchSum)
    if node.left is not None:
        depthFirstSearch(node.left, branchSum, array)
    if node.right is not None:
        depthFirstSearch(node.right, branchSum, array)

# O(n) time O(n) space where n is number of node
def branchSums(root):
    currentNode = root
    array = []
    depthFirstSearch(currentNode, 0, array)
    return array

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual([15, 16, 18, 10, 11], branchSums(tree))


class BinaryTree(BinaryTree):
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