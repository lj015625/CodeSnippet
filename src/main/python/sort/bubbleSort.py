# best O(N) time O(1) space
# avg O(N^2) time O(1) space
# worst O(N^2) time O(1) space
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):

        # right most i elements are sorted therefore moving item to the right
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array is:", bubbleSort(arr))
