with open('input.txt') as f:
    patterns = [pattern.split('\n') for pattern in f.read().split('\n\n')]


def try_horizontal(pattern, row):
    # minimum distance above or below mirror
    m = min(row, len(pattern) - row)

    for offset in range(m):
        if pattern[row - offset - 1] != pattern[row + offset]:
            return False

    return True


def find_horizontal(pattern):
    for row in range(1, len(pattern)):
        if try_horizontal(pattern, row):
            return row
    return None


def get_vertical(pattern, c):
    return [line[c] for line in pattern]


def try_vertical(pattern, col):
    # minimum distance left or right of mirror
    m = min(col, len(pattern[0]) - col)

    for offset in range(m):
        if get_vertical(pattern, col - offset - 1) != get_vertical(pattern, col + offset):
            return False
    return True


def find_vertical(pattern):
    for col in range(1, len(pattern[0])):
        if try_vertical(pattern, col):
            return col
    return None


def part1(pattern):
    h = find_horizontal(pattern)
    v = find_vertical(pattern)
    if h:
        return h * 100
    if v:
        return v
    return 0


print(f"Part 1: {sum([part1(p) for p in patterns])}")
