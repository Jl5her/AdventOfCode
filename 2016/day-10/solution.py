import re

registry = {}

def read():
    with open('input.txt') as f:
        return [line.rstrip() for line in f.readlines()]
    return None

def process(steps):
    new_steps = steps[:]
    for step in steps:
        if run(step):
            new_steps.remove(step)
            break

    return new_steps

def add(key, value):
    if key not in registry:
        registry[key] = []
    registry[key].append(int(value))

def run(step):
    give = r"bot (\d+) gives low to (\w+ \d+) and high to (\w+ \d+)"
    goes = r"value (\d+) goes to (\w+ \d+)"

    if re.match(goes, step):
        a = re.findall(goes, step)[0]
        add(a[1], a[0])
        return True
    
    if re.match(give, step):
        a = re.findall(give, step)[0]
        key = "bot " + str(a[0])
        if key in registry and len(registry[key]) == 2:
            add(a[1], min(registry[key]))
            add(a[2], max(registry[key]))
            return True
        else:
            return False

    return False

def main():
    steps = read()

    while len(steps) > 0:
        steps = process(steps)

    for key in registry:
        if registry[key] == [61, 17]:
            print(key)

    p = 1
    for o in range(3):
        p *= registry["output " + str(o)][0]
        
    print(p)
    
main()