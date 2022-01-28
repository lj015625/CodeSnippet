"""Given a list of integers, and an integer N,
   write a function sum_to_n find all combinations that that sum to the value N.
"""
integers = [2, 3, 5]
N = 8
# output = [
#     [2,2,2,2],
#     [2,3,3],
#     [3,5]
# ]

def dfs(integers, total, temp, dp, results):
    if total == 0:
        results.append(list(temp))
        return
    if total < 0:
        return
    for i in integers:
        temp.append(i)
        # try new i.
        dfs(integers, total - i, temp, dp, results)
        # remove last item because it was not useful.
        temp.remove(i)
    return

def sum_to_n(integers, total):
    results = []
    temp = []
    dp =[]
    dfs(integers, total, temp, dp, results)
    return results


print(sum_to_n(integers, N))

