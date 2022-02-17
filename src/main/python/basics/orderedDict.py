from collections import OrderedDict

ordered_dictionary = OrderedDict()
n = int(input())
for _ in range(n):
    # split on right most white space
    item, space, price = input().rpartition(' ')
    ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(price)

for item, price in ordered_dictionary.items():
    print(item, price)