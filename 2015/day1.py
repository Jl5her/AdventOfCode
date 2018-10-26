def part1(string):
    return eval(string.replace("(", "+1").replace(")", "-1"))

def part2(string):
    for pos in range(1,len(string)):
        if part1(string[:pos]) == -1:
            return pos
        
with open("inputs/day1_part1.txt") as f:
    print(part1(f.read()))

with open("inputs/day1_part2.txt") as f:
    print(part2(f.read()))