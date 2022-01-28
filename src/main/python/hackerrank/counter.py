import collections

numShoes = int(input())
inventory = collections.Counter(map(int, input().split()))
numCust = int(input())

income = 0
for i in range(numCust):
    # read size and price to pay
    size, price = map(int, input().split())
    if inventory[size]:
        income += price
        inventory[size] -= 1

print(income)

# get top 3 most frequent letter
s = 'aabbbccde'
myMap = collections.Counter(sorted(list(s)))
print(" ".join((t[0], t[1]) for t in myMap.most_common(3)), sep='\n')
# for x in myMap.most_common(3):
#     print(x[0], x[1])
