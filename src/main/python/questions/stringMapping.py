def string_map(string1, string2):
    # check whether the strings are the same length
    if len(string1) != len(string2):
        return False

    char_map = dict()

    # first check string1 does not have conflict match
    for char1, char2 in zip(string1, string2):
        # assign char1
        if char1 not in char_map:
            char_map[char1] = char2
        # match char 1 with char 2
        elif char_map[char1] != char2:
            return False
    # next check string2 does not have conflict match
    for char1, char2 in zip(string1, string2):
        # assign char2
        if char2 not in char_map:
            char_map[char2] = char1
        # match char2 with char 1
        elif char_map[char2] != char1:
            return False

    return True

string1 = 'qwe'
string2 = 'asd'
assert(string_map(string1, string2) == True)

string1 = 'donut'
string2 = 'fatty'
assert(string_map(string1, string2) == False)
# cannot map two distinct characters to two equal characters


string1 = 'enemy'
string2 = 'enemy'
assert(string_map(string1, string2) == True)
# there exists a one-to-one correspondence between equivalent strings

string1 = 'enemy'
string2 = 'ymene'
assert(string_map(string1, string2) == False)
# since our correspondence must be between characters of the same index, this case returns 'False' as we must map e = y AND e = e
