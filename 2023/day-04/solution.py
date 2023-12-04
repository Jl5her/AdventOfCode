import re

with open('input.txt') as f:
    lines = f.readlines()

points = 0
copies = {}
for i in range(len(lines)):
    copies[i + 1] = 1

for line in lines:
    [card, numbers] = re.findall(r"Card\s*(\d+):\s*(.*)", line)[0]
    numbers = numbers.split(' | ')
    card = int(card)

    winning_numbers = [int(i) for i in re.findall(r"(\d+)", numbers[0])]
    my_numbers = [int(i) for i in re.findall(r"(\d+)", numbers[1])]

    nums = sum([1 if i in winning_numbers else 0 for i in my_numbers])
    for i in range(card + 1, min(len(lines) + 1, card + nums + 1)):
        for _ in range(copies[card]):
            copies[i] = copies[i] + 1

    points += 2 ** (nums - 1) if nums > 0 else 0

print(points)
print(sum(copies.values()))
