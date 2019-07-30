n = int(input())

for i in range(10000):
    if 2**(i-2) >= n:
        print(i-1)
        exit()

    else: 
        i += 1
