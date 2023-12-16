import re

with open('input.txt') as f:
    lines = f.read().split('\n')


def gen(field, record, l):
    if '?' not in field:
        if is_valid(field, record):
            l.append(field)
        return l

    l = gen(field.replace('?', '.', 1), record, l)
    l = gen(field.replace('?', '#', 1), record, l)
    return l


def is_valid(field, record):
    return record == ",".join([str(len(m)) for m in re.findall(r'(#+)', field)])

part1 = sum([len(gen(*row.split(' '), [])) for row in lines])
print(f"Part 1: {part1}")