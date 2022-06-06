"""The score of a single word is 2 if the word contains an even number of vowels. Otherwise, the score of this word is 1.
The score for the whole list of words is the sum of scores of all words in the list.
"""


def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0
    for word in words.split():
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        # add 2 for even number of vowels
        if num_vowels % 2 == 0:
            score += 2
        # add 1 for odd number of vowels
        else:
            score += 1
    return score


print(score_words("programming is awesome"))
