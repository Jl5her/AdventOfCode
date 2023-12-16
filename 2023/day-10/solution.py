import sys

sys.setrecursionlimit(100000)

with open('input.txt') as f:
    grid = f.read().split('\n')

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == 'S':
            start_r = r
            start_c = c

visited = []


def do_step(y, x, yd, xd, path=[]):
    global visited
    c = grid[y + yd][x + xd]

    if (x, y, y + yd, x + xd) in visited:
        return None

    visited.append((x, y, y + yd, x + xd))
    coords = [(y, x)]

    if '|' == c and abs(yd) == 1:
        return do_step(y + yd, x + xd, yd, xd, path + coords)
    elif '-' == c and abs(xd) == 1:
        return do_step(y + yd, x + xd, yd, xd, path + coords)
    elif 'L' == c and (yd == 1 or xd == -1):
        if yd == 1:
            return do_step(y + yd, x + xd, 0, 1, path + coords)
        elif xd == -1:
            return do_step(y + yd, x + xd, -1, 0, path + coords)
    elif 'J' == c and (yd == 1 or xd == 1):
        if yd == 1:
            return do_step(y + yd, x + xd, 0, -1, path + coords)
        elif xd == 1:
            return do_step(y + yd, x + xd, -1, 0, path + coords)
    elif '7' == c and (yd == -1 or xd == 1):
        if yd == -1:
            return do_step(y + yd, x + xd, 0, -1, path + coords)
        elif xd == 1:
            return do_step(y + yd, x + xd, 1, 0, path + coords)
    elif 'F' == c and (yd == -1 or xd == -1):
        if yd == -1:
            return do_step(y + yd, x + xd, 0, 1, path + coords)
        elif xd == -1:
            return do_step(y + yd, x + xd, 1, 0, path + coords)
    elif 'S' == c:
        return path


def longest_path():
    max_steps = []
    for d in range(-1, 2):
        if d == 0:
            continue

        steps = do_step(start_r, start_c, 0, d)
        if steps:
            max_steps.append(steps)

        steps = do_step(start_r, start_c, d, 0)
        if steps:
            max_steps.append(steps)
    return sorted(max_steps, key=lambda x: len(x))[0]


path = longest_path()
part1 = int((len(path) + 1) / 2)
print(f"Part 1: {part1}")