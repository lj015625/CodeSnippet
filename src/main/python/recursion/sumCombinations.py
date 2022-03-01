"""Function to find out all combinations of positive numbers that add upto given number."""


def findCombinationsUtil(results, temp, index, max, target):
    if target < 0:
        return

    if target == 0:
        results.append(temp[0:index])
        return

    # Find the previous number stored in temp[].
    if index == 0:
        prev = 1
    else:
        prev = temp[index - 1]

    # note loop starts from previous number
    for k in range(prev, max + 1):
        # next element of array is k
        temp[index] = k

        # call recursively with target - temp[index]
        findCombinationsUtil(results, temp, index + 1, max, target - temp[index])


def findCombinations(n):
    results = []

    # array to store the combinations
    # It can contain max n elements
    arr = [0] * n

    # find all combinations
    findCombinationsUtil(results, arr, 0, n, n)
    print(results)


# Driver code
n = 5
findCombinations(n)
