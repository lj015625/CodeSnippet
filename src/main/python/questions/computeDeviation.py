input = [
    {
        'key': 'list1',
        'values': [4,5,2,3,4,5,2,3],
    },
    {
        'key': 'list2',
        'values': [1,1,34,12,40,3,9,7],
    }
]
# output -> {'list1': 1.12, 'list2': 14.19}

import numpy as np


def compute_deviation(list_numbers):
    output = {}
    for item in list_numbers:
        arr = np.array(item['values'])
        output[item['key']] = round(np.std(arr, axis=None), 2)

    return output


print(compute_deviation(input))
