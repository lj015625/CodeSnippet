"""Given an array of unsorted random numbers denoted nums write a function find_iqr to find the interquartile distance.
The interquartile distance is defined by subtracting the first quartile
from the third quartile.
"""

def median(a):
    k = len(a)
    if k % 2 == 0:
        return( (a[k//2] + a[k//2-1]) / 2)
    if k % 2 == 1:
        return(a[k//2])

def find_iqr(nums):
    nums.sort()
    k = len(nums)
    if k % 2 == 0:
        u_half = nums[k//2:k]
        l_half = nums[0:k//2]
    if k % 2 == 1:
        u_half = nums[k//2+1:k]
        l_half = nums[0:k//2]
    Q1 = median(l_half)
    Q3 = median(u_half)

    return Q3 - Q1

nums = [3,4,9,12,14,239]
print(find_iqr(nums))
