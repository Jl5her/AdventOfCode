def part1(string):
    return eval(string.replace("(", "+1").replace(")", "-1"))

def part2(string):
    for pos in range(1,len(string)):
        if part1(string[:pos]) == -1:
            return pos

with open("input.txt") as f:
    contents = f.read()
    
    print(part1(contents))
    print(part2(contents))