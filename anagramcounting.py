from sys import stdin
from math import factorial

for line in stdin:
    collection = { }
    for char in line[:-1]:
        if char not in collection:
            collection[char] = 1
        else:
            collection[char] += 1

    productOfTotalsFac = 1
    for val in collection.values():
        productOfTotalsFac *= factorial(val)

    print(factorial(len(line)-1) // productOfTotalsFac)
    
