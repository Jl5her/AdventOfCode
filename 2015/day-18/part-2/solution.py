def read():
    with open("../input.txt") as f:
        return [ list(line.rstrip()) for line in f.readlines()]
    return None

def disp(board):
    print()
    for row in board:
        print("".join(row))
    print()

def neighbors(board, pointX, pointY):
    neighbors = []
    for y in range(max(0, pointY - 1), min(pointY + 2, len(board))):
        for x in range(max(0, pointX - 1), min(pointX + 2, len(board))):
            if not(pointX == x and pointY == y):
                neighbors.append(board[y][x])
    return neighbors

def step(board):
    a = [["." for _ in range(len(board))] for _ in range(len(board))]

    width = len(board) - 1

    for y in range(0, len(board)):
        for x in range(0, len(board[y])):

            if [x,y] in [[0,0], [0,width], [width, 0], [width, width]]:
                a[y][x] = "#"
            elif board[y][x] == "#":
                a[y][x] = "#" if neighbors(board, x, y).count("#") in [2,3] else "."
            else:
                a[y][x] = "#" if neighbors(board, x, y).count("#") == 3 else "."    
    return a

def main():
    board = read()

    width = len(board) - 1
    board[0][0] = "#"
    board[0][width] = "#"
    board[width][0] = "#"
    board[width][width] = "#"

    disp(board)
    for _ in range(100):
        board = step(board)
        disp(board)
    disp(board)
    print(sum([row.count("#") for row in board]))
main()