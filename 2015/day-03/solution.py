def part1(string):
    a = ["0,0"]
    x = 0
    y = 0
    for s in string:
        if s == "^":
            y += 1
        if s == ">":
            x += 1
        if s == "v":
            y -= 1
        if s == "<":
            x -= 1
        a.append( str(x) + "," + str(y) )
    return len(set(a))

def part2(string):
    a = ["0,0"]
    c = 1
    p = [ [0,0], [0, 0]]
    for s in string:
        if s == "^":
            p[0 if c > 0 else 1][1] += 1
        if s == ">":
            p[0 if c > 0 else 1][0] += 1
        if s == "v":
            p[0 if c > 0 else 1][1] -= 1
        if s == "<":
            p[0 if c > 0 else 1][0] -= 1
        a.append( str(p[0][0]) + "," + str(p[0][1]) )
        a.append( str(p[1][0]) + "," + str(p[1][1]) )
        c *= -1
    return len(set(a))


with open("input.txt") as f:
    string = f.read()
    print(part1(string))
    print(part2(string))