"""Given a list of integers, write a function, gcd, to find the greatest common denominator between them."""


def compute_gcd(large, small):
    while small:
        reminder = large % small
        large = small
        small = reminder
    return large


def gcd(numbers):
    g = numbers[0]
    for num in numbers[1:]:
        g = compute_gcd(num, g)
    return g


int_list = [8, 16, 24]
print(gcd(int_list))
