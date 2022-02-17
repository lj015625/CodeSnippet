"""
Generate Gaussian dist.
"""

from scipy.stats import norm
import numpy as np


def generate_gaussian(N, M):
    x = norm.rvs(loc=M, scale=1, size=N)
    return np.round(x)


print(generate_gaussian(N=9, M=3))
