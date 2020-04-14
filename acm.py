times = 0
count = 0

questions = {} 

while True: 
    text = input().split()
    if text[0] == '-1':
        break

    time = int(text[0])
    question = text[1]
    correct = True if text[2] == 'right' else False 

    if correct: 
        if question in questions:
            times += len(questions[question])*20 + time
            count += 1
            questions[question].append(time)
        else:
            times += time 
            count += 1
            questions[question] = [time]
    else:
        if question in questions:
            questions[question].append(time)
        else:
            questions[question] = [time]

print("{0} {1}".format(count, times))
# print(questions) 
