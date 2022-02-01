def pivotIndex(nums):
    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return -1
    target_sum = total_sum / 2
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if target_sum == current_sum:
            return i
    return -1

nums = [1, 7, 3, 5, 6]
print(pivotIndex(nums))
