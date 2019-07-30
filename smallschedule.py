q, m, s, l = [int(i) for i in input().split()]
tasks = []
for i in range(l): tasks.append(q)
for i in range(s): tasks.append(1)


sch = tasks[:4]
del tasks[:4]

timeTaken = 0
while len(tasks)>0:
    timeTaken += 1 
    
    print(sch)
    for idx, task in enumerate(sch): 
        if task <= 1 and len(tasks)>0:
            sch[idx] = tasks.pop(0)
        sch[idx] -= 1
            
print(timeTaken)
