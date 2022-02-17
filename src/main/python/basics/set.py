# symmetric difference integers in ascending order
myset = set([2, 4, 5, 9])
myset2 = set([2, 4, 11, 12])
result = sorted(myset.difference(myset2).union(myset2.difference(myset)))
print('\n'.join(str(v) for v in result))
print(len(myset.symmetric_difference(myset2)))

# intersection union
a = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = set([10, 1, 2, 3, 11, 21, 55, 6, 8])
print(len(a.intersection(b)))
print(len(a.union(b)))
print(len(a.difference(b)))

# subset
a = set([1, 2, 3, 5, 6])
b = set([9, 8, 5, 6, 3, 2, 1, 4, 7])
print(a.issubset(b))

# strict superset
a = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 84, 78])
b = set([1, 2, 3, 4, 5])
print(a.issuperset(b))

# read in discard, remove, pop commands to set
n = 9
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
num_of_command = 10
commands = ['pop',
'remove 9',
'discard 9',
'discard 8',
'remove 7',
'pop',
'discard 6',
'remove 5',
'pop',
'discard 5']
for i in commands:
    cmd, *args = i.split()
    getattr(s, cmd)(*(int(x) for x in args))
print(sum(s))

# intersection_update, symmetric_difference_update
H = set("Hacker")
R = set("Rank")
H.intersection_update(R)
print(H)
#set(['a', 'k'])

H = set("Hacker")
R = set("Rank")
H.difference_update(R)
print(H)
#set(['c', 'e', 'H', 'r'])

H = set("Hacker")
R = set("Rank")
H.symmetric_difference_update(R)
print(H)
#set(['c', 'e', 'H', 'n', 'r', 'R'])

# all numbers repeating five time except one number.  Find that number.
k = 5
arr = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
myset = set(arr)
print(((sum(myset)*k)-(sum(arr))) // (k-1))

# for each item in array count +1 if x in A, -1 if x in B
arr = [1, 5, 3]
A = set(3, 1)
B = set(5, 7)
count = 0
for x in arr:
    count += 1 if x in A else -1 if x in B else 0
print(count)
# print(sum([1 if x in A else -1 if x in B else 0 for x in arr]))