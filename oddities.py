n = int(input())

output = []
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        output.append("{} is odd".format(num))
    else:
        output.append("{} is even".format(num))

for line in output:
    print(line)
    
