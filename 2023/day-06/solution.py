import re

with open('input.txt') as f:
    times = re.findall(r"(\d+)", f.readline())
    distances = re.findall(r"(\d+)", f.readline())

races = [(int(times[i]), int(distances[i])) for i in range(len(times))]
big_time = int("".join(times))
big_record = int("".join(distances))

part1 = 1
for (time, record) in races:
    ways = 0

    for m in range(time + 1):
        if m * (time - m) > record:
            ways += 1

    part1 *= ways

print(f"Part 1: {part1}")

part2 = 0
for m in range(big_time + 1):
    if m * (big_time - m) > big_record:
        part2 += 1
print(f"Part 2: {part2}")
