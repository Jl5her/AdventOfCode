DEBUG = False

with open('input.txt') as f:
    lines = f.read()

[seeds, *maps] = lines.split('\n\n')

functions = []


def debug(msg='', end='\n'):
    if DEBUG:
        print(msg, end=end)


def add_func(name, m):
    def func(n):
        for [dst, src, l] in m:
            if src <= n <= src + l:
                debug(f"{name}: {dst + n - src}", end=' -> ')
                return dst + n - src

        debug(f"{name}: {n}", end=' -> ')
        return n

    functions.append(func)


for mapping in maps:
    name = mapping.split('\n')[0]
    name = name.split(' ')[0].split('-')[2]

    mapping = [list(map(int, t.split(' '))) for t in mapping.split('\n')[1:]]
    # mapping.sort(key=lambda x: x[1])

    add_func(name, mapping)

loc_seed = {}


def get_loc(seed):
    loc = seed
    debug(f"seed: {loc}", end=' -> ')
    for f in functions:
        loc = f(loc)

    debug()
    loc_seed[loc] = seed

    return seed


seeds = list(map(int, seeds.split(' ')[1:]))
print(f"Part 1: {min(map(get_loc, seeds))}")

loc_seed = {}
# DEBUG = True

mini_ranges = []
for [start, l] in zip(*[seeds[i::2] for i in range(2)]):

    for seed in range(start, start + l):
        get_loc(seed)
print([list(zip(seeds, [1] * len(seeds))), list(zip(seeds[0::2], seeds[1::2]))])

# print(f"Part 2: {min(loc_seed.keys())}")
print("Done")
