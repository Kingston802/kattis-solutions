c = float(input())
l = int(input())

total = 0
for i in range(l):
    x, y = input().split()
    total += float(x) * float(y) * c

print(total)
