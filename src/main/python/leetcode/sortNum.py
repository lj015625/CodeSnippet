class Solution:

    def insertionSortedSum(self, a):
        n = a[0]
        # remove the first number which is length
        a = a[1:n+1]
        sum = 0
        for i in range(0, n):
            temp = a[i]
            j = i - 1
            # swap previous and current if current is smaller than previous
            while j >= 0 and temp < a[j]:
                # move item to the right
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = temp

            print(a[0:i+1])
            for k in range(0, i+1):
                sum += a[k] * (k+1)

        return sum



solution = Solution()
print(solution.insertionSortedSum([3,9,5,8]))

