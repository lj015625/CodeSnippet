# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot on the right

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            # swap smaller number than pivot to the left pointer
            arr[i], arr[j] = arr[j], arr[i]

    # put pivot with final position of the right pointer
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr


# use left most as pivot
# avg O(nlog(n)) time O(nlog(n)) space
# worst O(n^2) time O(nlog(n)) space
def quickSort2(array):
    qucikSortHelper(array, 0, len(array) - 1)
    return array


def qucikSortHelper(array, start, end):
    if start >= end:
        return
    pivotIdx = start
    # skip the first pivotIdx item
    leftIdx = start + 1
    rightIdx = end
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] > array[rightIdx]:
            # swap if leftIdx is bigger than pivotIdx than rightIdx
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    # change pivotIdx from last unsorted value on the rightIdx
    array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]

    leftSubarraySmaller = rightIdx - start < end - rightIdx
    if leftSubarraySmaller:
        qucikSortHelper(array, start, rightIdx - 1)
        qucikSortHelper(array, rightIdx + 1, end)
    else:
        qucikSortHelper(array, rightIdx + 1, end)
        qucikSortHelper(array, start, rightIdx - 1)


arr = [10, 7, 8, 9, 1, 5]
print("Sorted array is: ", quickSort(arr, 0, len(arr) - 1))

arr = [10, 7, 8, 9, 1, 5]
print("Sorted array is: ", quickSort2(arr))
