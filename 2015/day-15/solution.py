import re

def read():
    with open("input.txt") as f:
        return [Ingredient(line) for line in f.readlines()]
    return None

def genCombos(arr, current, mi, ma, count):
    if sum(current) > ma:
        return arr
    if len(current) == count:
        if sum(current) == 100:
            arr.append(current)
    else:
        for i in range(mi, ma):
            new_current = current[:]
            new_current.append(i)
            arr = genCombos(arr, new_current, mi, ma, count)
    return arr

def calculateHappy(ingredients, combo):
    c = 0 # Capacity
    d = 0 # Durability
    f = 0 # Flavor
    t = 0 # Texture

    for i in range(len(combo)): 
        c += combo[i] * ingredients[i].capacity
        d += combo[i] * ingredients[i].durability
        f += combo[i] * ingredients[i].flavor
        t += combo[i] * ingredients[i].texture

    return max(c, 0) * max(d, 0) * max(f, 0) * max(t, 0)

def calculateHappyPt2(ingredients, combo):
    happy = calculateHappy(ingredients, combo)
    calories = sum([combo[i] * ingredients[i].calories for i in range(len(combo))])
    
    return happy if calories == 500 else 0
    
def main():
    ingredients = read()

    combos = genCombos([], [], 0, 100, len(ingredients))
    happy = [calculateHappy(ingredients, combo) for combo in combos]

    happy2 = [calculateHappyPt2(ingredients, combo) for combo in combos] 

    print(max(happy))
    print(max(happy2))

class Ingredient:

    def __init__ (self, line):
        m = re.findall(r"(.*): capacity (-\d|\d), durability (-\d|\d), flavor (-\d|\d), texture (-\d|\d), calories (-\d|\d)", line)[0]

        self.name = m[0]
        self.capacity = int(m[1])
        self.durability = int(m[2])
        self.flavor = int(m[3])
        self.texture = int(m[4])
        self.calories = int(m[5])


main()