""" Return minimum of sum of wait time for a list of wait times. Free to rearrange the order of wait times."""


# O(log(n)) time O(1) space where n is number of queries
def minimumWaitingTime1(queries):
    totalWaitTime = 0
    queries.sort()
    # use a decreasing multiplier because first item in array would be added n times where n is array size
    for i, num in enumerate(queries):
        multiplier = len(queries) - 1 - i
        totalWaitTime += multiplier * num
    return totalWaitTime


def minimumWaitingTime2(queries):
    totalWaitTime = 0
    queries.sort()
    previous = 0
    # dynamic programming saving previous sum
    for i in range(len(queries)):
        totalWaitTime += previous
        previous += queries[i]

    return totalWaitTime


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        queries = [3, 2, 1, 2, 6]
        expected = 17
        actual = minimumWaitingTime1(queries)
        self.assertEqual(actual, expected)
        actual = minimumWaitingTime2(queries)
        self.assertEqual(actual, expected)
