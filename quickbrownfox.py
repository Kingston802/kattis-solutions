from string import ascii_lowercase
n = int(input())

strings = []
for i in range(n):
    strings.append(input())

for string in strings:
    alphabet = ascii_lowercase
    for letter in alphabet:
        if letter in string.lower():
            alphabet = alphabet.replace(letter, '')

    if len(alphabet) > 0:
        print(f'missing {alphabet}')
    else:
        print("pangram")

