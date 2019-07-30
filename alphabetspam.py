spam = input()

capitalCount = lowerCount = whiteCount = symbolCount = 0
for char in spam:
    if char in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        capitalCount += 1
    elif char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        lowerCount += 1
    elif char == '_':
        whiteCount += 1
    else:
        symbolCount += 1

print(whiteCount/len(spam))
print(lowerCount/len(spam))
print(capitalCount/len(spam))
print(symbolCount/len(spam))
