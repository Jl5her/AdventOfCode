f = open('input')
lines = [int(line) for line in f.readlines()]
f.close()

for i in lines:
    for e in lines:
        if i + e == 2020:
            print(f'Part 1: {i * e}')

        for n in lines:
            if i + e + n == 2020:
                print(f'Part 2: {i * e * n}')
