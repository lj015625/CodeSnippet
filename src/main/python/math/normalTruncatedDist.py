"""Given a percentile_threshold, sample size N, and mean and standard deviation m and sd of the normal distribution,
write a function truncated_dist to simulate a normal distribution truncated at percentile_threshold.
"""

import numpy as np
import scipy.stats as st


def truncated_dist(m, sd, n, percentile_threshold):
    # The inverse of the CDF is called the PPF or percentage point function.
    lim = st.norm(m, sd).ppf(percentile_threshold)
    v = [0] * n
    i = 0
    while i < n:
        # generate random normal number
        r = np.random.normal(m, sd, 1)[0]
        # truncate right tail
        if r <= lim:
            v[i] = r
            i = i + 1

    return v


m = 2
sd = 1
n = 6
percentile_threshold = 0.75
print(truncated_dist(m, sd, n, percentile_threshold))
