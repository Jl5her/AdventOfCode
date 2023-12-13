with open("input.txt") as f:
    lines = [[int(n) for n in l.rstrip().split(' ')] for l in f.readlines()]


def append_next(seq, s=0):
    if list(set(seq)) == [0]:
        seq.append(0)
        return seq

    diff = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    diff = append_next(diff, s + 1)

    seq.append(seq[-1] + diff[-1])

    return seq


part1 = sum([append_next(seq)[-1] for seq in lines])
print(f"Part 1: {part1}")
