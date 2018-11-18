import re

hlf = r"hlf (\w)"
tpl = r"tpl (\w)"
inc = r"inc (\w)"
jmp = r"jmp (\W\d+)"
jie = r"jie (\w), (\W\d+)"
jio = r"jio (\w), (\W\d+)"

def read():
    with open('input.txt') as f:
        return [line.rstrip() for line in f.readlines()]
    return None

def run(instructions, register):
    i = 0
    while True:
        if i >= len(instructions):
            break
        instr = instructions[i]
        if re.match(hlf, instr):
            a = re.findall(hlf, instr)[0]
            register[a[0]] = int(int(register[a[0]]) / 2) if a[0] in register else 0
        elif re.match(tpl, instr):
            a = re.findall(tpl, instr)[0]
            register[a[0]] = int(register[a[0]]) * 3 if a[0] in register else 0
        elif re.match(inc, instr):
            a = re.findall(inc, instr)[0]
            register[a[0]] = int(register[a[0]]) + 1 if a[0] in register else 1 
        elif re.match(jmp, instr):
            a = re.findall(jmp, instr)[0]
            i += int(a)
            continue
        elif re.match(jio, instr):
            a = re.findall(jio, instr)[0]
            if int(register[a[0]]) == 1:
                i += int(a[1])
                continue
        elif re.match(jie, instr):
            a = re.findall(jie, instr)[0]
            if int(register[a[0]]) % 2 == 0:
                i+= int(a[1])
                continue
        else:
            print("ERROR: could not find instruction for '" + instr + "'")
        i += 1

    return register

def main():
    instructions = read()   

    register = {"a": 0, "b": 0}
    print(run(instructions, register))

    register2 = {"a": 1, "b": 0}
    print(run(instructions, register2))

    
main()