import re

def apply(string):
    result = ''
    current = string[0]
    count = 0
    for s in string:
        if s == current:
            count = count + 1
        else:
            result = result + str(count) + current
            current = s
            count = 1
    result = result + str(count) + current
    return result

def apply_regex(string):
    reg = r"(0{1,}|1{1,}|2{1,}|3{1,}|4{1,}|5{1,}|6{1,}|7{1,}|8{1,}|9{1,})"
    result = ''
    for match in re.findall(reg, string):
        result = result + str(len(match)) + match[0]
    return result

result = '1113122113'
for i in range(1,51):
    result = apply_regex(result)
    if i >= 40:
        print(str(i) + ". " + str(len(result)))

# Part 2
print(len(result))