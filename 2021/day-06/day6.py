def simulate(fish, num_days):
    for _ in range(num_days):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
    return len(fish)


with open("input.txt") as f:
    lanternfish = [int(i) for i in f.readline().split(",")]

    # print(f"Part 1: {simulate(lanternfish, 80)}")
    print(f"Part 2: {simulate([3], 256)}")
