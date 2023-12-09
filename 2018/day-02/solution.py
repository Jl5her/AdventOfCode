with open('input.txt') as f:
    lines = [line.rstrip() for line in f.readlines()]


def diff(line1, line2):
    return [i for i, c in enumerate(list(line1)) if c != line2[i]]


def part1():
    twos = 0
    threes = 0

    for line in lines:
        if len([c for c in set(line) if line.count(c) == 2]) > 0:
            twos += 1
        if len([c for c in set(line) if line.count(c) == 3]) > 0:
            threes += 1
    return twos * threes


def part2():
    for line1 in lines:
        for line2 in lines:
            d = diff(line1, line2)
            if len(d) == 1:
                l1 = list(line1)
                del l1[d[0]]
                return "".join(l1)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
