import re
from collections import Counter

single = r"(\w+) \((\d+)\)$"
links = r"(\w+) \((\d+)\) -> (.*)"

class Program:  

    programs = []

    def __init__ (self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.parent = None

        self.children = []

        Program.programs.append(self)

    def __str__(self):
        return "{} ({}:{}) @ {} [{}]".format(self.name, self.weight, self.sweight(), self.rank(), ", ".join([child.name for child in self.children]))

    def sweight(self):
        return self.weight + sum([p.sweight() for p in self.children])

    def rank(self):
        return 0 if self.parent is None else self.parent.rank() + 1

    def print(self):
        if self.parent is not None:
            self.parent.print()
        print(self)

    def addChild(self, name):
        for p in Program.programs:
            if p.name == name:
                self.children.append(p)
                p.parent = self

def read():
    with open('input.txt') as f:
        return f.readlines()
    return None

def exists(name):
    for p in Program.programs:
        if p.name == name:
            return True
    return False

def main():
    lines = read()

    for line in lines:
        if re.match(single, line):
            a = re.findall(single, line)[0]
            program = Program(a[0], int(a[1]))
        elif re.match(links, line):
            a = re.findall(links, line)[0]
            haveChildren = True
            for c in a[2].split(", "):
                if not(exists(c)):
                    lines.append(line)
                    haveChildren = False
                    break
            if not(haveChildren):
                continue
            program = Program(a[0], int(a[1]))
            for s in a[2].split(", "):
                program.addChild(s)
        else:
            continue
        
    root = None
    for p in Program.programs:
        if p.parent == None:
            root = p
    
    checkChildren(root)

def checkChildren(p):
    if len(p.children) == 0:
        return True

    weights = [c.sweight() for c in p.children]
    c = Counter(weights)
    common_sweight = c.most_common(1)[0][0]

    for child in p.children:
        if child.sweight() != common_sweight:
            if checkChildren(child):
                print("MisMatch!", child, common_sweight, "\n\n")
                pprint(child.parent)
            return False
    return True

def pprint(prog):
    print(prog)
    for child in prog.children:
        pprint(child)


main()