import re

with open("input.txt") as f:
    line = f.readline()

openers = ['{', '<']
closers = {'{': '}', '<': '>'}


def analyze(group):
    group = re.sub("!.", "", group)
    group = re.sub('<[^>]*>,*', '', group)
    group = group.replace('{', '[')
    group = group.replace('}', ']')

    return eval(group)


def count(groups):
    if len(groups) == 0:
        return 1
    return 1 + sum([count(group) for group in groups])


def score(groups, last_score=1):
    if len(groups) == 0:
        return last_score
    return last_score + sum([score(group, last_score + 1) for group in groups])


def count_garbage(line):
    line = re.sub("!.", "", line)
    return sum([len(m) for m in re.findall(r"<([^>]*)>", line)])


print(f"Part 1: {score(analyze(line))}")
print(f"Part 2: {count_garbage(line)}")
