# use Recursive functions
def countways_(bills, amount, index):
    if amount == 0:  # base case 1
        return 1
    if amount < 0 or index >= len(bills):  # base case 2
        return 0
    # count the amount with current bill, and amount without current bill
    return countways_(bills, amount - bills[index], index) + countways_(bills, amount, index + 1)


def countways(bills, amount):
    return countways_(bills, amount, 0)


print(countways([1, 2, 5], 5))


# more efficient use dynamic programming
def countways_dp(bills, amount):
    if amount <= 0:
        return 0
    # save calculated results default to 1 for each amount
    dp = [[1 for _ in range(len(bills))] for _ in range(amount + 1)]
    #print(dp)
    for amt in range(1, amount + 1):
        for j in range(len(bills)):
            bill = bills[j]
            # can add this bill j
            if amt - bill >= 0:
                # existing count for j and (amt - bill) is dp[amt - bill][j]
                x = dp[amt - bill][j]
            else:
                x = 0
            # cannot add this bill j
            if j >= 1:
                # existing count for previous j-1 and amt is dp[amt][j-1]
                y = dp[amt][j - 1]
            else:
                y = 0
            # save count for j and amt
            dp[amt][j] = x + y

    print(dp)
    return dp[amount][len(bills) - 1]


print(countways_dp([1, 2, 5], 5))
