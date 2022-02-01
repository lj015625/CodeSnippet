"""You have an array of integers of length n spanning 0 to n with one missing.
Write a function missing_number that returns the missing number in the array."""


def missing_number(nums):
    n = max(nums)
    total = n * (n + 1) / 2
    sum_nums = sum(nums)
    if total == sum_nums:
        return 0
    else:
        return total - sum_nums


nums = [0, 1, 2, 4, 5]
print(missing_number(nums))
