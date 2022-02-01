"""Given a list of integers, find the index at which the sum of the left half of the list is equal to the right half.

If there is no index where this condition is satisfied return -1."""


def pivotIndex(arr):
    total_sum = sum(arr)
    if total_sum % 2 == 1:
        return -1
    target_sum = total_sum / 2
    current_sum = 0
    for i, num in enumerate(arr):
        current_sum += num
        if target_sum == current_sum:
            return i
    return -1


nums = [1, 7, 3, 5, 6]
print(pivotIndex(nums))
