def fourNumberSum(array, targetSum):
    results = []
    allPairsSums = {}
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            complement = targetSum - currentSum
            # found a match add to results
            if complement in allPairsSums:
                # for each saved pairs equals to complements add combos with [array[i], array[j]]
                for pair in allPairsSums[complement]:
                    results.append(pair + [array[i], array[j]])
        # only add pairs to hashtable when loop is on the second number to prevent double counting
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairsSums:
                # add new array of arrays
                allPairsSums[currentSum] = [[array[k], array[i]]]
            else:
                # add other combinations
                allPairsSums[currentSum].append([array[k], array[i]])

    return results


print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))
