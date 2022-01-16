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