# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index: ", str(result))
else:
    print("Element is not present in array")


def binary_search(numlist, target):
    if not numlist:
        return
    start, end = 0, len(numlist) - 1
    while start + 1 < end:
        mid = (start + end) //2

        if numlist[mid] >= numlist[start]:
            if numlist[start] <= target <= numlist[mid]:
                end = mid
            else:
                start = mid

        else: # numlist[mid] < numlist[start]
            if numlist[mid] <= target <= numlist[end]:
                start = mid
            else:
                end = mid

    if numlist[start] == target:
        return start
    elif numlist[end] == target:
        return end

rotated_input = [4,5,6,7,0,1,2]
target_value = 6
print('Found target at index: ', binary_search(rotated_input, target_value))
