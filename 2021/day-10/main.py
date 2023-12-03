opening_items = ['(', '[', '{', '<']
closing_items = [')', ']', '}', '>']

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def score(line):
    stack = []
    for item in line:
        if item in opening_items:
            stack.append(item)
        elif item in closing_items:
            peek = stack[-1]
            if peek in opening_items:
                if peek == '(' and item != ')':
                    return scores[item], 0
                elif peek == '[' and item != ']':
                    return scores[item], 0
                elif peek == '{' and item != '}':
                    return scores[item], 0
                elif peek == '<' and item != '>':
                    return scores[item], 0
                else:
                    stack.pop()

    part2 = 0
    stack.reverse()
    for item in [opening_items.index(item) + 1 for item in stack]:
        part2 *= 5
        part2 += item

    return 0, part2


part1 = 0
part2 = []
with open('input.txt') as f:
    for line in f.readlines():
        p1, p2 = score(line)

        part1 += p1
        if p1 == 0:
            part2 += [p2]


part2.sort()
print(part2)
m = int(len(part2) / 2)

print(f"Part 1: {part1}")
print(f"Part 2: {part2[m]}")
