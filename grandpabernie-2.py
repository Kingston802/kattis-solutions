import re 
n = int(input())

trips = {}
output = []

for i in range(n):
    inputString = input().strip()
    if inputString[:-5] in trips:
        trips[inputString[:-5]].append(inputString[-4:])
    else:
        trips[inputString[:-5]] = [inputString[-4:]]

for trip in trips.values():
    trip.sort()

n = int(input())

for i in range(n):
    inputString = input()  
    search = re.search(r"[1234567890]+", inputString)
    idx = search.span()
    output.append([inputString[:idx[0]].strip(),int(inputString[idx[0]:])-1])

for trip in output:
    print(trips[trip[0]][trip[1]])
