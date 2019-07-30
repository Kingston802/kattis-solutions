n = int(input())

prefix = "Simon says "
output = []
for i in range(n):
    instruction = input()
    if prefix in instruction:
        output.append(instruction.replace(prefix, ""))
        
for line in output:
    print(line)
