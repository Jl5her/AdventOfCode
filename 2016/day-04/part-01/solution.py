import re

def read():
    with open("../input.txt") as f:
        return [line.rstrip() for line in f.readlines()]
    return None

def isValid(room):
    m = re.findall(r"(.*)-(\d+)\[([a-z]+)\]", room)[0]
    name = m[0].replace("-", "") # get the name without the dashes
    checksum = m[2]
    f = frequency(name) # get the frequency of each letter sorted
    f = [x[0] for x in f] # extract the letters from order
    check = "".join(f[:5]) # put arry into string
    
    return check == checksum # if calculated checksum matches listed checksum

def frequency(word):
    f = {}
    for l in word:
        if not(l in f):
            f[l] = 1
        else:
            f[l] += 1
    f = sorted(f.items(), key = lambda x: x[0])
    f = sorted(f, key = lambda x: x[1], reverse= True)    
    return f

def main():
    rooms = read()
    
    valid_rooms = list(filter(lambda x: isValid(x), rooms))

    total = 0
    for room in valid_rooms:
        secId = int(re.findall(r"(.*)-(\d+)\[([a-z]+)\]", room)[0][1])
        total += secId

    print(total)

main()