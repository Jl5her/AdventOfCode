def read():
    with open('input.txt') as f:
        return [int(line) for line in f.readlines()]
    return None

def part1(maze):
    i = 0
    steps = 0
    while i < len(maze):
        step = maze[i]
        maze[i] += 1
        i += step
        steps += 1
    
    return steps

def part2(maze):
    i = 0
    steps = 0
    while i < len(maze):
        step = maze[i]
        maze[i] += 1 if step < 3 else -1
        i += step
        steps += 1
    
    return steps

def main():
    maze = read()

    print(part1(maze[:]))
    print(part2(maze[:]))
main()