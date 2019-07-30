v = [int(i) for i in input().split()]
v = sorted(v)
sortString = input()

output = []
for char in sortString:
    if char == 'A':
        output.append(v[0])
    elif char == 'B':
        output.append(v[1])
    elif char == 'C':
        output.append(v[2])

constructedString = ''
for val in output:
    constructedString += str(val) + ' '

print(constructedString)
