import re


def set_registry(a=0, b=0, c=0, d=0):
    return {
        "a": a,
        "b": b,
        "c": c,
        "d": d,
    }


steps = []
with open("input.txt") as f:
    steps = f.readlines()


registry = set_registry(0)


def simulate(registry, limit=10):
    p = 0
    count = 0
    while p < len(steps):
        cmd, register, *extra = re.findall(r"(\w+) (\w+)\s(.+)*", steps[p])[0]
        match cmd:
            case "inc":
                registry[register] += 1
                p += 1
            case "dec":
                registry[register] -= 1
                p += 1
            case "cpy":
                registry[extra[0]] = int()
                p += 1
            case "jnz":
                check = int(register) if register.isdigit(
                ) else registry[register]
                if check != 0:
                    p += int(extra[0])
                else:
                    p += 1
            case "out":
                yield registry[register]
                p += 1
                count += 1
        if count >= limit:
            break


for a in range(10):
    print("a = %d" % a)
    for x in simulate(set_registry(a=a)):
        print("%d" % x, end=", ")
    print()
