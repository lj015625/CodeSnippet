"""Write a function that outputs the (sample) variance given a list of integers."""


def variance(test_list):
    n = len(test_list)
    mean = sum(test_list) / n
    temp_list = [(mean - y) ** 2 for y in test_list]
    return sum(temp_list) / n


test_list = [6, 7, 3, 9, 10, 15]
print(variance(test_list))
