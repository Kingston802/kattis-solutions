inputString = input()

previousChar = ""
builtString = ""
for char in inputString:
    if char != previousChar:
        builtString = builtString + char
    
    previousChar = char

print(builtString)

