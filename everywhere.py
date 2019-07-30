n = int(input())
output = []

trips = []
for i in range(n):
    numOfCities = int(input())
    cities = []
    for j in range(numOfCities):
        temp = input()
        cities.append(temp)

    trips.append(cities)

for trip in trips:
    known = []
    unknown = trip
    for city in trip:
        if city not in known:
            known.append(city)

    output.append(len(known))

for val in output:
    print(val)
