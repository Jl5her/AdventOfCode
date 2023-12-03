f = open("input.txt")
pos = [int(e) for e in f.readline().split(",")]
f.close()


part1 = min([sum([abs(e-p) for e in pos])
             for p in range(min(pos), max(pos))])

print(f"Part 1: {part1}")

part2 = min([sum([sum(range(1, abs(e-p)+1)) for e in pos])
             for p in range(min(pos), max(pos))])

print(f"Part 2: {part2}")
