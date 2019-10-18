out = []
n, a, b = [int(i) for i in input().split()]

max = (a**2 + b**2)**0.5
for i in range(n):
    val = int(input())
    
    if val > max:
        out.append("NE")
    else:
        out.append("DA")

for val in out:
    print(val)
