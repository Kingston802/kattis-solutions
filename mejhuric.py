def isSorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

unsorted = [int(i) for i in input().split()]
while True:
    for idx in range(len(unsorted)):
        if isSorted(unsorted):
            quit() 
        
        if idx + 1 < len(unsorted):
            if unsorted[idx] > unsorted[idx+1]:
                unsorted[idx], unsorted[idx+1] = unsorted[idx+1], unsorted[idx]
                output = ""
                for char in unsorted:
                    output += str(char) + ' '
                print(output)



