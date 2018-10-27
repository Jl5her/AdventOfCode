import re

lights = [[0 for _ in range(1000)] for _ in range(1000)]

def parse(step):
    a = re.findall(r"(.*)\s(\d+),(\d+).*\s(\d+),(\d+)", step)[0]

    for x in range(int(a[1]), int(a[3]) + 1):
        for y in range(int(a[2]), int(a[4]) + 1):
            if a[0] == "turn off":
                lights[x][y] += -1 if lights[x][y] > 0 else 0
            elif a[0] == "turn on":
                lights[x][y] += 1
            elif a[0] == "toggle":
                lights[x][y] += 2

with open("../input.txt") as f:
    for line in f.readlines():
        parse(line)
    
    count = 0
    for row in lights:
        for light in row:
            count += light
    print(count)