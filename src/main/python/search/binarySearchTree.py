# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# avg O(log(n)) time O(1) space
# worst O(n) time O(1) space
def findClosestValueInBst(tree, target):
    currentNode = tree
    closest = currentNode.value
    while currentNode is not None:
        # if current value is closer then with new closest value
        if abs(target - currentNode.value) < abs(target - closest):
            closest = currentNode.value
        # move to left child node
        if target < currentNode.value:
            currentNode = currentNode.left
        # move to right child node
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            return currentNode.value

    return closest



import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)
