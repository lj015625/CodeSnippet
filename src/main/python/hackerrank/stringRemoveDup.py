"""repeat split string into k substring, then remove duplicate characters."""
def merge_the_tools(string, k):
    # i = 0
    # while i < len(string):
    #     a = string[i:i+k]
    #     output = ""
    #     for x in a:
    #         if x not in output:
    #             output += x
    #     print(output)
    #     i += k

    for i in range(0, len(string), k):
        a = string[i:i+k]
        d = dict()
        print(''.join([d.setdefault(c, c) for c in a if c not in d]))


print(merge_the_tools('AABCAAADA', 3))  # ABCADA