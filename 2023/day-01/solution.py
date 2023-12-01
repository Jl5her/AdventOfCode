import re

f = open("input.txt")

t = 0

spell = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9"
}


def find_occurrences(search):
    o = []
    for word in spell.keys():
        if word not in search:
            continue

        rindex = search.rindex(word)
        index = search.index(word)
        o.append((word, rindex))
        o.append((word, index))

    return sorted(o, key=lambda t: t[1])


for line in f.readlines():

    occurrences = find_occurrences(line)
    if len(occurrences) != 0:
        (first_word, _) = occurrences[0]
        (last_word, _) = occurrences[-1]

        new_first_word = spell[first_word]
        new_last_word = spell[last_word]

        line = line.replace(first_word, f"{new_first_word}{first_word[-1]}", 1)
        line = line.replace(last_word, new_last_word)

    m = re.findall(r"(\d)", line)

    t += int(m[0] * 2) if len(m) == 1 else int(m[0] + m[-1])

f.close()
print(t)
