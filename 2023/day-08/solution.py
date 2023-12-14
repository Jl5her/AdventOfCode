import re
from math import lcm

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

current_nodes = list(filter(lambda x: x[-1] == 'A', network.keys()))

current_step = 0
steps = []

# Assuming that it is a multiple of the length of the instructions.
while len(current_nodes) > 0:
    current_step += len(instructions)

    new_current_nodes = []
    for current_node in current_nodes:
        for instruction in instructions:
            current_node = network[current_node][instruction]

        if current_node[-1] == 'Z':
            steps.append(current_step)
        else:
            new_current_nodes.append(current_node)

    current_nodes = new_current_nodes

print(f"Part 2: {lcm(*steps)}")
