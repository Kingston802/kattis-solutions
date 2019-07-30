from math import sin, radians, ceil
h, v = input().split()
print(ceil(int(h)/sin(radians(int(v)))))
