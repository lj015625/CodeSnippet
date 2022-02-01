"""Given an example paragraph string and an integer N, write a function n_frequent_words
that returns the top N frequent words in the posting and the frequencies for each word.
"""
import re
import collections


def n_frequent_words(posting, n):
    posting = posting.lower()
    # remove punctuations
    posting = re.sub(r'[^\w\s]', '', posting)
    # remove stop words
    stopwords = ['I', 'as', 'to', 'you', 'your', 'but', 'be', 'a']
    words = [c for c in posting.split() if c not in stopwords]
    myMap = collections.Counter(words)
    return myMap.most_common(n)


posting = """
Herbal sauna uses the healing properties of herbs in combination with distilled water.   
The water evaporates and distributes the effect of the herbs throughout the room.   
A visit to the herbal sauna can cause real miracles, especially for colds. 
"""
n = 3
print(n_frequent_words(posting, n))