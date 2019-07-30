opened = [False]*100

#for x in range(0,100):
#    for i in range(x, len(opened), x+1):
#        opened[i-1] = not opened[i-1]

for i in range(100):
    for j in range(i, 100, i+1): 
        opened[j] = not opened[j]

print(opened)
print(opened.count(1)) 

for idx, val in enumerate(opened):
    if val:
        print(idx+1)
