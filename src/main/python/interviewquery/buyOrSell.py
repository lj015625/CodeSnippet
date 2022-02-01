"""find max gain given stock prices and date"""
def max_profit(stock_prices, dts):
    max = 0
    max_dt_1 = 0
    max_dt_2 = 0
    for i in range(0, len(stock_prices)):
        for j in range(i+1, len(stock_prices)):
            diff = stock_prices[j] - stock_prices[i]
            if diff > max:
                max = diff
                max_dt_1 = i
                max_dt_2 = j

    return [max, dts[max_dt_1], dts[max_dt_2]]


stock_prices = [10, 5, 20, 32, 25, 12]
dts = [
    '2019-01-01',
    '2019-01-02',
    '2019-01-03',
    '2019-01-04',
    '2019-01-05',
    '2019-01-06',
]
print(max_profit(stock_prices, dts))

