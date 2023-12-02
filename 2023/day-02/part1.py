import re

f = open('input.txt')

lines = f.readlines()

total = 0

colors = {
    'red': 12,
    'green': 13,
    'blue': 14
}

for line in lines:
    [game_num, game] = re.findall(r"Game (\d+): (.*)", line)[0]

    valid = True

    for color, color_max in colors.items():
        regex = re.compile(f"(\d+) {color}")
        color_combo = re.findall(regex, game)

        for i in color_combo:
            if int(i) > color_max:
                valid = False
                break

    if valid:
        total += int(game_num)

print(total)

f.close()