import itertools as it

def cartesian_product(arr1, arr2):
    print(*it.cartesian_product(A, B))

A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]
cartesian_product(A,B)


s,n = input().split()
s = sorted(str(s))
n = int(n)
for i in it.permutations(s,n):
    print(''.join(i),sep='\n')


s,n = input().split()
for i in range(1, int(n)+1):
    for j in it.combinations(sorted(s), i):
        print(''.join(j))


# This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
s, n = input().split()
for c in it.combinations_with_replacement(sorted(s), int(n)):
    print("".join(c))


# create list of tuples from repeating items in a string
print(*[(len(list(values)), int(key)) for key, values in it.groupby(input())])


# count number of a in combinations
n = 4
arr = ['a', 'a', 'c', 'd']
k = 2
count = 0
total = 0
for t in it.combinations(arr, k):
    total += 1
    count += 'a' in t
print(count/total)
