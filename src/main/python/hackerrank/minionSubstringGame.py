import re
import string

def minion_game(s):
    s = s.lower()
    vowels = ['a','e','i','o','u']
    startVowelCount = 0
    for v in vowels:
        # All occurrences of vowels in string
        indices = [m.start() for m in re.finditer(v, s)]
        for index in indices:
            startVowelCount += len(s) - index
    #print('vowel', startVowelCount)

    constants = [a for a in string.ascii_lowercase if a not in vowels]
    startConstantCount = 0
    for c in constants:
        # All occurrences of constants in string
        indices = [i.start() for i in re.finditer(c, s)]
        for index in indices:
            startConstantCount += len(s) - index
    #print('constant', startConstantCount)

    if startConstantCount == startVowelCount:
        print('Draw')
    elif startConstantCount > startVowelCount:
        print('Stuart', startConstantCount)
    else:
        print('Kevin', startVowelCount)


minion_game('banana')