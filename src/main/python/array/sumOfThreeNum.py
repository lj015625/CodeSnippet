def threeNumberSumBruteforce(array, targetSum):
    results = []
    for i in range(0, len(array)-2):
        for j in range(i + 1, len(array)-1):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == targetSum:
                    results.append([array[i], array[j], array[k]])
    return results

print(threeNumberSumBruteforce([12, 3, 1, 2, -6, 5, -8, 6], 0))


def threeNumberSum(array, targetSum):
    results = []
    array.sort()
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                results.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return results

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))


