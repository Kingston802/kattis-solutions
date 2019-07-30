from re import findall 
splitString = findall(r'[ABCDEFGHIJKLMNOPQRSTUVWXY]', input())
constructedString = ""
for char in splitString:
    constructedString = constructedString + char

print(constructedString)
