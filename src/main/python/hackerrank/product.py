from itertools import product

def cartesian_product(arr1, arr2):
    print(*product(A, B))


A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]

cartesian_product(A,B)