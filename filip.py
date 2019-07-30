inputList = input().split()
if int(inputList[0][::-1]) > int(inputList[1][::-1]):
    print(inputList[0][::-1])
else:
    print(inputList[1][::-1]) 
