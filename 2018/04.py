from collections import Counter, defaultdict
from datetime import datetime
from pprint import pprint as P
import re

with open('input_data/04.txt') as f:
    DATA = sorted([x.strip() for x in f.readlines()])

PATTERN = re.compile(r'\[(?P<dt>.*)\] (?P<instr>falls asleep|wakes up|Guard #(?P<guard>\d+) begins shift)')


# Part 1

# Initialize
guard_number = 0
guard_data = defaultdict(Counter)
awake = True
asleep_at = 0

# Process logs
for log in DATA:
    match = PATTERN.search(log)
    if not match:
        raise Exception("Parser didn't parse correctly this instruction: {0}".format(log))
    instruction = match.group('instr')
    if instruction == 'falls asleep':
        awake = False
        dt = datetime.strptime(match.group('dt'), '%Y-%m-%d %H:%M')
        asleep_at = dt.minute
    elif instruction == 'wakes up':
        awake = True
        dt = datetime.strptime(match.group('dt'), '%Y-%m-%d %H:%M')
        awake_at = dt.minute
        for x in range(asleep_at, awake_at):
            guard_data[guard_number][x] += 1
    else:
        if not awake:
            raise Exception('Guard not awake when next shift starts!\n{}'.format(log))
        guard_number = int(match.group('guard'))

print "Complete processing logs!"

total_minutes_asleep = [(x, sum(y.values())) for x, y in guard_data.iteritems()]
sleepiest_guard_num = sorted(total_minutes_asleep, key= lambda x: x[1], reverse=True)[0][0]
sleepiest_guard_data = guard_data[sleepiest_guard_num]
sleepy_minute = sorted(list(sleepiest_guard_data.iteritems()), key=lambda x: x[1], reverse=True)[0][0]

print "Part 1:"
print "Sleepiest Guard is #{}".format(sleepiest_guard_num)
print "Sleepiest minute is: {}".format(sleepy_minute)
print "Answer is: {}".format(sleepiest_guard_num * sleepy_minute)

# Part 2
sleepiest_minute_list = [(x, sorted(list(y.iteritems()), key=lambda x: x[1], reverse=True)[0]) for x, y in guard_data.iteritems()]
sm = sorted(sleepiest_minute_list, key=lambda x: x[1][1], reverse=True)[0]

print "Part 2:"
print "Sleepiest Guard is #{}".format(sm[0])
print "Sleepiest minute is: {}".format(sm[1][0])
print "Answer is: {}".format(sm[0] * sm[1][0])
