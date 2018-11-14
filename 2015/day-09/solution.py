import re

def permutate(cities, string, arr):
    for city in cities:
        new_cities = cities[:]
        new_cities.remove(city)
        arr = permutate(new_cities, string + city + " -> ", arr)
    if len(cities) == 0:
        arr.append(string[:-4])
    return arr

def parse_data(data):
    cities = []
    for line in data:
        for city in re.findall('(.*) to (.*) = .*', line)[0]:
            cities.append(city)
    cities = list(set(cities))

    distances = [[0 for _ in range(len(cities))] for _ in range(len(cities))]
    for line in data:
        for e in re.findall('(.*) to (.*) = (.*)', line):
            c1 = cities.index(e[0])
            c2 = cities.index(e[1])
            d = int(e[2])
            distances[c1][c2] = d
            distances[c2][c1] = d

    return cities, distances

def distance(cities, distances, perm):
    entries = perm.split(" -> ")
    last = -1
    dis = 0
    for e in entries:
        i = cities.index(e)
        if last != -1:
            dis = dis + distances[last][i]
        last = i
    return dis

with open('input.txt') as f:
    data = f.readlines()
    cities, distances = parse_data(data)

    mi = 1000000
    ma = 0

    permutations = permutate(cities, "", [])
    for p in permutations:
        dis = distance(cities, distances, p)
        if dis < mi:
            mi = dis
        if dis > ma:
            ma = dis
    print(mi)
    print(ma)