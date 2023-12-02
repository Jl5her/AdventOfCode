import re

f = open('input.txt')

lines = f.readlines()

total = 0

colors = ['red', 'green', 'blue']

for line in lines:
    [game_num, game] = re.findall(r"Game (\d+): (.*)", line)[0]

    power = 1
    for color in colors:
        regex = re.compile(f"(\d+) {color}")
        color_combo = re.findall(regex, line)

        power *= max([int(i) for i in color_combo])

    total += power


print(total)

f.close()
