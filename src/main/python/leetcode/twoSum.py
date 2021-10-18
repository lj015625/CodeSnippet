"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""
from typing import List

class Solution:
     """
     Hashmap save a number's position index
     """
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         hashmap = {}
         for i, num in enumerate(nums):
             complement = target - num
             if complement in hashmap:
                 return [i, hashmap[complement]]
             hashmap[num] = i
         return []

solution = Solution()
print(solution.twoSum([2,7,11,15],9))