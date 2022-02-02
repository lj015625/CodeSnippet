"""
Given a dictionary with keys of letters and values of a list of letters,
write a function closest_key to find the key with the input value closest to the beginning of the list.
"""


def closest_key(dic, inp):
    nums = []
    for i in dic:
        nums.append(dic[i].index(inp))
    index = list(dic.keys())[nums.index(min(nums))]
    return index

dictionary = {
    'a' : ['b','c','e'],
    'm' : ['c','e'],
}
input = 'c'

print(closest_key(dictionary, input))

