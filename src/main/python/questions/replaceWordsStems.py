
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