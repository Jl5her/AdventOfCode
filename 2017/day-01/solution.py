def part1(string):
    total = 0
    for i in range(len(string)):
        if string[i] == string[(i + 1) % len(string)]:
            total += int(string[i])
    return total

def part2(string):
    total = 0
    l = len(string)
    for i in range(l):
        if string[i] == string[(i + int(l / 2)) % l]:
            total += int(string[i])
    return total

def main():
    with open("input.txt") as f:
        puzzle_input = f.readline()
        
        print(part1(puzzle_input))
        print(part2(puzzle_input))
    
main()
