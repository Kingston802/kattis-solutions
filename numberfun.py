n = int(input())

possible = []
for i in range(n):
    a, b, c = [int(i) for i in input().split()]

    passed = False
    operations = ['+', '-', '/', '*']
    for op in operations:
        if eval('{} {} {} == {}'.format(a, op, b, c)):
            possible.append(True)
            passed = True
            break
        elif eval('{} {} {} == {}'.format(b, op, a, c)) and not passed:
            possible.append(True)
            passed = True
            break

    if not passed:
        possible.append(False)


for val in possible:
    if val:
        print("Possible")
    else:
        print("Impossible")

