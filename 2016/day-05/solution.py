
import hashlib

puzzle_input = "uqwqemis"

def md5(s):
    return hashlib.md5(bytes(s, encoding='utf-8')).hexdigest()

def part1(s):
    password = ""
    i = 0
    while len(password) != 8:
        m = md5(s + str(i))
        if m[:5] == "00000":
            password += m[5]
            print(password)
        i += 1
    return password

def part2(s):
    password = ["." for i in range(8)]
    i = 0
    while "." in password:
        m = md5(s + str(i))
        if m[:5] == "00000" and m[5].isdigit():
            index = int(m[5])
            if index < 8 and password[index] == ".":
                password[index] = m[6]
                print("".join(password))
        i+= 1
    return "".join(password)

print("Part 1")
part1(puzzle_input)

print("\nPart 2")
part2(puzzle_input)