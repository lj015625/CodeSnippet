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
        output = ''
        d = dict()
        print(''.join([d.setdefault(c, c) for c in a if c not in d]))