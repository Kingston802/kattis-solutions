n = int(input())
inputList = []
for i in range(n): inputList.append(input())

for string in inputList:
    values = list(map(int,string.split()[1::]))
    avg = sum(values)/len(values)

    above = 0
    for val in values:
        if val > avg:
            above += 1

    print("{:.3f}%".format(round(((above/len(values))*100),3)))



