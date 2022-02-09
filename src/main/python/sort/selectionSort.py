# best O(N^2) time O(1) space
# avg O(N^2) time O(1) space
# worst O(N^2) time O(1) space
def selectionSort(array):
    for i in range(len(array)):
        smallestIndex = i
        # find the smallest number
        for j in range(i + 1, len(array)):
            if array[smallestIndex] > array[j]:
                smallestIndex = j
        array[i], array[smallestIndex] = array[smallestIndex], array[i]
    return array


A = [64, 25, 12, 22, 11]
print("Sorted array", selectionSort(A))
