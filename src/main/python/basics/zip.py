n, x = 5, 3

scores = ['89 90 78 93', '90 91 85 88', '91 92 83 89']

sheet = []
for i in range(x):
    sheet.append(map(float, scores[i].split()))

for i in zip(*sheet):
    print(sum(i)/len(i))

