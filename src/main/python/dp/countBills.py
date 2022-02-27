"""
Count number of ways from bills to sum to amount.
"""


# use Recursive functions
def countways_(amount, bills, index):
    if amount == 0:  # base case 1
        return 1
    if amount < 0 or index >= len(bills):  # base case 2
        return 0
    # count the amount with current bill, and amount without current bill
    return countways_(amount - bills[index], bills, index) + countways_(amount, bills, index + 1)


def countways(amount, bills):
    return countways_(amount, bills, 0)


# more efficient use dynamic programming
def countways_dp(amount, bills):
    if amount <= 0:
        return 0
    # save calculated results default to 1 for each amount
    dp = [[1 for _ in range(len(bills))] for _ in range(amount + 1)]
    # print(dp)
    for amt in range(1, amount + 1):
        for j in range(len(bills)):
            bill = bills[j]
            # we can add this bill j because amt - bill >= 0
            if amt - bill >= 0:
                # existing count for j and (amt - bill) is dp[amt - bill][j]
                x = dp[amt - bill][j]
            # we cannot add this bill j
            else:
                x = 0
            # count of amt previously without bill j
            if j >= 1:
                # existing count for previous j-1 and amt is dp[amt][j-1]
                y = dp[amt][j - 1]
            else:
                y = 0
            # count is ways to count of (amt - bill) and count of (amt
            dp[amt][j] = x + y

    # print(dp)
    return dp[amount][len(bills) - 1]


# much more efficient dp
# O(nd) time O(n) space
def numberOfWaysToMakeChange(amount, bills):
    if amount <= 0:
        return 0
    ways = [0 for _ in range(amount + 1)]
    ways[0] = 1
    # for each bill add to ways
    for bill in bills:
        # for each amount from 1 to amount
        for amt in range(1, amount + 1):
            # if we can add this bill then count of (amt) is added by count of (amt - bill)
            if bill <= amt:
                ways[amt] += ways[amt - bill]
    return ways[amount]


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(4, countways(5, [1, 2, 5]))

    def test_case_2(self):
        self.assertEqual(4, countways_dp(5, [1, 2, 5]))

    def test_case_3(self):
        self.assertEqual(4, numberOfWaysToMakeChange(5, [1, 2, 5]))
