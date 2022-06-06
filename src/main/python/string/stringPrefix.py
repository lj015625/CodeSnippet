"""
Given a list of strings, write a function that returns their longest common prefix.
For example, if you were given the strings “flowers”, “flow”, and “flight”, your function should return the string “fl”.

If the list of strings has no common prefix, return an empty string.
"""


def common_prefix(strings):
    prefix = ""
    # loop over min of lengths of the strings.
    for char_index in range(len(min(strings, key=len))):
        if all(string[char_index] == strings[0][char_index] for string in strings):
            prefix += strings[0][char_index]
        else:
            break
    return prefix


strings = ["showboat", "showcase", "shower"]
print(common_prefix(strings))
