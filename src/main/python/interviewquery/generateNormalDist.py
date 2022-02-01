# Generate Normal Distribution
import scipy.stats
import numpy as np

import matplotlib.pyplot as plt


def sample_from_norm(N):
    dist = scipy.stats.norm(0, 1)
    samples = dist.rvs(N)

    fig, ax = plt.subplots(1, 1)
    x = np.linspace(scipy.stats.norm.ppf(0.01),
                    scipy.stats.norm.ppf(0.99), 100)
    ax.plot(x, dist.pdf(x), 'k-', lw=2, label='frozen pdf')
    ax.hist(samples, density=True, histtype='stepfilled')
    ax.legend(loc='best', frameon=False)
    plt.xlabel(str(N)+' samples')
    plt.ylabel('Count')
    plt.show()

    return samples

sample_from_norm(1000000)