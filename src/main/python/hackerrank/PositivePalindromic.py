
def positive_palindromic(arr):
    palindromic = any([j == j[::-1] for j in arr])
    pos = (all([int(i) > 0 for i in arr]))
    return pos and palindromic

print(positive_palindromic(['1', '2', '3', '4', '5', '-9']))