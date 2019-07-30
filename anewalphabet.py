inputString = input().lower()
translatedString = ""

translateDict = {
    'a':'@',
    'b':'8',
    'c':'(',
    'd':'|)',
    'e':'3',
    'f':'#',
    'g':'6',
    'h':'[-]',
    'i':'|',
    'j':'_|',
    'k':'|<',
    'l':'1',
    'm':'[]\/[]',
    'n':'[]\[]',
    'o':'0',
    'p':'|D',
    'q':'(,)',
    'r':'|z',
    's':'$',
    't':'\'][\'',
    'u':'|_|',
    'v':'\/',
    'w':'\/\/',
    'x':'}{',
    'y':'`/',
    'z':'2',
}

for char in inputString:
    if char in translateDict:
        translatedString += translateDict[char]
    else:
        translatedString += char

print(translatedString)
