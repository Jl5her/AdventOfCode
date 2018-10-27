import re

def part1(string):
    return not(re.search(r"(ab|cd|pq|xy)", string)) and len(re.findall(r"(a|e|i|o|u)", string)) >= 3 and re.search(r"(.)\1", string)
    
with open("../input.txt") as f:
    count = 0
    for line in f.readlines():
        if part1(line):
            count += 1
    print(count)