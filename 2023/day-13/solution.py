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


def get_value(pattern, h_func, v_func):
    h = h_func(pattern)
    v = v_func(pattern)
    if h:
        return h * 100
    if v:
        return v
    return 0


part1 = sum([get_value(p, find_horizontal, find_vertical) for p in patterns])
print(f"Part 1: {part1}")


def diff(seq1, seq2):
    return sum([0 if seq1[i] == seq2[i] else 1 for i in range(len(seq1))])


def diff_horizontal(pattern, row):
    # minimum distance above or below mirror
    m = min(row, len(pattern) - row)

    return sum([diff(pattern[row - offset - 1], pattern[row + offset]) for offset in range(m)])


def horizontal_smudge(pattern):
    for row in range(1, len(pattern)):
        if diff_horizontal(pattern, row) == 1:
            return row
    return None


def diff_vertical(pattern, col):
    # minimum distance left or right of mirror
    m = min(col, len(pattern[0]) - col)

    return sum(
        [diff(get_vertical(pattern, col - offset - 1), get_vertical(pattern, col + offset)) for offset in range(m)])


def vertical_smudge(pattern):
    for col in range(1, len(pattern[0])):
        if diff_vertical(pattern, col) == 1:
            return col
    return None


part2 = sum([get_value(p, horizontal_smudge, vertical_smudge) for p in patterns])
print(f"Part 2: {part2}")
