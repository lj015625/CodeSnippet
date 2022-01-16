from collections import OrderedDict

ordinary_dictionary = OrderedDict()
n = int(input())
for _ in range(n):
    # split on right most white space
    item, space, price = input().rpartition(' ')
    ordinary_dictionary[item] = ordinary_dictionary.get(item, 0) + int(price)

for item, price in ordinary_dictionary.items():
    print(item, price)