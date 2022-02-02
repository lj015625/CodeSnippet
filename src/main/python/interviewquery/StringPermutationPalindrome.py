"""Given a string str, write a function perm_palindrome to determine
whether there exists a permutation of str that is a palindrome."""

from collections import Counter


def perm_palindrome(str):
    c = Counter(str)

    num_odds = 0

    for char, count in c.items():
        if count % 2 != 0:
            num_odds += 1

    return num_odds <= 1


def perm_palindrome(str):
    arr = [0] * 1000

    num_odds = 0
    # keeping one array that maps each index to its corresponding character.
    # Then we can even do this in a single pass as we iterate over the string and keep track of the odd counts.
    for char in str:
        # integer representing the Unicode character.
        i = ord(char)
        arr[i] += 1

        if arr[i] % 2 != 0:
            num_odds += 1
        else:
            num_odds -= 1

    return num_odds <= 1

str = 'carerac'
print(perm_palindrome(str))
