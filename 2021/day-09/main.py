grid = None

with open('input.txt') as f:
    grid = [[int(c) for c in line.rstrip()]
            for line in f.readlines()]

low_points = []
basins = []


def in_bounds(r, c):
    return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])


def find_basin(r, c, visited):
    val = grid[r][c]
    basin_value = 0
    for [rt, ct] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if in_bounds(r+rt, c+ct) and (r+rt, c+ct) not in visited:
            check = grid[r+rt][c+ct]
            if check != 9 and check > val:
                visited.append((r+rt, c+ct))
                basin_value += find_basin(r+rt, c+ct, visited)
    return 1 + basin_value


for r in range(len(grid)):
    for c in range(len(grid[r])):
        val = grid[r][c]
        adj = []
        if in_bounds(r-1, c):
            adj.append(grid[r - 1][c])
        if in_bounds(r, c-1):
            adj.append(grid[r][c - 1])
        if in_bounds(r+1, c):
            adj.append(grid[r + 1][c])
        if in_bounds(r, c+1):
            adj.append(grid[r][c + 1])

        if val < min(adj):
            low_points.append(val)
            basins.append(find_basin(r, c, []))
            print()

print(f"Risk Level: {sum([i + 1 for i in low_points])}")
product = 1
for basin in sorted(basins)[-3:]:
    product *= basin
print(f"Basins: {product}")
