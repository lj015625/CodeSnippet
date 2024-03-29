# best O(nlog(n)) time O(nlog(n)) space
# avg O(nlog(n)) time O(nlog(n)) space
# worst O(nlog(n)) time O(nlog(n)) space
def mergeSort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Recursive call on each half
    mergeSort(left)
    mergeSort(right)

    # Two iterators for traversing the two halves
    i = 0
    j = 0

    # Iterator for the main list
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # The value from the left half has been used
            array[k] = left[i]
            # Move the iterator forward
            i += 1
        else:
            array[k] = right[j]
            j += 1
        # Move to the next slot
        k += 1

    # For all the remaining values
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(myList)
print(myList)
