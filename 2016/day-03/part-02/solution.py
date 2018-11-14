import re

def read():
    with open("../input.txt") as f:
        return [[int(s) for s in re.findall(r"(\d+)+", line)] for line in f.readlines()]
    return None

def isValid(t):
    if t[0] + t[1] <= t[2]:
        return False
    if t[1] + t[2] <= t[0]:
        return False
    if t[0] + t[2] <= t[1]:
        return False
    return True

def main():
    triangles = read()
    new_triangles = []

    for y in range(0, len(triangles), 3): # group 3 rows vertically
        for x in range(3): # each column
            triangle = [ triangles[y][x], triangles[y + 1][x], triangles[y + 2][x] ]
            new_triangles.append(triangle)

    valid_trianges = list(filter(lambda x: isValid(x), new_triangles))
    print(len(valid_trianges))

main()
