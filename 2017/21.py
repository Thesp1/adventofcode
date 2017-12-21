from pprint import pprint as P
import datetime

with open('input_data/21.txt') as f:
    DATA = f.read().strip()

art = """.#.
..#
###"""

def flip_pattern(pattern):
    "Only works for 2x2 and 3x3."
    # print "Old pattern"
    # print pattern
    rows = pattern.split('\n')
    new_rows = []
    for row in rows:
        listrow = list(row)
        listrow[0], listrow[-1] = listrow[-1], listrow[0]
        new_rows.append(''.join(listrow))
    new_pattern = '\n'.join(new_rows)
    # print "Flipped pattern"
    # print new_pattern
    return new_pattern

def rotate_pattern(pattern):
    rows = [list(x) for x in pattern.split('\n')]
    # print "printing rows..."
    # print rows
    # Is it 2x2?
    if len(rows[0]) == 2:
        rows[0][0], rows[0][1], rows[1][0], rows[1][1] = rows[1][0], rows[0][0], rows[1][1], rows[0][1]
        return '\n'.join([''.join(x) for x in rows])
    else:
        # It's 3x3.
        rows[0][0], rows[0][1], rows[0][2], rows[1][0], rows[1][1], rows[1][2], rows[2][0], rows[2][1], rows[2][2] = rows[2][0], rows[1][0], rows[0][0], rows[2][1], rows[1][1], rows[0][1], rows[2][2], rows[1][2], rows[0][2]
    return '\n'.join([''.join(x) for x in rows])

# Star 1
rules = [x.split(' => ') for x in DATA.split('\n')]
transformations = {}

# Create the transformation dictionary of all possibilities.
for rule in rules:
    # print "rule"
    # print rule
    # transformations = {} #testing
    input_pattern = rule[0].replace('/', '\n')
    output_pattern = rule[1].replace('/', '\n')
    for x in range(4):
        # Each cycle adds twice to the dictionary, for 8 total additions.
        potential_input_pattern = input_pattern
        for y in range(x):
            potential_input_pattern = rotate_pattern(potential_input_pattern)
        # print "adding\n{0}".format(potential_input_pattern)
        transformations[potential_input_pattern] = output_pattern
        potential_input_pattern = flip_pattern(potential_input_pattern)
        # print "adding\n{0}".format(potential_input_pattern)
        transformations[potential_input_pattern] = output_pattern
    # print "Transformations: ============================="
    # P(transformations)

# raise Exception

# print "Transformations:"
# P(transformations)

for iteration in range(18):
    art_rows = art.split('\n')
    if len(art_rows) % 2 == 0:
        divisor = 2
    else:
        divisor = 3
    length = len(art_rows) / divisor
    art_batches = []

    # Break it all apart
    for y in range(length):
        art_batch = []
        for x in range(length):
            # print "x: {0} | y: {1}".format(x, y)
            art_batch.append('\n'.join([art_rows[i+y*divisor][x*divisor:(x*divisor)+divisor] for i in range(divisor)]))
        art_batches.append(art_batch)

    # Transform each batch
    for y in range(length):
        for x in range(length):
            # print art_batch[x][y]
            art_batches[x][y] = transformations[art_batches[x][y]]

    # Put it all back together.
    new_art_lines = []
    for y in range(length):
        for x in range(length):
            art_batches[x][y] = art_batches[x][y].split('\n')
    # print '======================'
    # print "art_batches"
    # print art_batches
    new_length = len(art_batches[0][0])
    for y in range(length):
        for i in range(new_length):
            new_line = ''.join([art_batches[y][x][i] for x in range(length)])
            new_art_lines.append(new_line)
    art = '\n'.join(new_art_lines)
    print "============================"
    print "Iteration {0}:".format(iteration)
    print "============================"
    print art


print "Answer 1:"
print art.count('#')

# Star 2
