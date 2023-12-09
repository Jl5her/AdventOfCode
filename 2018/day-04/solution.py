import re
from datetime import datetime

with open('input.txt') as f:
    lines = [l.rstrip() for l in f.readlines()]


def by_timestamp(line):
    timestamp = re.findall(r"\[(.*)\]", line)[0]
    return datetime.strptime(timestamp, "%Y-%m-%d %H:%M")


lines.sort(key=by_timestamp)

exp = r"\[1518\-(\d+)\-(\d+) (\d+):(\d+)\] (.*)"
guard_exp = r"Guard #(\d+) (.*)"

timesheet = {}
guards = []

guard = None
last_time = None

for line in lines:
    [m, d, hr, min, statement] = re.findall(exp, line)[0]
    m, d, hr, min = int(m), int(d), int(hr), int(min)

    if re.match(guard_exp, statement):
        guard = int(re.findall(guard_exp, statement)[0][0])
        guards.append(guard)

    if "falls asleep" == statement:
        last_time = min

    if guard:
        date = f"{m}-{d}  #{guard}"
        if date not in timesheet:
            timesheet[date] = ["." for _ in range(60)]

        if "wakes up" == statement:
            for minute in range(last_time, min):
                timesheet[date][minute] = "#"


def time_asleep(guard):
    return sum([t.count("#") for d, t in timesheet.items() if f"#{guard}" in d])


def get_sleepiest_minute(guard):
    minutes = {}
    for d, t in timesheet.items():
        if f"#{guard}" in d:
            for i, minute in enumerate(t):
                if i not in minutes:
                    minutes[i] = 1
                else:
                    minutes[i] += 1 if minute == '#' else 0
    m = max(minutes, key=minutes.get)
    return m, minutes[m]


def part1():
    sleepy_guard = sorted([[g, time_asleep(g)] for g in guards], key=lambda x: x[1])[-1][0]

    (minute, _) = get_sleepiest_minute(sleepy_guard)
    return sleepy_guard * minute


def part2():
    frequent_sleeper = sorted([[g, get_sleepiest_minute(g)] for g in guards], key=lambda x: x[1][1])[-1]
    return frequent_sleeper[0] * frequent_sleeper[1][0]


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
