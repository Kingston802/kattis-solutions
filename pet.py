maxscore = [0,0]
for i in range(1,6):
    score = sum([int(k) for k in input().split()])
    if score > maxscore[0]:
        maxscore[0] = score
        maxscore[1] = i 

print(maxscore[1], maxscore[0])



