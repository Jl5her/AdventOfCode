import re
import math

puzzle_input = "R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3"

def follow(puzzle_input):
    steps = re.findall(r"(\w)(\d+)+", puzzle_input)

    p = [0, 0]
    a = 90

    first = True
    points = []

    for step in steps:
        a += 90 if step[0] == "L" else -90
        for _ in range(int(step[1])):
            p[0] += int(math.cos(math.radians(a)))
            p[1] += int(math.sin(math.radians(a)))

            s = ",".join([str(e) for e in p])
            if s in points and first:
                print("Part 2: " + str(abs(p[0]) + abs(p[1])))
                first = False
            points.append(s)

    print("Part 1: " + str(abs(p[0]) + abs(p[1])))

def main():
    with open('input.txt') as f:
        for line in [line.rstrip() for line in f.readlines()]:
            print(line)
            follow(line)
            print()
        

main()