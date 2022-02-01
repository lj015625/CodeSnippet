"""Given an array and a target integer, write a function sum_pair_indices that returns the indices of two integers
in the array that add up to the target integer if not found such just return empty list.
Note: even though there could be many solutions, only one needs to be returned."""

def sum_pair_indices(array, target):
    index_holder = {}
    for i in range(len(array)):
        current_number = array[i]
        complement = target - current_number
        if complement in index_holder:
            return [index_holder[complement], i]
        else:
            index_holder[current_number] = i
    return []

array = [1, 2, 3, 4]
target = 5
print(sum_pair_indices(array, target))
