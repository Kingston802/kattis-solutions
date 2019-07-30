n = int(input())
atbats = [int(i) for i in input().split()]

total = 0
for val in atbats:
    if val==-1:
        n-=1
        continue

    total += val

print(total/n)
