x, y, n = input().split()

for i in range(int(n)):
    outputString = ""
    if (i+1) % int(x) == 0:
        outputString += "Fizz"
    if (i+1) % int(y) == 0:
        outputString += "Buzz"
    if (i+1) % int(y) != 0 and (i+1) % int(x) != 0:
        outputString += str(i+1)

    print(outputString)
