import re

board = [["." for _ in range(50)] for _ in range(6)]

def read():
    with open("input.txt") as f:
        return [line.rstrip() for line in f.readlines()]
    return None

def disp():
    print()
    for row in board:
        print("".join(row))
    print()

def rect(width, height):
    for x in range(width):
        for y in range(height):
            board[y][x] = "#"

def rotateRow(row, by):
    old_board = board[:]

    w = len(old_board[row])
    return [[old_board[y][(x - by) % w] if y == row else old_board[y][x] for x in range(len(old_board[y]))] for y in range(len(old_board))]

def rotateCol(col, by):
    old_board = board[:]

    h = len(old_board)
    return [[old_board[(y - by) % h][x] if x == col else old_board[y][x] for x in range(len(old_board[y]))] for y in range(len(old_board))]

def process(steps):
    global board
    for step in steps:
        if re.match(r"rect (\d+)x(\d+)", step):
            m = re.findall(r"rect (\d+)x(\d+)", step)[0]
            rect(int(m[0]), int(m[1]))
        elif re.match(r"rotate row y=(\d+) by (\d+)", step):
            m = re.findall(r"rotate row y=(\d+) by (\d+)", step)[0]
            board = rotateRow(int(m[0]), int(m[1]))
        elif re.match(r"rotate column x=(\d+) by (\d+)", step):
            m = re.findall(r"rotate column x=(\d+) by (\d+)", step)[0]
            board = rotateCol(int(m[0]), int(m[1]))
        else:
            continue

def main():
    steps = read()
    process(steps)
    
    disp()

    total = 0
    for row in board:
        total += row.count("#")
    print(total)
    
main()