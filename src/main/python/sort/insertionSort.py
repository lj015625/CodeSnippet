# best O(N) time O(1) space
# avg O(N^2) time O(1) space
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array

print(insertionSort([8, 5, 2, 9, 5, 6, 3]))
