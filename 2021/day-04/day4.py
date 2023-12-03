numbers = []
lines = []

with open("input.txt") as f:
    numbers = [int(i) for i in f.readline().rstrip().split(",")]

    lines = [line.rstrip() for line in f.readlines()]

boards = []
cur_board = []
for line in lines:
    if line == "":
        if cur_board:
            boards.append(cur_board)
        cur_board = None
    else:
        if not(cur_board):
            cur_board = []
        line = [int(x) for x in line.split(" ") if x != ""]
        cur_board.append(line)
boards.append(cur_board)


def play_game(boards, numbers):
    part1_score = None
    part2_score = None
    for num in numbers:
        for board in boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = -1

                i_row = set(board[i])
                i_col = set(row[i] for row in board)

                if (i_row == {-1} or i_col == {-1}):
                    score = num * sum([sum([cell for cell in row if cell != -1])
                                       for row in board])
                    if score > 0:
                        part2_score = score
                    if not(part1_score):
                        part1_score = score

    return part1_score, part2_score


part1, part2 = play_game(boards, numbers)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
