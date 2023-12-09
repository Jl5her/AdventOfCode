import re

with open('input.txt') as f:
    [instructions, _, *nodes] = f.readlines()

instructions = instructions.rstrip()

network = {}
for node in nodes:
    [n, l, r] = re.findall(r"(\w+) = \((\w+), (\w+)\)", node)[0]
    network[n] = {'L': l, 'R': r}

steps = 0
current_node = 'AAA'
while current_node != 'ZZZ':
    instruction = instructions[steps % len(instructions)]
    current_node = network[current_node][instruction]

    steps += 1

print(f"Part 1: {steps}")
