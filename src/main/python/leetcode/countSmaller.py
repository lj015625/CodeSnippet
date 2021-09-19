from sortedcontainers import SortedList, SortedDict

class Solution(object):
    """
    Count number of integers that is smaller than current number in array from left to right.
    """


    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [0] * len(nums)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    output[i] = output[i] + 1

        return output

    def countSmaller2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [0] * n
        savedAnswer = SortedList()
        # list[<start>:<stop>:<step>]
        for i, num in enumerate(nums[::-1]):
            index = n-i-1
            # skip the last item in the array
            if index < n-1:
                answer[index] = savedAnswer.bisect_left(num)
            savedAnswer.add(num)
        return answer

solution = Solution()
nums = [5,2,6,1]
print(solution.countSmaller2(nums))

# sd = SortedDict({'5':2, '2':1, '6':1, '1':0})
# print(sd)
# print(sd.bisect_left('2'))
# print(sd.bisect_right('2'))
# print(sd['2'])