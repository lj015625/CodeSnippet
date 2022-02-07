def count_substring(string, sub_string):
    subStringSize = len(sub_string)
    count = 0
    for i in range(len(string)):
        if sub_string == string[i:i + subStringSize]:
            count += 1
    return count


def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


def swap_case(s):
    s1 = ''
    for c in s:
        if c.islower():
            s1 = s1 + c.upper()
        else:
            s1 = s1 + c.lower()

    return s1


def split_and_join(line):
    return "-".join(line.split())


def string_type(s):
    print(any([True for sub in s if sub.isalpha() or s.isnumeric()]))
    print(any([True for sub in s if sub.isalpha()]))
    print(any([True for sub in s if sub.isdigit()]))
    print(any([True for sub in s if sub.islower()]))
    print(any([True for sub in s if sub.isupper()]))


import math


def wrap(string, max_width):
    result = []
    for i in range(0, int(math.ceil(len(string) / max_width))):
        # print(i*max_width, i*max_width+max_width)
        result.append(string[i * max_width:i * max_width + max_width])
    return '\n'.join(result)


def solve(s):
    # return ' '.join(map(str.capitalize, s.split(' ')))
    s = list(s.split(' '))
    p = []
    for i in s:
        if i.isalpha():
            p.append(i[0].upper() + i[1:])
        else:
            p.append(i)
    return " ".join(p)


def print_formatted(number):
    """print 1 to n number in float, oct, hex, binary format."""
    spacePad = len(str(bin(number)))
    for i in range(1, number + 1):
        floatVar = str(i)
        octVar = str(oct(i)[2:])
        hexVar = str(hex(i)[2:]).upper()
        binVar = str(bin(i)[2:])
        formatFloat = ((" " * (spacePad - len(str(floatVar)) - 2)) + floatVar)
        formatOct = ((" " * (spacePad - len(str(octVar)) - 2)) + octVar)
        formatHex = ((" " * (spacePad - len(str(hexVar)) - 2)) + hexVar)
        formatBin = ((" " * (spacePad - len(str(binVar)) - 2)) + binVar)
        print(formatFloat + " " + formatOct + " " + formatHex + " " + formatBin)


import string


def print_rangoli(n):
    alpha = string.ascii_lowercase

    myList = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        # each row contains 17 characters.  n = 5, row = 4 * 5 - 3 = 17
        myList.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))

    print('\n'.join(myList[::-1]))
    print('\n'.join(myList[1:]))
