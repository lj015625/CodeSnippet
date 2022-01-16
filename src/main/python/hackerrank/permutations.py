from itertools import permutations
s,n = input().split()
s = sorted(str(s))
n = int(n)

for i in permutations(s,n):
    print(''.join(i), sep='\n')
