import re

f = open('input.txt')
grid = f.readlines()
f.close()


exp = re.compile(r"\d+")
gears = {}

part1 = 0

for yindex, line in enumerate(grid):
    line = line.rstrip()
    numbers = exp.finditer(line)

    for num in numbers:
        xindex, end_x = num.span()

        xrange = range(max(0, xindex - 1), min(end_x + 1, len(line)))
        yrange = range(max(0, yindex - 1), min(yindex + 2, len(grid)))

        is_valid = False

        for y in yrange:
            for x in xrange:
                c = grid[y][x]
                if not c.isdigit() and c != ".":
                    is_valid = True

                if c == "*":
                    if (y,x) not in gears:
                        gears[(y,x)] = []

                    gears[(y,x)].append(int(num.group()))

        if is_valid:
            part1 += int(num.group())
print(f"Part 1: {part1}")


# Part 2
print(gears)

part2 = 0

for loc,nums in gears.items():
    if len(nums) == 2:
        part2 += nums[0] * nums[1]

print(f"Part 2: {part2}")

