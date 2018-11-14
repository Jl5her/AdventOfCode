import re

def toString(a):
    return "".join([chr(e) for e in a])

def toList(s):
    return [ord(e) for e in s]

def check1(a):
    for i in range(len(a) - 2):
        if a[i:i+3] == [i for i in range(a[i], a[i+2] + 1)]:
            return True
    return False

def check2(a):
    s = toString(a)
    return len(re.findall(r"[i,o,l]", s)) == 0

def check3(a):
    s = toString(a)
    return len(re.findall(r"(.)\1.*(.)\2", s)) > 0

def next(a):
    for index in [7-i for i in range(8)]:
        a[index] = a[index] + 1 
        if a[index] > 122:
            a[index] = 97
            continue
        return
    return 

def checkAll(a):
    return check1(a) and check2(a) and check3(a)

puzzle_input = toList("hxbxwxba")

while not(checkAll(puzzle_input)):
    next(puzzle_input)
    print(puzzle_input)

print(toString(puzzle_input))
next(puzzle_input)

while not(checkAll(puzzle_input)):
    next(puzzle_input)
    print(puzzle_input)

print(toString(puzzle_input))