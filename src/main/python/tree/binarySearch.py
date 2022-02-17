def binary_search_iterative(array, target):
    if not array:
        return -1
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right) // 2
        # found the target
        if array[mid] == target:
            return mid
        # if target is in first half then search from the start to mid
        elif target < array[mid]:
            right = mid - 1
        # search from the mid to end
        else:
            left = mid + 1
    return -1


arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print(binary_search_iterative(arr, target))

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# Test array
arr = [ 2, 3, 4, 10, 40]
target = 10
print(binarySearch(arr, target))
