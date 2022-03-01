"""
Count the minimum number of bills to get to an amount.  If cannot find a combination then return -1.
"""


# O(nd) time O(n) space  n is amount d is len of bills
def minNumberOfCoinsForChange(amount, bills):
    if amount <= 0:
        return 0
    minNumOfBills = [float('inf') for _ in range(amount + 1)]
    # min number of bill is 0 get 0 dollars
    minNumOfBills[0] = 0
    # for each bill add to ways
    for bill in bills:
        # for each amount from 1 to amount
        for amt in range(1, amount + 1):
            # if we can add this bill then count of (amt) is added by count of (amt - bill)
            if bill <= amt:
                # use minimal of current number of bills or [amt - bill] + 1,
                # number of bill for amt - bill and current bill
                minNumOfBills[amt] = min(minNumOfBills[amt - bill] + 1, minNumOfBills[amt])
    # default is -1 if not found
    return minNumOfBills[amount] if minNumOfBills[amount] != float('inf') else -1


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(3, minNumberOfCoinsForChange(7, [1, 5, 10]))
