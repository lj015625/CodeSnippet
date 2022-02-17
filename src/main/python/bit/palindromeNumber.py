import math

class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: integer
        :rtype: bool
        """
        if x <= 0:
            return x == 0

        num_digits = math.floor(math.log10(x)) + 1
        msd_mask = 10 ** (num_digits - 1)
        iterations = num_digits // 2
        for i in range(iterations):
            most_sig_dig = x // msd_mask  # floor division discards the fractional part
            least_sig_dig = x % 10 # the % operator returns the remainder of the division
            if most_sig_dig != least_sig_dig:
                return False

            x %= msd_mask  # Remove the most significant digit of x
            x //= 10 #Remove the least significant digix of x.
            msd_mask //= 100 #remove two digits from mask

        return True

solution = Solution()
print(solution.isPalindrome(151751))