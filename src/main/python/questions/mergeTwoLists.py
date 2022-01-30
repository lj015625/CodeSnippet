def merge_lists(list1, list2):
    merged = []
    n = 0
    m = 0

    while n < len(list1) and m < len(list2):
        if list1[n] < list2[m]:
            merged.append(list1[n])
            n += 1
        else:
            merged.append(list2[m])
            m += 1
    merged += list1[n:] + list2[m:]
    return merged

list1 = [1,2,5]
list2 = [2,4,6]
print(merge_lists(list1, list2))