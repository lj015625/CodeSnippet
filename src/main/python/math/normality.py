"""Write a function that checks if a list of integers is normally distributed.
Specifically given a list of 100 numbers, write a function that returns a score that measures the deviation from normality. I.E. a normally distributed list of integers would return 0.
Note: Use What Is called the 68-95-99.7 rule of thumb for normal distributions.
Bonus: Don’t use any graphical output or a statistical test for normality.
"""

import math

import numpy as np


def normality_test_napkin(sample_list):
    list_avg = sum(sample_list) / len(sample_list)
    list_sigma = math.sqrt(sum((x - list_avg) ** 2 for x in sample_list) / len(sample_list))
    # what percent of the sample list (sample_list in these examples) fall between one, two, and three sigmas.
    perc_one_sigma = sum(
        [1 if (x < list_sigma + list_avg) and (x > list_avg - list_sigma) else 0 for x in sample_list]) / len(
        sample_list)
    perc_two_sigma = sum([1 if (x < (2 * list_sigma) + list_avg) and (x > list_avg - (2 * list_sigma)) else 0 for x in
                          sample_list]) / len(sample_list)
    perc_three_sigma = sum([1 if (x < (3 * list_sigma) + list_avg) and (x > list_avg - (3 * list_sigma)) else 0 for x in
                            sample_list]) / len(sample_list)
    print(perc_one_sigma, perc_two_sigma, perc_three_sigma)
    # We know that generally, 68% of samples fall between +-1 standard deviation from the mean of any perfectly normal distribution, 95% between +-2 standard deviations, and 99.7% between +-3.
    evidence = 0
    if perc_one_sigma <= .72 and perc_one_sigma >= .64:
        evidence += 1
    if perc_two_sigma <= .96 and perc_two_sigma >= .94:
        evidence += 1
    if perc_three_sigma >= .98:
        evidence += 1

    if evidence == 3:
        return ('There is strong evidence that this distribution is normal')
    elif evidence == 2:
        return ('There is evidence that this distribution is normal')
    elif evidence == 1:
        return ('There is little evidence that this distribution is normal')
    else:
        return ('There is no evidence that this distribution is normal')


print(normality_test_napkin(np.random.normal(0, 1, 100)))
print(normality_test_napkin(np.random.binomial(1, .5, 100)))
