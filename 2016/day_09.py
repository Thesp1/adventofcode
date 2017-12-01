import re

with open('input_09.txt') as f:
    data = f.read().strip()

PATTERN = re.compile(r'\((?P<num_chars>\d+)x(?P<multiplier>\d+)\)')

# Test cases
# data = "(3x3)XYZ"
# data = "X(8x2)(3x3)ABCY"


# (start_pos, end_pos, num_chars, multiplier)
marker_list = []

class Marker:
    def __init__(self, start_pos, end_pos, num_chars, multiplier):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.num_chars = num_chars
        self.multiplier = multiplier

    @property
    def start_affected(self):
        return self.end_pos

    @property
    def end_affected(self):
        return self.end_pos + self.num_chars

    def within_parameters(self, outer_start, outer_end):
        if outer_start <= self.start_pos and self.end_pos <= outer_end:
            return True
        else:
            return False

    def __repr__(self):
        return u"<Marker {0}x{1} located:{2}-{3} affects: {4}-{5}".format(
                self.num_chars, self.multiplier, self.start_pos,
                self.end_pos, self.start_affected, self.end_affected)


def marker_finder(s, start):
    match = PATTERN.search(s, pos=start)
    if not match:
        return None
    num_chars = int(match.group('num_chars'))
    multiplier = int(match.group('multiplier'))
    start_pos = match.start()
    end_pos = match.end()
    return (start_pos, end_pos, num_chars, multiplier)

marker_index = 0
while True:
    res = marker_finder(data, marker_index)
    if not res:
        break
    marker_index = res[1]
    marker_list.append(Marker(*res))

# Set multipliers on data.
# Character itself and multiplier.
data_lists = [[x, 1] for x in data]
for index in range(marker_list_length):
    marker = marker_list[index]
    for inner_index in range(marker.start_affected, marker.end_affected):
        try:
            data_lists[inner_index][1] *= marker.multiplier
        except IndexError:
            print "Failed here:"
            print marker
            print inner_index

# Now, eliminate values for markers
for index in range(marker_list_length):
    marker = marker_list[index]
    for inner_index in range(marker.start_pos, marker.end_pos):
        try:
            data_lists[inner_index][1] = 0
        except IndexError:
            print "Failed here:"
            print marker
            print inner_index

print "Final tally:"
print sum([x[1] for x in data_lists])
print marker_list
print data_lists




"""
# Part 1
def marker_grabber(s):
    match = PATTERN.search(s)
    if not match:
        return s, ''
    num_chars = int(match.group('num_chars'))
    multiplier = int(match.group('multiplier'))
    start_pos = match.start()
    end_pos = match.end()
    chars_to_repeat = s[end_pos:end_pos+num_chars]
    beginning_string = s[:start_pos]
    remainder_string = s[end_pos+num_chars:]
    return beginning_string + (chars_to_repeat * multiplier), remainder_string

final_string = ''
while True:
    while data:
        uncompressed, remainder = marker_grabber(data)
        final_string += uncompressed
        data = remainder
    print "run once!"
    if PATTERN.search(final_string):
        data = final_string
        final_string = ''
    else:
        break


final_count = len(''.join(final_string.split()))

print final_count
"""
