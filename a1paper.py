n = int(input())
amounts = [int(i) for i in input().split()]
used = [0] * len(amounts)



tapelength = 0
for size, amount in enumerate(used):
    tapelength += (2**(-5/4) / 2**(size-2)) * amount

print(tapelength)
