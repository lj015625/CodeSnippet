"""
Take non-empty array of integers and return an array.
Each element in the output array is product of every other number.
"""

from functools import reduce


# O(n) time O(n) space
def arrayOfProducts(array):
    # multiply array element together except 0
    totalProduct = reduce(lambda x, y: x * y if x != 0 else 1, array)
    # any zeros in the array
    numberOfZeros = sum(1 for n in array if n == 0)
    product = []
    for num in array:
        # no zero in array we can div total by num to get product of every other number
        if numberOfZeros == 0:
            product.append(totalProduct / num)
        # only one zero in array then products are all zeros except one position of 0
        elif numberOfZeros == 1 and num == 0:
            product.append(totalProduct)
        else:
            product.append(0)
    return product

# O(n) time O(n) space
def arrayOfProducts2(array):
    leftProduct = [1 for _ in range(len(array))]
    rightProduct = [1 for _ in range(len(array))]
    product = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        # product of all elements on the left except current
        leftProduct[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in range(len(array)-1, -1, -1):
        # product of all elements on the right except current
        rightProduct[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    # total product is left * right
    for i in range(len(array)):
        product[i] = leftProduct[i] * rightProduct[i]

    return product

# O(n) time O(n) space
def arrayOfProducts3(array):
    product = [1 for _ in range(len(array))]
    leftRunningProduct = 1
    for i in range(len(array)):
        # product of all elements on the left except current
        product[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in range(len(array)-1, -1, -1):
        # product of left and right
        product[i] *= rightRunningProduct
        # product of all elements on the right except current
        rightRunningProduct *= array[i]

    # total product is left * right
    return product


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        actual = arrayOfProducts(array)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [362880, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = arrayOfProducts(array)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        array = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        actual = arrayOfProducts(array)
        self.assertEqual(expected, actual)

    def test_case_4(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        actual = arrayOfProducts2(array)
        self.assertEqual(expected, actual)

    def test_case_5(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [362880, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = arrayOfProducts2(array)
        self.assertEqual(expected, actual)

    def test_case_6(self):
        array = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        actual = arrayOfProducts2(array)
        self.assertEqual(expected, actual)


