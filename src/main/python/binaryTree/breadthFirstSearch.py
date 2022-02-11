class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(vertices+edges) time O(vertices) space
    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            current = queue.pop(0)
            # use array to keep traversal record
            array.append(current.name)
            for child in current.children:
                # FIFO queue to track siblings
                queue.append(child)
        return array

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"], graph.breadthFirstSearch([]))