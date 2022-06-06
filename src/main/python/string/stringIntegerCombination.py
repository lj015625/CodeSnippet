"""Write a Python function that adds together
all combinations of adjacent integers of a given string of integers named int_str."""


def int_str_addition(int_str):
    sum = 0
    for beg in range(len(int_str)):
        # end index is last index +1 [beg:end]
        for end in range(beg + 1, len(int_str) + 1):
            print(int_str[beg:end])
            sum += int(int_str[beg:end])
    return sum


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        int_str = '12'
        self.assertEqual(15, int_str_addition(int_str))


