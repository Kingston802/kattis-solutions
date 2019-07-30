x = int(input())
n = int(input())
total = 0
for i in range(n):
    amountLeft = x - int(input())
    total += amountLeft

print(total+x)
