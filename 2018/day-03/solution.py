import re

with open('input.txt') as f:
    lines = [l.rstrip() for l in f.readlines()]

grid = [[0 for _ in range(1000)] for _ in range(1000)]

sq = 0
for line in lines:
    [iX, iY, w, h] = re.findall(r"(\d+),(\d+): (\d+)x(\d+)", line)[0]
    iX, iY, w, h = int(iX), int(iY), int(w), int(h)

    for x in range(iX, iX + w):
        for y in range(iY, iY + h):
            grid[x][y] += 1
            if grid[x][y] == 2:
                sq += 1

print(sq)

for line in lines:
    [claim, iX, iY, w, h] = re.findall(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)[0]
    iX, iY, w, h = int(iX), int(iY), int(w), int(h)

    overlap = False
    for x in range(iX, iX + w):
        for y in range(iY, iY + h):
            if grid[x][y] != 1:
                overlap = True

    if not overlap:
        print(claim)
