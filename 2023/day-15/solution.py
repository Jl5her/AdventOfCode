import functools

with open('input.txt') as f:
    puzzle_input = f.read()

words = puzzle_input.split(',')
part1 = sum(map(lambda word: functools.reduce(lambda v, c: ((v + ord(c)) * 17) % 256, word, 0), words))

print(f"Part 1: {part1}")

