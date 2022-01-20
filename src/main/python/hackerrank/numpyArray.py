import numpy as np

n, m = map(int, input().split())
arr = list(input().strip().split() for _ in range(n))
np_array = np.array(arr, int)
print(np.transpose(np_array))
print(np_array.flatten())

n, m, p = map(int, input().split())
# N * P array1
arr1 = list(input().strip().split() for _ in range(n))
np_array1 = np.array(arr1, int)
# M * P array2
arr2 = list(input().strip().split() for _ in range(m))
np_array2 = np.array(arr2, int)
# (N+M) * P array
print(np.concatenate((np_array1, np_array2), axis = 0))

A = np.array(list(input().strip().split()), int)
B = np.array(list(input().strip().split()), int)
print(np.inner(A, B))
print(np.outer(A, B))

nums = tuple(map(int, input().split()))
print(np.zeros(nums, dtype = np.int64))
print(np.ones(nums, dtype = np.int64))

n, m  = map(int, input().split())
print(np.identity(3)) #3 is for  dimension 3 X 3
print(np.eye(n, m))