"""We’re given an ascending string of integers that represents page numbers.
Write a function get_last_page to return the last page number in the string.
If the string of integers is not in correct page order, return the last number in order. """

def get_last_page(int_string):
    cursor = 0
    expected_number = 0
    while cursor < len(int_string):
        target = str(expected_number+1)
        increment = len(target)
        if int_string[cursor:cursor+increment] == target:
            cursor += increment
            expected_number += 1
        # unexpected break in number
        else:
            return expected_number
    return expected_number


input = '12345'  # output = 5
print(get_last_page(input))
input = '12345678910111213'  # output = 13
print(get_last_page(input))
input = '1235678'  # output = 3
print(get_last_page(input))
