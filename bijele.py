chessPieces = list(map(int, input().split()))
requiredAmount = [1,1,2,2,2,8,8]
changes = []

for i in range(6):
    changes.append(requiredAmount[i] - chessPieces[i])

for change in changes: 
    print(change, end=' ')
print()

