import re

def main():
    with open("../input.txt") as f:
        line = f.readline()
        print(len(apply(line)))

def apply(string):
    while "(" in string:
        for m in re.findall(r"(\((\d+)x(\d+)\))(.+)", string):
            repeating_string = (m[3])[:int(m[1])]
            
            old = m[0] + repeating_string
            new = "".join([repeating_string for _ in range(int(m[2]))])

            new = new.replace("(", "[")
            new = new.replace(")", "]")

            string = string.replace(old, new)
    return string

main()