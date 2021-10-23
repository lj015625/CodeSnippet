import math

def minMoves(arr):
    # Given an array of 0 and 1s find the min moves to move all 1 to one side
    if len(arr) == 0:
        return 0
    n = arr[0]
    # remove first length
    arr = arr[1:n+1]

    # convert arr to a binary number
    number = ""
    for digit in arr:
        number += str(digit)
    binaryNum = int(number, 2)
    print(binaryNum)
    #ones =  bin(binaryNum).replace("0b", "").count('1')
    #print(ones)

    # construct the final binary number
    num_of_1 = sum(arr)
    #print(num_of_1)
    num_of_0 = n - num_of_1
    #print(num_of_0)

    # option 1 move all 1 to left
    move1ToLeftNum = ""
    for digit in range(num_of_1):
        move1ToLeftNum += "1"
    for digit in range(num_of_0):
        move1ToLeftNum += "0"
    binaryMove1ToLeftNum = int(move1ToLeftNum, 2)
    print(binaryMove1ToLeftNum)
    #ones = bin(binaryMove1ToLeftNum).replace("0b", "").count('1')
    #print(ones)

    diff = binaryMove1ToLeftNum - binaryNum
    # 2^n - 1 = diff
    # n = log2(diff + 1)
    n1 = int(math.log2(diff+1))

    # option 2 move all 1 to the right
    move1ToRightNum = ""
    for digit in range(num_of_1):
        move1ToRightNum += "1"
    binaryMove1ToRightNum = int(move1ToRightNum, 2)
    print(binaryMove1ToRightNum)

    diff = binaryNum - binaryMove1ToRightNum
    # 2^n - 1 = diff
    # n = log2(diff + 1)
    n2 = int(math.log2(diff+1))

    return min(n1, n2)

print(minMoves([8,1,1,1,1,0,1,0,1]))