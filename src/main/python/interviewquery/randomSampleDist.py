"""
Write a function to generate M samples from a random normal distribution of size N.
Then return the average difference between the 5th and 6th lowest values.
Note: N should always be greater than 6.
"""
import numpy as np

np.random.seed(23)


def normal_func(n, m):
    diff = 0
    # create distribution
    dist = np.random.normal(loc=0, scale=1, size=1000000)  # create distribution
    # pick m samples and find average difference
    for i in range(m):
        # random samples of n from 1000000 dist
        sample = np.random.choice(dist, n)
        S1 = sorted(sample)
        # diff between 5th and 6th
        diff += (S1[5] - S1[4])

    return diff / m


N = 10
M = 20
print(normal_func(M, N))
