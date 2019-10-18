answers = []

for i in range(int(input())):
    sub = []
    inputString = input().split()
    b = int(inputString[0])
    p = float(inputString[1])

    # min
    sub.append(60/(p/b)-60/p) 
    # calculated bpm
    sub.append(60/(p/b)) 
    # max
    sub.append(60/(p/b)+60/p) 

    answers.append(sub)

for answer in answers:
    print("{:.4f}".format(answer[0]), "{:.4f}".format(answer[1]), "{:.4f}".format(answer[2]))
