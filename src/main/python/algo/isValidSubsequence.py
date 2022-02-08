def isValidSubsequence(array, sequence):
    # queue is pop from first item
    q = sequence.pop(0)
    for i in array:
        if i == q:
            if len(sequence) == 0:
                return True
            # get another item from queue
            q = sequence.pop(0)
    return False

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))

def isValidSubsequence2(array, sequence):
    arrIndex = 0
    subseqIndex = 0
    while arrIndex < len(array) and subseqIndex < len(sequence):
        if array[arrIndex] == sequence[subseqIndex]:
            subseqIndex += 1
        arrIndex += 1
    return subseqIndex == len(sequence)


print(isValidSubsequence2([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
