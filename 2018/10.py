from __future__ import print_function
import re

with open('input_data/10.txt') as f:
    DATA = [x.strip() for x in f.readlines()]

PATTERN = re.compile(r'position=< *(?P<startx>-?\d+), *(?P<starty>-?\d+)> velocity=< *(?P<velx>-?\d+), *(?P<vely>-?\d+)>')
MAX_RANGE = 62 # Trial and error to find

class Point:
    def __init__(self, input_line):
        match = PATTERN.search(input_line)
        if not match:
            raise Exception("Parser didn't parse correctly this instruction: {0}".format(input_line))
        self.x = int(match.group('startx'))
        self.y = int(match.group('starty'))
        self.velocity_x = int(match.group('velx'))
        self.velocity_y = int(match.group('vely'))

    def run_me(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def __repr__(self):
        return u'({}, {}) <{}, {}>'.format(self.x, self.y, self.velocity_x, self.velocity_y)

def print_points(tuples_list):
    x_max = max([z[0] for z in tuples_list])
    y_max = max([z[1] for z in tuples_list])
    tuples_set = set(tuples_list)
    for y in range(y_max+1):
        for x in range(x_max+1):
            if (x, y) in tuples_set:
                print('#', end='')
            else:
                print(' ', end='')
        print()


all_points = [Point(x) for x in DATA]
aligned = False

for step in range(1, 20000):
    for x in all_points:
        x.run_me()
    all_x = [z.x for z in all_points]
    all_y = [z.y for z in all_points]
    if (max(all_x) - min(all_x) < MAX_RANGE) and (max(all_y) - min(all_y) < MAX_RANGE):
        print("The stars are aligned!")
        print(step)
        # print(max(all_x) - min(all_x))
        # print(max(all_y) - min(all_y))
        aligned = True
        min_x = min(all_x)
        min_y = min(all_y)
        # Do more stuff
        print_points([(z.x - min_x, z.y - min_y) for z in all_points])
    elif aligned:
        print("They've gone too far apart now. Fly away...")
        break

