"""Given an array of words and a max_width parameter, write a function justify to format the text
such that each line has exactly max_width characters.
Pad extra spaces ‘ ’ when necessary so that each line has exactly max_width characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, place excess spaces on the right-hand side of each line.
"""

def justify(words, max_width):
    res = []
    current = []
    num_of_letters = 0

    for w in words:
        #check if existing words + new words are greater than max width
        if num_of_letters + len(w) + len(current) > max_width:
            #add (max_width - num_of_letters) spaces
            for i in range(max_width - num_of_letters):
                # only more than two words in current then we add between words
                if len(current) >= 2:
                    between_words = len(current) - 1
                    current[i % between_words] += ' '
                else:
                    # only 1 word then add spaces after the word
                    current[0] += ' '
            res.append(''.join(current))
            current, num_of_letters = [], 0
        current += [w]
        num_of_letters += len(w)
    return res + [' '.join(current).ljust(max_width)]

words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 16
print(justify(words, max_width))

words = ["A", "no", "can", "mess", "twins"]
max_width = 5
print(justify(words, max_width))

words = ['A', 'no', 'can', 'mess', 'twins', 'shorts']
max_width = 7
print(justify(words, max_width))

words = ['This', 'says', 'your', 'fork', 'aint', 'cool']
max_width = 4
print(justify(words, max_width))


