part1_horizontal = 0
part2_horizontal = 0
part1_depth = 0
part2_depth = 0
aim = 0

with open("input.txt") as f:
    for line in f.readlines():
        parsed = line.split(" ")
        command = parsed[0]
        X = int(parsed[1])

        if command == "down":
            part1_depth -= X
            aim -= X
        elif command == "up":
            part1_depth += X
            aim += X
        elif command == "forward":
            part1_horizontal += X
            part2_horizontal += X
            part2_depth += aim * X

print("Part 1:")
print(f"Horizontal = {part1_horizontal}")
print(f"Depth = {part1_depth}")
print(f"Product = {abs(part1_horizontal * part1_depth)}")

print("Part 2:")
print(f"Horizontal = {part2_horizontal}")
print(f"Depth = {part2_depth}")
print(f"Aim = {aim}")
print(f"Product = {abs(part1_horizontal * part2_depth)}")
