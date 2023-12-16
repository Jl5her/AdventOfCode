with open('input.txt') as f:
    lines = f.read().split('\n')

galaxies = []
empty_columns = []
empty_rows = []

for r, row in enumerate(lines):
    for c, cell in enumerate(row):
        if cell == '#':
            galaxies.append((c, r))
    if '#' not in row:
        empty_rows.append(r)

for c in range(len(lines[0])):
    col = [lines[r][c] for r in range(len(lines))]
    if '#' not in col:
        empty_columns.append(c)


def scale_galaxies(scale=1):
    new_galaxies = []

    for (x, y) in galaxies:
        bump_rows = sum([scale - 1 for gr in empty_rows if y > gr])
        bump_cols = sum([scale - 1 for gc in empty_columns if x > gc])

        new_galaxies.append((x + bump_cols, y + bump_rows))

    return new_galaxies


def make_pairs(g):
    return [(g[g1], g[g2]) for g1 in range(len(g)) for g2 in range(g1 + 1, len(g))]


def sum_shortest_paths(pairs):
    return sum(list(map(lambda p: abs(p[1][1] - p[0][1]) + abs(p[1][0] - p[0][0]), pairs)))


part1 = sum_shortest_paths(make_pairs(scale_galaxies(2)))
print(f"Part 1: {part1}")

part2 = sum_shortest_paths(make_pairs(scale_galaxies(1_000_000)))
print(f"Part 2: {part2}")
