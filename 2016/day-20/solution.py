blocked = []
with open("input") as f:
    blocked = [line.rstrip() for line in f.readlines()]

blocked = sorted(blocked, key=lambda key: int(key.split('-')[0]))


def part1():
    i = 0

    for block in blocked:
        b = block.rstrip().split('-')

        start = int(b[0])
        end = int(b[1])

        if i >= start:
            i = end + 1
        else:
            break

    return i


def part2():
    count = 0
    b_index = 0

    i = 0
    while i < 4294967295:
        b = blocked[b_index].rstrip().split('-')
        start = int(b[0])
        end = int(b[1])

        if i >= start:
            if end > i:
                i = end + 1
            b_index += 1
            if b_index >= len(blocked):
                break
        else:
            next_b = blocked[b_index + 1].rstrip().split('-')
            next_start = int(next_b[0])
            next_end = int(next_b[1])

            if end < next_start:
                count += (next_start - end + 1)
            i = (next_end + 1)

    return count


print(part1())
print(part2())
