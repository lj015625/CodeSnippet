import itertools as it

def combinational_dice_rolls(n, m):
    return list(it.product(range(1, m+1), repeat=n))
combinational_dice_rolls(2,2)

def cartesian_product(arr1, arr2):
    print(*it.product(A, B))
A = [1,2,3]
B = [1,2,3]
cartesian_product(A,B)


s, n = 2, 3
s = sorted(str(s))
n = int(n)
for i in it.permutations(s,n):
    print(''.join(i), sep='\n')


s, n = 'ABC', 2
for i in range(1, int(n)+1):
    for j in it.combinations(sorted(s), i):
        print(''.join(j))


# This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
s, n = 'ABC', 2
for c in it.combinations_with_replacement(sorted(s), int(n)):
    print("".join(c))


# create list of tuples from repeating items in a string
print(*[(len(list(values)), int(key)) for key, values in it.groupby('12345')])


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
