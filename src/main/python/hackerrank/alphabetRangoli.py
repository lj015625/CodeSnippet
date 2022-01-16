import string

def print_rangoli(n):
    alpha = string.ascii_lowercase

    myList = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        # each row contains 17 characters.  n = 5, row = 4 * 5 - 3 = 17
        myList.append((s[::-1]+s[1:]).center(4*n-3, "-"))

    print('\n'.join(myList[::-1]))
    print('\n'.join(myList[1:]))