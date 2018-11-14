import re

with open("../input.txt") as f:
    string_numbers = re.findall(r"(-\d+|\d+)+", f.readline())
    numbers = [int(string_number) for string_number in string_numbers]
    print(sum(numbers))