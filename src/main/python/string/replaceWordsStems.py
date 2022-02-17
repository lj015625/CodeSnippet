"""In data science, there exists the concept of stemming,
which is the heuristic of chopping off the end of a word to clean and bucket it into an easier feature set.

Given a dictionary consisting of many roots and a sentence,
write a function replace_words to stem all the words in the sentence with the root forming it.
If a word has many roots that can form it, replace it with the root with the shortest length.
"""


def replace_words(roots, sentence):
    words = sentence.split(' ')
    out_list = []
    for w in words:
        out_list.append(w)
        for r in roots:
            if w.startswith(r):
                out_list[-1] = r
    return ' '.join(out_list)


roots = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

print(replace_words(roots, sentence))
