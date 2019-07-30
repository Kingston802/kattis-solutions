valOne, valTwo, valThree = input().split()

if int(valOne) + int(valTwo) == int(valThree):
    print(valOne + '+' + valTwo + '=' + valThree)
elif int(valOne) == int(valTwo) + int(valThree):
    print(valOne + '=' + valTwo + '+' + valThree)

elif int(valOne) - int(valTwo) == int(valThree):
    print(valOne + '-' + valTwo + '=' + valThree)
elif int(valOne) == int(valTwo) - int(valThree):
    print(valOne + '=' + valTwo + '-' + valThree)

elif int(valOne) * int(valTwo) == int(valThree):
    print(valOne + '*' + valTwo + '=' + valThree)
elif int(valOne) == int(valTwo) * int(valThree):
    print(valOne + '=' + valTwo + '*' + valThree)

elif int(valOne) / int(valTwo) == int(valThree):
    print(valOne + '/' + valTwo + '=' + valThree)
elif int(valOne) == int(valTwo) / int(valThree):
    print(valOne + '=' + valTwo + '/' + valThree)
