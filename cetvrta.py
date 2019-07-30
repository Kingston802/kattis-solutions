x_values = set()
y_values = set()

for i in range(3):
    point = [int(i) for i in input().split()]
    if point[0] in x_values:
        x_values.remove(point[0])
    else:
        x_values.add(point[0])
    if point[1] in y_values:
        y_values.remove(point[1])
    else:
        y_values.add(point[1])

print(x_values.pop(), y_values.pop())
