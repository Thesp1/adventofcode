import re
from collections import Counter

with open('input_data/03.txt') as f:
    DATA = [x.strip() for x in f.readlines()]

PATTERN = re.compile(r'#(?P<instructionnumber>\d+) @ (?P<startx>\d+),(?P<starty>\d+): (?P<lengthx>\d+)x(?P<lengthy>\d+)')


class Patch:
    def __init__(self, line_input):
        self.line_input = line_input
        match = PATTERN.search(line_input)
        if not match:
            raise Exception("Parser didn't parse this instruction correctly: {}".format(line_input))
        self.instruction_number = int(match.group('instructionnumber'))
        self.start_x = int(match.group('startx'))
        self.start_y = int(match.group('starty'))
        self.length_x = int(match.group('lengthx'))
        self.length_y = int(match.group('lengthy'))
        self.end_x = self.start_x + self.length_x
        self.end_y = self.start_y + self.length_y

    def is_covered(self, x, y):
        if x >= self.start_x and x < self.end_x and y >= self.start_y and y < self.end_y:
            return True
        return False

    def covered_spots(self):
        seen_spots = set()
        for x in range(self.length_x):
            for y in range(self.length_y):
                seen_spots.add(tuple([self.start_x + x, self.start_y + y]))
        return seen_spots

    def __repr__(self):
        return u'{}'.format(self.line_input)

# # Testing
# p = Patch('#1 @ 1,3: 4x4')
# print p
# print p.covered_spots()

patches = [Patch(x) for x in DATA]

# Part 1
spot_counter = Counter()

for patch in patches:
    for spot in patch.covered_spots():
        spot_counter[spot] += 1

p1_answer = len([x for x in spot_counter.values() if x > 1])
print "Complete!"
print p1_answer


# Part 2
for p1_index in range(len(patches)):
    found_overlap = False
    for p2_index in range(len(patches)):
        if p1_index == p2_index:
            continue
        patch_1 = patches[p1_index]
        patch_2 = patches[p2_index]
        # print "Checking {} against {}...".format(patch_1, patch_2)
        for spot in patch_1.covered_spots():
            if patch_2.is_covered(*spot):
                found_overlap = True
                print "Overlap: {} - {} at {}".format(patch_1, patch_2, spot)
                break
        if found_overlap:
            break
    if not found_overlap:
        print "Found it!"
        print patches[p1_index]
        break
