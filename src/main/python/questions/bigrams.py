sentence = """
Have free hours and love children? 
Drive kids to school, soccer practice 
and other activities.
"""

def create_bigram(sentence):
    bigrams = []
    words = sentence.split()
    # iterate over two lists words and words skip 1st element.
    for w1, w2 in zip(words, words[1:]):
        bigrams.append(tuple([w1, w2]))
    return bigrams
print(create_bigram(sentence))
