from math import sqrt
v = [int(i) for i in input().split()]
s = sum(v)/2
print(sqrt((s-v[0])*(s-v[1])*(s-v[2])*(s-v[3])))
