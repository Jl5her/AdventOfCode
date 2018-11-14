import json

def read(data):
    if type(data) in [dict, list]:
        if type(data) == dict and "red" in data.values():       # Stop when in dictionary with value of 'red'
            return 0
        arr = data if type(data) == list else data.values()
        numbers = [read(e) for e in arr]
        return sum(numbers)
    elif type(data) == int:
        return data
    else:
        return 0

with open('../input.txt') as f:
    json_data = json.loads(f.readline())
    print(read(json_data))