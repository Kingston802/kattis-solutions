from math import ceil
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

for v in l:
    print(ceil(v/400))

