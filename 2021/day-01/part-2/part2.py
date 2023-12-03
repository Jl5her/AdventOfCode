groups = []

with open("input.txt") as f:
    lines = [int(line.rstrip()) for line in f.readlines()]
    for i in range(len(lines) - 3):
        groups.append(sum(lines[i:i+3]))

    increased = 0
    last_val = 0
    for val in groups:
        if val > last_val:
            increased += 1
        last_val = val

    print(f"Increased: {increased}")
