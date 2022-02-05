"""Capital One has two levels of customer acquisition strategies for customers that are opening credit cards.

For high spending customers, Capital One will give clients a one-time bonus of 800 dollars.
For everyone else, they give a 100 dollar bonus.

Write a function in Python that takes a list of client spends as floats
and figures out the threshold to divide the high spending vs low spending customers.
"""
import math
import numpy as np


def get_threshold(spends, margin=0.1):
    median = np.median(spends)
    percentile_n = (800 - median * margin) / 700

    if percentile_n > 1:
        percentile_n = 1
    elif percentile_n < 0:
        percentile_n = 0.1

    percentile_n *= 100
    percentile_n = math.ceil(percentile_n)

    return np.percentile(spends, percentile_n)

input = [704, 704, 795, 1103, 1127, 1461, 1528, 1559, 1658, 1823, 2011,
         2031, 2063, 2154, 2291, 2293, 2335, 2338, 2517, 2526, 2977, 3014,
         3100, 3335, 3359, 3532, 3543, 3561, 3858, 3977, 4097, 4120, 4164,
         4339, 4463, 4549, 4637, 4785, 5132, 5199, 5360, 5799, 6027, 6028,
         6082, 6194, 6242, 6660, 6940, 6959]
print(get_threshold(input))