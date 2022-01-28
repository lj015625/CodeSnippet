"""Given a list of integers, and an integer N,
   write a function sum_to_n find all combinations that that sum to the value N.
"""
integers = [2, 4, 6, 8]
N = 8


def dfs(arr, total, temp, results, index):
    if total == 0:
        results.append(list(temp))
        return
    if total < 0:
        return
    # start looking each of the numbers in arr
    for i in range(index, len(arr)):
        # checking that sum does not become negative
        if(total - arr[i]) >= 0:
            temp.append(arr[i])
            # start with the same previous index
            dfs(arr, total - arr[i], temp, results, i)
            # remove last item because it was not useful
            temp.remove(arr[i])
    return

def sum_to_n(arr, total):
    results = []
    temp = []
    dfs(arr, total, temp, results, 0)
    return results


print(sum_to_n(integers, N))
