def frequency(a):
    f = {}
    for e in a:
        f[e] = f[e] + 1 if e in f else 1
    f = sorted(f.items(), key = lambda x: x[0])
    f = sorted(f, key = lambda x: x[1], reverse= True)    
    return f

def read():
    with open("input.txt") as f:
        return f.readlines()
    return None

def part1(lines):
    message = ""
    for col in range(len(lines[0]) - 1):
        column = [row[col] for row in lines]
        freq = frequency(column)
        message += freq[0][0]
    return message

def part2(lines):
    message = ""
    for col in range(len(lines[0]) - 1):
        column = [row[col] for row in lines]
        freq = frequency(column)
        message += freq[len(freq) - 1][0]
    return message

def main():
    lines = read()

    print(part1(lines))
    print(part2(lines))
   
    
main()