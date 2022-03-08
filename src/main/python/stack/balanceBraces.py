"""
Take a string with braces and brackets and other optional characters and return whether braces and brackets are balanced
"""
from collections import deque


def balancedBrackets(string):
    bracesStack = deque()
    for char in string:
        if char in '({[':
            bracesStack.append(char)
        elif char == ')':
            if len(bracesStack) == 0 or bracesStack.pop() != '(':
                return False
        elif char == ']':
            if len(bracesStack) == 0 or bracesStack.pop() != '[':
                return False
        elif char == '}':
            if len(bracesStack) == 0 or bracesStack.pop() != '{':
                return False

    # any extra braces remaining
    if len(bracesStack) > 0:
        return False

    return True


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balancedBrackets("([])(){}(())()()"), True)
