"""
Given a dictionary with keys of letters and values of a list of letters,
write a function closest_key to find the key with the input value closest to the beginning of the list.
"""


def closest_key(dictionary, input):
    itemIndices = []
    # iterate over each dict list and save index of input
    for i in dictionary:
        itemIndices.append(dictionary[i].index(input))

    # Find the smallest index
    smallestNum = min(itemIndices)
    smallestIndex = itemIndices.index(smallestNum)
    dictKeys = list(dictionary.keys())
    index = dictKeys[smallestIndex]
    return index


dictionary = {
    'a': ['b', 'c', 'e'],
    'm': ['c', 'e'],
}
print(closest_key(dictionary, 'c'))
