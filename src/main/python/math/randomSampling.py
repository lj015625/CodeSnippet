"""Write a function for sampling from a multimodal distribution.
Inputs are keys (i.e. green, red, blue), weights (i.e. 2, 3, 5.5), and the number of samples drawn from the distribution.
The output should return the keys of the samples. """

import random

def select_n(keys, weights, n):
    return random.choices(keys, weights=weights, k=n)

keys = ['green', 'red', 'blue']
weights = [1, 10, 2]
n = 5
print(select_n(keys, weights, n))
