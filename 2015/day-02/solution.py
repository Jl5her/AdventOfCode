def part1(string):
    s = string.split("x")
    l = int(s[0])
    w = int(s[1])
    h = int(s[2])
    
    sides = [l*w,l*h,w*h]

    return (2 * sides[0]) + (2 * sides[1]) + (2 * sides[2]) + min(sides)

def part2(string):
    s = string.split("x")
    l = int(s[0])
    w = int(s[1])
    h = int(s[2])

    area = l * w * h
    perimeter = 2 * (l + w + h - max(l,w,h))
    return perimeter + area

with open("input.txt") as f:
    paper = 0
    ribbon = 0

    for line in f.readlines():
        paper += part1(line)
        ribbon += part2(line)
        
    print(paper)
    print(ribbon)