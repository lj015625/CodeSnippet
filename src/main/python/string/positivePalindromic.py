def positive_palindromic(arr):
    '''all positive and any number is palindrome '''
    palindromic = any([j == j[::-1] for j in arr])
    pos = (all([int(i) > 0 for i in arr]))
    return pos and palindromic

# 121 is palindrome while 121 is not.
print(positive_palindromic(['123', '121']))