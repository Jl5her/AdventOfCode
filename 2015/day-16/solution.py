import re

key = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def read():
    with open("input.txt") as f:
        return [parse(line) for line in f.readlines()]
    return None

def parse(line):
    a = re.findall(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line)[0]
    d = {}
    for i in range(1, 7, 2):
        d[a[i]] = a[i+1]
    return d

def check(sue):
    for k in sue:
        if int(sue[k]) != key[k]:
            return False
    return True

def check2(sue):
    for k in sue:
        if k in ["cats", "trees"] and int(sue[k]) <= key[k]:
            return False
        elif k in ["pomeranians", "goldfish"] and int(sue[k]) >= key[k]:
            return False
        elif not(k in ["cats", "trees", "pomeranians", "goldfish"]) and int(sue[k]) != key[k]:
            return False
    return True

def main():
    sues = read()

    for sue in sues:
        if check(sue):
            print("Part 1")
            print(sues.index(sue) + 1)

        if check2(sue):
            print("Part 2")
            print(sues.index(sue) + 1)

main()