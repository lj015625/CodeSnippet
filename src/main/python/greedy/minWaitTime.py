""" Given a list of positive integer representing the amounts of time that specific queries take to execute.
Only one query can be executed at a time, but the queries can be executed in any order.
A query's wait time is defined as the amount of time that it must wait before its execution starts.
In other words, if a query is executed second, then its waiting time is the duration of the first query;
if a query is executed third, then its waiting time is the sum of the durations of the first two queries.
Return minimum of sum of wait time for a list of wait times for . Free to rearrange the order of wait times.

For example if you are given the queries of durations [1, 4, 5], then the total waiting tie if the queries were
executed in the order of [5, 1, 4] would be (0) + (5) + (5 + 1) = 11. the first query duration 5 would be
executed immediately, so the waiting time would be 0, the second query of duration 1 would have to wait
5 seconds (duration of the first query) to be executed, and the last query would have to wait the duration of
the first two queries before being executed.

"""


# O(log(n)) time O(1) space where n is number of queries
def minimumWaitingTime1(queries):
    totalWaitTime = 0
    # sort in increase order
    queries.sort()
    # use a decreasing multiplier
    for i, num in enumerate(queries):
        # multiplier is used on each item
        # first item in array would be added n times where n is array size,
        # the second to last item would be added 1 times  len(n) - 1 - i where i is 0, 1, 2,...n-1
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
        # previous sum is saved
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
