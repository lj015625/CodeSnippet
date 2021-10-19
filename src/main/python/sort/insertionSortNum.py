
def insertionSortSum(a):
    n = a[0]
    # remove the first number which is length
    a = a[1:n+1]
    total = 0
    for i in range(0, n):
        temp = a[i]
        j = i - 1
        # swap previous and current if current is smaller than previous
        while j >= 0 and temp < a[j]:
            # move item to the right
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp

        print(a[0:i+1])
        for k in range(0, i+1):
            total += a[k] * (k + 1)

    return total


print(insertionSortSum([3,9,5,8]))

