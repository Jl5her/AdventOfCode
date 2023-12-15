from functools import reduce

with open('input.txt') as f:
    puzzle_input = f.read()

words = puzzle_input.split(',')
part1 = sum(map(lambda word: reduce(lambda v, c: ((v + ord(c)) * 17) % 256, word, 0), words))

print(f"Part 1: {part1}")

# Part 2
boxes = {}
for i in range(256):
    boxes[str(i)] = []

for word in words:
    op = "=" if "=" in word else "-"
    op_index = word.index(op)

    label = word[:op_index]
    focal_length = word[op_index + 1:]

    box = str(reduce(lambda v, c: ((v + ord(c)) * 17) % 256, label, 0))

    if op == "=":
        index = -1
        for i, l in enumerate(boxes[box]):
            if label in l:
                index = i

        lens = f"{label} {focal_length}"

        if index == -1:
            boxes[box].append(lens)
        else:
            boxes[box][index] = lens
    elif op == "-":
        boxes[box] = [b for b in boxes[box] if label not in b]

part2 = 0
for b,box in boxes.items():
    if len(box) != 0:
        for l, lens in enumerate(box):
            part2 += (int(b) + 1) * (l + 1) * int(lens.split(' ')[1])


print(f"Part 2: {part2}")