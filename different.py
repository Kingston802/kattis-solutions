from sys import stdin

inputList = []
for line in stdin:
    a, b = line.split()
    inputList.append((a,b))

for value in inputList:
    print(abs(int(value[0])-int(value[1])))
