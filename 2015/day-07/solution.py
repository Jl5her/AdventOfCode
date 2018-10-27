import re

steps = []

def execute(mem, step):
    instructions = r"AND|OR|LSHIFT|RSHIFT|NOT"
    if re.search(instructions, step):
        instruction = re.findall(instructions, step)[0]

        if instruction == "NOT":
            a = re.findall(r"NOT (.*) -> (.*)", step)[0]
            if a[0] not in mem and not(a[0].isdigit()):
                return False
            mem[a[1]] = 65536 + ~(int(a[0]) if a[0].isdigit() else mem[a[0]])
            return True
                
        a = list(re.findall(r"(.*)\s(AND|OR|RSHIFT|LSHIFT)\s(.+) -> (.+)", step)[0])

        if a[0] not in mem and not(a[0].isdigit()):
            return False
        a[0] = int(a[0]) if a[0].isdigit() else mem[a[0]]

        if a[2] not in mem and not(a[2].isdigit()):
            return False
        a[2] = int(a[2]) if a[2].isdigit() else mem[a[2]]

        if instruction == "AND":
            mem[a[3]] = a[0] & a[2]
        if instruction == "OR":
            mem[a[3]] = a[0] | a[2]
        if instruction == "LSHIFT":
            mem[a[3]] = a[0] << a[2]
        if instruction == "RSHIFT":
            mem[a[3]] = a[0] >> a[2]
    else:
        a = re.findall(r"(.*) -> (.*)", step)[0]
        if a[0] not in mem and not(a[0].isdigit()):
            return False
        if a[1] in mem:
            return True
        mem[a[1]] = int(a[0]) if a[0].isdigit() else mem[a[0]]
        
    return True

def part1(steps):
    mem = {}
    while len(steps) > 0:
        step = steps.pop(0)
        if not(execute(mem, step)):
            steps.append(step)
    print(mem["a"])

def part2(steps):
    mem = {"b": 956}
    while len(steps) > 0:
        step = steps.pop(0)
        if not(execute(mem, step)):
            steps.append(step)
    print(mem["a"])

with open("input.txt") as f:
    steps = f.readlines()

    part1(steps[:])
    part2(steps[:])
