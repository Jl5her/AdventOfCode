def bin2dec(x): return sum([(2**(len(x) - i - 1)) * int(x[i])
                            for i in range(len(x))])


lines = []
cols = []

with open("input.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]
    for line_num in range(len(lines)):
        line = lines[line_num]
        for col in range(len(line)):
            val = int(line[col])
            if line_num == 0:
                cols.append([val])
            else:
                cols[col].append(val)

print("\nPart 1: ")
gamma = []
epsilon = []

for col in cols:
    mode = 1 if col.count(1) > col.count(0) else 0
    imode = 1 if mode == 0 else 0
    gamma.append(mode)
    epsilon.append(imode)

gamma = bin2dec(gamma)
epsilon = bin2dec(epsilon)

print(f"Gamma = {gamma}")
print(f"Epsilon = {epsilon}")
print(f"Product = {gamma * epsilon}")

print("\nPart 2:")

o_numbers = lines[:]
c_numbers = lines[:]
col = 0
while len(o_numbers) > 1 or len(c_numbers) > 1:
    if len(o_numbers) > 1:
        o_bits = [num[col] for num in o_numbers]
        o_mode = "1" if o_bits.count("1") >= o_bits.count("0") else "0"
        o_numbers = list(filter(lambda x: x[col] == o_mode, o_numbers))
    if len(c_numbers) > 1:
        c_bits = [num[col] for num in c_numbers]
        c_mode = "1" if not(c_bits.count("1") >= c_bits.count("0")) else "0"
        c_numbers = list(filter(lambda x: x[col] == c_mode, c_numbers))
    col += 1


ocr = bin2dec(o_numbers[0])
csr = bin2dec(c_numbers[0])

print(f"Oxygen Generator Rating: {ocr}")
print(f"CO2 Scrubber Rating: {csr}")
print(f"Product: {ocr * csr}")
