# O(n) time O(1) space
def findThreeLargestNumbers(array):
    # three largest number in increasing order
    threeLargest = [None, None, None]
    for num in array:
        if threeLargest[2] is None or num > threeLargest[2]:
            insertThreeLargest(2, num, threeLargest)
        elif threeLargest[1] is None or num > threeLargest[1]:
            insertThreeLargest(1, num, threeLargest)
        elif threeLargest[0] is None or num > threeLargest[0]:
            insertThreeLargest(0, num, threeLargest)

    return threeLargest

def insertThreeLargest(index, num, threeLargest):
    # shift smaller number to the left
    # if index == 2:
    #     threeLargest[0] = threeLargest[1]
    #     threeLargest[1] = threeLargest[2]
    #     threeLargest[2] = num
    # elif index == 1:
    #     threeLargest[0] = threeLargest[1]
    #     threeLargest[1] = num
    # elif index == 0:
    #     threeLargest[0] = num
    for i in range(0, index+1):
        if i == index:
            threeLargest[i] = num
        elif threeLargest[i+1] is not None:
            threeLargest[i] = threeLargest[i+1]



import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])
