import hashlib

def md5(string):
    encoded = string.encode('ascii')
    m = hashlib.md5()
    m.update(encoded)   
    return m.hexdigest()

def part1(string):
    i = 0
    hashed = md5(string + str(i))
    while not(hashed[:5] == "00000"):
        i += 1
        hashed = md5(string + str(i))
    return i

def part2(string):
    i = 0
    hashed = md5(string + str(i))
    while not(hashed[:6] == "000000"):
        i += 1
        hashed = md5(string + str(i))
    return i

secret_key = "bgvyzdsv"

print(part1(secret_key))
print(part2(secret_key))