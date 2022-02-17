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