import re

def read():
    with open('input.txt') as f:
        return [row.rstrip().split(" ") for row in f.readlines()]

def isValid(p):
    for w1 in p:
        for w2 in p:
            if w1 != w2 and sorted(w1) == sorted(w2):
                return False
    return True

def main():
    passphrases = read()

    valid = [p for p in passphrases if len(p) == len(set(p))]
    valid2 = [p for p in valid if isValid(p)]

    print(len(valid))
    print(len(valid2))
    
main()