def stopwords_stripped(paragraph, stopwords):
    """Remove stop words from paragraph
       Parameters:
           paragraph (str): the paragraph with stopwords
           stopwords (list): list of stop words
    """
    new_paragraph = ' '.join([c for c in paragraph.split() if c not in stopwords])
    return new_paragraph

stopwords = ['I', 'as', 'to', 'you', 'your', 'but', 'be', 'a']
paragraph = 'I want to figure out how I can be a better data scientist'
print(stopwords_stripped(paragraph, stopwords))
