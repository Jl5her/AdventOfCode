with open('input.txt') as f:
    puzzle_input = f.readline().rstrip()

combos = [f"{chr(i)}{chr(i).lower()}" for i in range(65, 65 + 26)]
combos.extend([c[::-1] for c in combos])


def do_step(inp):
    s = sorted([[c, inp.index(c)] for c in combos if c in inp], key=lambda x: x[1])

    if len(s) > 0:
        return True, inp.replace(s[0][0], "", 1)

    return False, inp


def reduce(inp):
    while True:
        changed, inp = do_step(inp)
        if not changed:
            break
    return len(inp)


print(f"Part 1: {reduce(puzzle_input)}")

part2 = min([reduce(puzzle_input[:].replace(chr(c), "").replace(chr(c).lower(), "")) for c in range(65, 65 + 26)])
print(f"Part 2: {part2}")
