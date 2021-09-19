import random
class Solution(object):

    def uniforrn_random(self, lower_bound, upper_bound):

        random_number = upper_bound - lower_bound + 1
        while True:
            result, i = 0, 0
            # generate a number in range
            while (1 << i) < random_number:
                zero_one_random = random.randint(0, 1)
                # fill each bit
                result = (result << 1) | zero_one_random
                i += 1
            if result < random_number:
                break

        return result + lower_bound

solution = Solution()
print(solution.uniforrn_random(1, 10))