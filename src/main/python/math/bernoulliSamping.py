"""
Given a random Bernoulli trial generator, write a function to return a value sampled from a normal distribution.
"""
import numpy as np
import random
import matplotlib.pyplot as plt

def bernoulli_sample(p):
    """
    generate 100 outputs of bernoulli sample , given prob of 1 as p and 0 as 1-p

    """
    return (np.sum(random.choices([0,1],[1-p,p],k=100)))

# According to the de Moivre–Laplace theorem, as n grows large,
# the shape of the discrete distribution converges to the continuous Gaussian curve of the normal distribution.
def normal_approximation(p):
    l = []
    for i in range(1000):
        l.append(bernoulli_sample(p))
    plt.hist(l)

    return random.choice(l)

print(normal_approximation(0.5))
