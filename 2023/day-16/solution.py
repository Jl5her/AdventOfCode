import sys

sys.setrecursionlimit(1_000_000_000)

with open('input.txt') as f:
    grid = f.read().split('\n')


def in_bounds(beam):
    (x, y, _, _) = beam
    if y < 0 or y >= len(grid):
        return False
    if x < 0 or x >= len(grid[0]):
        return False
    return True


def do_beams(beams, visited, energized):
    new_beams = []
    for beam in beams:
        (x, y, dx, dy) = beam

        if beam in visited:
            continue

        visited.append(beam)
        energized.add((x, y))

        c = grid[y][x]

        if '.' == c:
            new_beams.append((x + dx, y + dy, dx, dy))
        elif '|' == c:
            if dy in [-1, 1]:
                new_beams.append((x + dx, y + dy, dx, dy))
            if dx in [-1, 1]:
                new_beams.append((x, y - 1, 0, -1))
                new_beams.append((x, y + 1, 0, 1))
        elif '-' == c:
            if dx in [-1, 1]:
                new_beams.append((x + dx, y + dy, dx, dy))
            if dy in [-1, 1]:
                new_beams.append((x - 1, y, -1, 0))
                new_beams.append((x + 1, y, 1, 0))
        elif '\\' == c:
            if 1 == dx:
                new_beams.append((x, y + 1, 0, 1))
            elif -1 == dx:
                new_beams.append((x, y - 1, 0, -1))
            elif 1 == dy:
                new_beams.append((x + 1, y, 1, 0))
            elif -1 == dy:
                new_beams.append((x - 1, y, -1, 0))
        elif '/' == c:
            if 1 == dx:
                new_beams.append((x, y - 1, 0, -1))
            elif -1 == dx:
                new_beams.append((x, y + 1, 0, 1))
            elif 1 == dy:
                new_beams.append((x - 1, y, -1, 0))
            elif -1 == dy:
                new_beams.append((x + 1, y, 1, 0))

    new_beams = list(filter(in_bounds, new_beams))

    if len(new_beams) == 0:
        return energized

    return do_beams(new_beams, visited, energized)


def get_energized(x, y, dx, dy):
    return len(do_beams([(x, y, dx, dy)], [], set()))


part1 = get_energized(0, 0, 1, 0)

print(f"Part 1: {part1}")

possible = []
maxX = len(grid[0]) - 1

for y in range(len(grid)):
    possible.append(get_energized(0, y, 1, 0))
    possible.append(get_energized(maxX, y, -1, 0))

for x in range(maxX):
    possible.append(get_energized(x, 0, 0, 1))
    possible.append(get_energized(x, len(grid) - 1, 0, -1))

print(f"Part 2: {max(possible)}")
