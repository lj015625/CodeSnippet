"""Given two strings A and B, write a function can_shift to return
whether or not A can be shifted some number of places to get B."""


# def can_shift(string1, string2):
#     if len(string1) != len(string2):
#         return False
#     for i in range(len(string1)):
#         string1 = string1[-1] + string1[:-1]
#         if string1 == string2:
#             return True
#     return False

def can_shift(string1, string2):
    # A = 'abcde'
    # B * 2 = 'cdeabcdeab'
    return (string1 and string2 and
            len(string1) == len(string2) and
            string1 in string2 * 2)


A = 'abcde'
B = 'cdeab'
assert (can_shift(A, B) == True)

A = 'abc'
B = 'acb'
assert (can_shift(A, B) == False)
