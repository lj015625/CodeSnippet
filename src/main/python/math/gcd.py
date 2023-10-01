"""Given a list of integers, write a function, gcd, to find the greatest common denominator between them."""


def compute_gcd(large, small):
    while small > 0:
        reminder = large % small
        large, small = small, reminder
    return large


def gcd(numbers):
    small = numbers[0]
    for large in numbers[1:]:
        small = compute_gcd(large, small)
    return small


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1, gcd([5, 16, 24]))

    def test_case_2(self):
        self.assertEqual(8, gcd([8, 16, 24]))

    def test_case_3(self):
        self.assertEqual(2, gcd([2, 4, 8, 16, 32, 64]))

