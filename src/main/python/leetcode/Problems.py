array = [1,1,3,5,7,5,3]
single = []
[single.remove(x) if x in single else single.append(x) for x in array]
print(single)
# print(sum(set(array)) * 2 - sum(array))



