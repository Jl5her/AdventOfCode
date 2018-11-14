keypad = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def add(v1, v2):
    x = min(2, max(0, v1[0] + v2[0]))
    y = min(2, max(0, v1[1] + v2[1]))
    return [x,y]

def read():
    with open("../input.txt") as f:
        return [list(line.rstrip()) for line in f.readlines()]
    return None

def main():
    lines = read()

    p = [1,1]

    code = ""
    for line in lines:
        for step in line:
            if step == "U":
                p = add(p, [0, -1])
            elif step == "D":
                p = add(p, [0, 1])
            elif step == "L":
                p = add(p, [-1, 0])
            elif step == "R":
                p = add(p, [1, 0])
        code += str(keypad[p[1]][p[0]])
    print(code)


main()
