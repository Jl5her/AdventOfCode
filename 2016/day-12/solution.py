import re

registry = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0
}

def read():
    with open("input.txt") as f:
        return f.readlines()
    return None

def run(step, p):
    m = re.findall(r"(\w+) (\w+)\s(.+)*", step)[0]
    if m[0] == "inc":
        registry[m[1]] += 1
        return p + 1
    elif m[0] == "dec":
        registry[m[1]] -= 1
        return p + 1
    elif m[0] == "cpy":
        registry[m[2]] = int(m[1]) if m[1].isdigit() else registry[m[1]]
        return p + 1
    elif m[0] == "jnz":
        check = int(m[1]) if m[1].isdigit() else registry[m[1]]
        if check != 0:
            return p + int(m[2])
        else:
            return p + 1
    else:
        print(step)
        return p + 1


def main():
    steps = read()

    p = 0
    while p < len(steps):
        p = run(steps[p], p)

    print(registry["a"])

# Part 2
    for k in registry:
        registry[k] = 0
    registry["c"] = 1
        
    p = 0
    while p < len(steps):
        p = run(steps[p], p)

    print(registry["a"])
    

main()