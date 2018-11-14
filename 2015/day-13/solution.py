import re

PART2 = False

def makeOptions(arr, people, a):
    for p in people:
        new_people = people[:]
        new_people.remove(p)
        new_a = a[:]
        new_a.append(p)  
        arr = makeOptions(arr, new_people, new_a)
    if len(people) == 0:
        arr.append(a)
    return arr
        
def calculate(a, happy):
    total = 0
    for b in range(len(a)):
        c = (b + 1) % len(a)

        if a[c] == "You" or a[b] == "You":
            continue

        total += happy[a[b]][a[c]]
        total += happy[a[c]][a[b]]
    return total


with open('input.txt') as f:

    people = ["You"] if PART2 else []
    happy = {}

    for line in f.readlines():
        a = re.findall(r"(.*) would (gain|lose) (\d*) happiness units by sitting next to (.*).", line)[0]
        if a[0] not in happy:
            happy[a[0]] = {}

        change = +1 if a[1] == "gain" else -1
        happy[a[0]][a[3]] = change * int(a[2])

        people.append(a[0])
        people.append(a[3])


    people = list(set(people)) # Remove duplicates
    options = makeOptions([], people, []) # Make array of all possible seating arrangements

    ma = 0
    for option in options:
        if calculate(option, happy) > ma:
            ma = calculate(option, happy)
    
    print("Max: " +str(ma))