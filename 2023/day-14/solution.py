from numpy import rot90
from copy import deepcopy
import os

with open('input.txt') as f:
    grid = [list(l.rstrip()) for l in f.readlines()]


def tilt_north():
    global grid
    for r in range(1, len(grid)):
        row = grid[r]
        for c, cell in enumerate(row):
            if cell == 'O':
                new_row = r
                for new_row in range(r, -1, -1):
                    if new_row == 0 or grid[new_row - 1][c] in ['O', '#']:
                        break

                if new_row != r:
                    grid[new_row][c] = "O"
                    grid[r][c] = "."


def calculate_load():
    load = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'O':
                load += len(grid) - r
    return load


tilt_north()
print(f"Part 1: {calculate_load()}")


def print_grid():
    global grid
    os.system('clear')
    for row in grid:
        print("".join(row))
    print()


# Part 2

# Reset grid
with open('input.txt') as f:
    grid = [list(l.rstrip()) for l in f.readlines()]

loads = []
for i in range(1_000_000_000):
    for _ in range(4):
        tilt_north()
        grid = rot90(grid, axes=(1, 0))
    loads.append(calculate_load())

    for period_length in range(2, 100):
        period = loads[-period_length:]
        if loads[-period_length * 2:-period_length] == period:
            # I believe the 2 comes from i not incrementing until the end of this code block, and 0 based counting
            # since 1 iteration occurred, but i has not been incremented
            remaining = 1_000_000_000 - i - 2
            offset = remaining % period_length
            print(f"Part 2: {period[offset]}")
            exit()
