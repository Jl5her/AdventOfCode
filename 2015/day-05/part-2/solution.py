import re

def part2(string):
    return re.search(r"(.)(.)\1", string) and re.findall(r"(..)(.*)\1", string)
    
with open("../input.txt") as f:
    count = 0
    for line in f.readlines():
        if part2(line):
            count += 1
    print(count)