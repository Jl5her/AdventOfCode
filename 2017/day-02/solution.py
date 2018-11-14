def part2(data):
    t = 0
    for row in data:
        for e1 in row:
            for e2 in row:
                if e1 != e2 and e1 % e2 == 0:
                    t += e1 / e2    
    return t

with open("input.txt") as f:
    data = [[int(val) for val in row.split("\t")] for row in f.readlines()]

    # Part 1
    print(sum([max(r) - min(r) for r in data]))
    print(part2(data))