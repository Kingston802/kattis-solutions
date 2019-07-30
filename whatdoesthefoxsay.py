n = int(input())
outputList = []

for i in range(n):
    sounds = input().split()
    while True:
        statement = input()
        if statement == "what does the fox say?":
            break 

        sound = statement[statement.index('goes') + 5:]
        sounds = [s for s in sounds if s != sound]


    outputList.append(sounds) 

for output in outputList:
    for item in output:
        print(item, end=' ')
    print()
