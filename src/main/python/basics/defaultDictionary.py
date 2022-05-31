"""
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict)
container, but the only difference is that a defaultdict will have a default value if that key has not been set yet.

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'
For the first word in group B is 'a', it appears at positions 1, 2, 3 in group A.
The second word in group B is 'b' in group B, 'a', it appears at positions 3, 5 in group A.
Expected output:
1 2 4
3 5
"""
from collections import defaultdict

n, m = 5, 2
a = ['a', 'a', 'b', 'a', 'b']
b = ['a', 'b']

d = defaultdict(list)
for i in range(n):
    key = a[i]
    d[key].append(str(i+1))

# find existing key's position, if not found print -1.
for j in range(m):
    key = b[j]
    if key in d:
        print(" ".join(d[key]))
    else:
        print(-1)
