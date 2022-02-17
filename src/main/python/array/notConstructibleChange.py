"""Find non-constructible changes from array of coins."""

# O(n^2) time
def nonConstructibleChange(coins):
    if len(coins) == 0:
        return 1
    # use a set to track existing changes and remove duplicates
    changes = set()
    for i in range(len(coins)):
        coin = coins[i]
        # looping over existing changes and add current coin
        for j in changes.copy():
            changes.add(j + coin)
        # add current coin
        changes.add(coin)
    for k in range(1, sum(changes)):
        if k not in changes:
            return k
    return max(changes) + 1


# O(log(n)) time | O(1) space
def nonConstructibleChange2(coins):
    coins.sort()
    # start with 0 and increasing
    maxChange = 0
    for coin in coins:
        # we cannot make maxChange + 1 because coin is bigger than maxChange + 1
        if maxChange + 1 < coin:
            return maxChange + 1
        else:
            maxChange += coin
    return maxChange + 1


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = nonConstructibleChange(input)
        self.assertEqual(expected, actual)
        actual = nonConstructibleChange2(input)
        self.assertEqual(expected, actual)
