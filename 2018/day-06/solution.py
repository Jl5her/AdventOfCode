with open("input.txt") as f:
    lines = [l.rstrip() for l in f.readlines()]

limit_x = 0
limit_y = 0

coords = {}

for i, line in enumerate(lines):
    x, y = line.split(', ')
    x, y = int(x), int(y)

    coords[chr(65 + i)] = (x, y)

    limit_x = max(x, limit_x)
    limit_y = max(y, limit_y)

limit_x += 2
limit_y += 2


def dist(x1, y1, x2, y2):
    return abs(y2 - y1) + abs(x2 - x1)


def closest(x1, y1):
    d = {c: dist(x1, y1, x2, y2) for c, (x2, y2) in coords.items()}
    m = min(d.values())
    return [c for c, i in d.items() if i == m] if m > 0 else None


def sum_distance(x, y):
    return sum([dist(x, y, x1, y1) for (x1, y1) in coords.values()])


grid = [["." for _ in range(limit_x)] for _ in range(limit_y)]

for c, (x, y) in coords.items():
    grid[y][x] = c

finite = list(coords.keys())
count = {}

part2 = 0

for y in range(limit_y):
    for x in range(limit_x):
        c = closest(x, y)
        if c and len(c) == 1:
            grid[y][x] = c[0].lower()

            if y in [0, limit_y - 1] or x in [0, limit_x - 1]:
                if c[0] in finite:
                    finite.remove(c[0])

            if c[0] not in count:
                count[c[0]] = 1

            count[c[0]] += 1

        elif c and len(c) > 1:
            grid[y][x] = "."

        if sum_distance(x, y) < 10000:
            part2 += 1

min_v = 0
min_k = 0
for k in finite:
    if not min_k or count[k] > min_v:
        min_k = k
        min_v = count[k]

print(f"Part 1: {min_v}")
print(f"Part 2: {part2}")