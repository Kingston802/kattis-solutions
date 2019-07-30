st = input()
cs = st[0]

prevChar = ''
for char in st:
    if prevChar == '-':
        cs += char  

    prevChar = char

print(cs)

