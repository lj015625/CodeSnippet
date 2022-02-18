"""

"""


# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiply=1):
    sum = 0
    for value in array:
        if isinstance(value, list):
            sum += productSum(value, multiply + 1)
        else:
            sum += value
    return multiply * sum


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(12, productSum(test))
