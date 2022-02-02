""" Given an integer array arr, write a function decreasing_values to return an array of integers so that
the subsequent integers in the array get filtered out if they are less than an integer in a later index of the array.
"""


def decreasing_values(arr):
    dic = {}

    # loop through the array store index
    for index, v in enumerate(arr):
        if v in dic:
            # if the value already exists in the dictionary and the index is
            # further down in the array, set the new index to the value
            if index > dic[v]:
                dic[v] = index
        else:
            dic[v] = index

    # create a sorted tuple of the values as the key and the indices as
    # the value
    dic = sorted(dic.items(), key=lambda x: x[0], reverse=True)
    output = []

    # set res as our second index
    res = 0

    # loop through each value in the dictionary starting with the
    # highest value
    for v, index in dic:

        # if the index is greater than the new index, then we know
        # this is the largest value. So we set the new index with the
        # largest value index.
        if index >= res:
            res = index
            output.append(v)
    return output


arr = [20, 17, 19, 18, 12, 16, 10, 4, 6, 3]
print(decreasing_values(arr))

arr = [25, 30, 21, 22, 14, 10, 5, 26]
print(decreasing_values(arr))
