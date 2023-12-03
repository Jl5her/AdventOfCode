import re

with open("input.txt") as f:
    lines = f.readlines()
    parsed_lines = []

    max_x = 0
    max_y = 0

    for line in lines:
        g = re.findall(r"(\d+)\,(\d+) \-> (\d+)\,(\d+)", line.rstrip())[0]

        y1 = int(g[0])
        x1 = int(g[1])
        y2 = int(g[2])
        x2 = int(g[3])

        parsed_lines.append([y1, x1, y2, x2])

        max_x = max(x1, x2, max_x)
        max_y = max(y1, y2, max_y)

    part1_board = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    part2_board = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for y1, x1, y2, x2 in parsed_lines:
        if x1 == x2 or y1 == y2:
            x1_ = min(x1, x2)
            x2 = max(x1, x2)
            x1 = x1_
            y1_ = min(y1, y2)
            y2 = max(y1, y2)
            y1 = y1_
        if x1 == x2:
            for y in range(y1, y2 + 1):
                part1_board[x1][y] += 1
                part2_board[x1][y] += 1

        elif y1 == y2:
            for x in range(x1, x2 + 1):
                part1_board[x][y1] += 1
                part2_board[x][y1] += 1

        else:
            ix = x1
            iy = y1
            for _ in range(abs(x2-x1) + 1):
                part2_board[ix][iy] += 1
                ix += 1 if x1 < x2 else -1
                iy += 1 if y1 < y2 else -1


# for row in part2_board:
#     print("".join(["." if e == 0 else str(e) for e in row]))

print(
    f"Part 1 = {sum([sum([1 if cell >= 2 else 0 for cell in row]) for row in part1_board])}")
print(
    f"Part 2 = {sum([sum([1 if cell >= 2 else 0 for cell in row]) for row in part2_board])}")
