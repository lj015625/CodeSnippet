def merge_list(lst1, lst2):
    i, j = 0, 0
    res = []
    while (i < (len(lst1) - 1) or j < (len(lst2) - 1)):
        if lst1[i] <= lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    return res + lst1[i:] + lst2[j:]

list1 = [1,2,5]
list2 = [2,4,6]
print(merge_list(list1, list2))