# O(2^N) time, O(N) space
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n-2)

# O(N) time, O(N) space
def getNthFib2(n, memoize={1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]

# O(N) time, O(1) space
def getNthFib3(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

# O(N) time, O(1) space
def getNthFib4(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
        return a
