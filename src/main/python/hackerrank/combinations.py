from itertools import combinations

def sortedCombination(s,n):
    """sorted combinations of 1 to n """
    for i in range(1, int(n)+1):
        for j in combinations(sorted(s), i):
            print(''.join(j))

#sortedCombination('hack', 2)


from itertools import combinations_with_replacement
def sortedCombinationWithReplacement(s,n):
    """sorted combinations with replacement of n length subsequences of elements from the input iterable allowing individual elements to be repeated more than once."""
    for c in combinations_with_replacement(sorted(s), int(n)):
        print("".join(c))
sortedCombination('hack', 2)