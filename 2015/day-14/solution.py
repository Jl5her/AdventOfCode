import re

def read():
    with open("input.txt") as f:
        return [Reindeer(line) for line in f.readlines()]
    return None

def main():
    reindeers = read()

    # Part 1
    for r in reindeers:
        r.calculate(2503)
        
    print(max([r.distance for r in reindeers]))
    
    reindeers = read()

    # Part 2
    for t in range(2503):
        for r in reindeers:
            r.calculate(t + 1) # adding 1 changes range 0-2502 to 1-2503
        max_distance = max([r.distance for r in reindeers])
        for r in reindeers:
            if r.distance == max_distance:
                r.score += 1

    print(max([r.score for r in reindeers]))


class Reindeer:
    def __init__(self, line):
        a = re.findall(r"(.*) can fly (.*) km/s for (.*) seconds, but then must rest for (.*) seconds.", line)[0]
    
        self.name = a[0]
        self.speed = int(a[1])
        self.length = int(a[2])
        self.rest = int(a[3])
# 1085
        self.score = 0

    def calculate(self, time):
        distance = int(time / (self.rest + self.length)) * (self.speed * self.length)
        remain = time % (self.length + self.rest)

        distance += self.speed * self.length if remain >= self.length else self.speed * remain
        self.distance = distance


main() 