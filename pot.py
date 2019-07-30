n = int(input())

total = 0
for i in range(n):
    string = input()
    exponent = int(string[-1])
    base = int(string[:-1])

    total += base ** exponent  

print(total)
