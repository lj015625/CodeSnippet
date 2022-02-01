"""Write a program in python to determine the TF (term_frequency) values for each term of this document."""

def term_frequency(sentences):
    words = sentences.split(' ')
    out_dict = {}
    if words == [""]:
        return out_dict

    for word in words:
        if word in out_dict:
            out_dict[word] += 1
        else:
            out_dict[word] = 1
    for key in out_dict.keys():
        out_dict[key] = round(out_dict[key]/len(words), 2)
    return out_dict

document = "I have a nice car with a nice tires"
print(term_frequency(document))
