from functools import reduce

with open('input.txt') as f:
    lines = f.read()

[seeds, *maps] = lines.split('\n\n')


def make_func(name, m):
    def func(n):
        for [dst, src, l] in m:
            if src <= n < src + l:
                return dst + n - src

        return n

    return func


functions = []
ifunctions = []

for mapping in maps:
    name = mapping.split('\n')[0]
    name = name.split(' ')[0].split('-')

    mapping = [list(map(int, t.split(' '))) for t in mapping.split('\n')[1:]]
    # mapping.sort(key=lambda x: x[1])

    functions.append(make_func(name[2], mapping))

    mapping = [[src,dst,l] for [dst, src,l] in mapping]

    ifunctions.append(make_func(name[0], mapping))

ifunctions.reverse()

seeds = list(map(int, seeds.split(' ')[1:]))

part1 = min([reduce(lambda cur, m: m(cur), functions, seed) for seed in seeds])
print(f"Part 1: {part1}")

# Part 2
def is_seed(seed):
    for [start, l] in zip(seeds[0::2], seeds[1::2]):
        if start <= seed <= start + l:
            return True
    return False


loc = 0
while True:
    seed = reduce(lambda cur, m: m(cur), ifunctions, loc)

    if is_seed(seed):
        print(f"Part 2: {loc}")
        break

    loc += 1