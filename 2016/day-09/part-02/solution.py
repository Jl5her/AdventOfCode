import re

def read():
    with open("../input.txt") as f:
        return [line.rstrip() for line in f.readlines()]
    return None

def main():
    lines = read()
    for line in lines:
        print(calculate(line))

def calculate(line):
    m = re.findall(r"(\((\d+)x(\d+)\))(.+)", line)
    if len(m) == 0: # If there are no markers, just return the length
        return len(line)
    m = m[0]

    string = (m[3])[:int(m[1])] # string marker is affecting
    replace = m[0] + string # marker and string of marker
    calc = int(m[2]) * int(calculate(string)) # calculate string and multiply by marker 
    
    line = line.replace(replace, "") # remove marker and affected string to calculate remaining text
    return calculate(line) + calc # add remaining length and calculated length

main()