from collections import Counter 
  
def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0] 
    
possibilities = []

a, b = [int(i) for i in input().split()]
for i in range(1, a+1):
    for j in range(1, b+1):
        possibilities.append(i+j)


print(most_frequent(possibilities)) 
