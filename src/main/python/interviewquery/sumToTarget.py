"""Given an array and a target integer, write a function sum_pair_indices that returns the indices of two integers
in the array that add up to the target integer if not found such just return empty list.
Note: even though there could be many solutions, only one needs to be returned."""

def sum_pair_indices(array, target):
    index_holder = {}
    for i in range(len(array)):
        current_number = array[i]
        complement = target - current_number
        if complement in index_holder:
            return [index_holder[complement], i]
        else:
            index_holder[current_number] = i
    return []

array = [1, 2, 3, 4]
target = 5
print(sum_pair_indices(array, target))


def twoNumberSum(array, targetSum):
    # use hashset O(n) time O(n) space
    saved = {}
    for current_num in array:
        complement = targetSum - current_num
        if complement in saved:
            return [current_num, complement]
        else:
            # use dict as a hashset not a hashmap
            saved[current_num] = True
    return []

array = [3,5,-4,8,11,1,-1,6]
target = 10
print(twoNumberSum(array, target))


def twoNumberSum2(array, targetSum):
    # use sorting O(nlogn) time O(1) space
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

print(twoNumberSum2(array, target))
