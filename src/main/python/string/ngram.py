"""Write a function get_ngrams to take in a word (string) and return a dictionary of n-grams and their frequency in the given string.
"""


def get_ngrams(n, string):
    d = {}
    # range end at index + 1
    for i in range(len(string) - n + 1):
        temp = string[i:i + n]
        if temp in d:
            d[temp] += 1
        else:
            d[temp] = 1
    return d


string = 'banana'
n = 2
print(get_ngrams(n, string))

string = 'banana'
n = 3
print(get_ngrams(n, string))
