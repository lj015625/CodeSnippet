"""Given an integer NN, write a Python function that returns all of the prime numbers up to NN.
"""

def prime_numbers(N):
    primes = []
    for num in range(2, N):
        # all prime numbers are greater than 1
        # for i in range(2, num):
        #     if (num % i) == 0:
        #             break
        # else:
        #     print(num)
        if all(num % i != 0 for i in range(2, num)):
            primes.append(num)
    return primes

print(prime_numbers(5))
