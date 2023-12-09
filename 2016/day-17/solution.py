import hashlib
import sys
sys.setrecursionlimit(1500)

OPEN_DOOR = ["b", "c", "d", "e", "f"]

puzzle_input = input("Puzzle Input: ")


def get_doors(cur):
    return [i in OPEN_DOOR for i in hashlib.md5(cur.encode('utf-8')).hexdigest()[:4]]


def get_loc(cur):
    x = 0
    y = 0
    for step in cur[len(puzzle_input):]:
        if "D" == step:
            y += 1
        elif "U" == step:
            y -= 1
        elif "L" == step:
            x -= 1
        elif "R" == step:
            x += 1

    return x, y


min_length = -1


def get_path(cur, stop_at_min=True):
    global min_length

    # min length is set, and exceeded
    if stop_at_min and 0 <= min_length < len(cur):
        return

    x, y = get_loc(cur)

    if (x, y) == (3, 3):
        min_length = len(cur)
        yield cur

    up, down, left, right = get_doors(cur)
    up, down, left, right = up and y > 0, down and y < 3, left and x > 0, right and x < 3

    try:
        if up:
            yield from get_path(cur + "U", stop_at_min)
        if down:
            yield from get_path(cur + "D", stop_at_min)
        if left:
            yield from get_path(cur + "L", stop_at_min)
        if right:
            yield from get_path(cur + "R", stop_at_min)
    except RecursionError:
        print("Ignoring ")


print(f"Part 1: {sorted(get_path(puzzle_input), key=lambda x: len(x))[0][len(puzzle_input):]}")
print(sorted(get_path(puzzle_input, False), key=lambda x: len(x))[-1][len(puzzle_input):])
