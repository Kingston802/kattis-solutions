n = int(input())

caseStrings = []
for i in range(n):
    caseStrings.append(input())
    
for case in caseStrings:
    builtString = ""
    goalString = "welcome to code jam"
    count = 0
    for char in case:
        possibleBuiltString = builtString + char
        if possibleBuiltString in goalString:
            builtString = possibleBuiltString 
        if builtString == goalString:
            count += 1                
            builtString 

        builtString

    print(count)
