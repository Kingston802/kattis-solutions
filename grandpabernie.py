inputList = []
trips = {}

for i in range(int(input())):
    country, year = input().split()
    if country in trips:
        trips[country].append(year)
    else:
        trips[country] = [year]

for country in trips.values():
    country = country.sort()

for i in range(int(input())):
    country, count = input().split()
    inputList.append([country, count])

for country, count in inputList:
    print(trips[country][int(count)-1])

