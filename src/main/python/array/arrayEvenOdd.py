class Solution(object):
    """
    Rearrange an array to even and odd
    """

    def even_odd (self, A):
        next_even, next_odd = 0, len(A) - 1
        while next_even < next_odd:
            # if it is even then increment next_even pointer
            if A[next_even] % 2 == 0:
                next_even += 1
            # if it is odd swap next_odd with next_even then increment next_odd pointer
            else:
                A[next_even], A[next_odd] = A[next_odd], A[next_even]
                next_odd -= 1
        return A
solution = Solution()
print(solution.even_odd([2,3,4,5,6,7,8,9,10,11,12,13,17]))