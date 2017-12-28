from collections import defaultdict
from pprint import pprint as P

with open('input_data/22.txt') as f:
    DATA = f.read().strip()

# Constants.
UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)
CLEANED = '.'
INFECTED = '#'
WEAKENED = 'W'
FLAGGED = 'F'

# Helper functions.
def turn_right(direction):
    result_dictionary = {UP: RIGHT,
                         RIGHT: DOWN,
                         DOWN: LEFT,
                         LEFT: UP}
    return result_dictionary[direction]

def turn_left(direction):
    result_dictionary = {UP: LEFT,
                         RIGHT: UP,
                         DOWN: RIGHT,
                         LEFT: DOWN}
    return result_dictionary[direction]

def turn_around(direction):
    result_dictionary = {UP: DOWN,
                         RIGHT: LEFT,
                         DOWN: UP,
                         LEFT: RIGHT}
    return result_dictionary[direction]

def mesh(pos, direction):
    "Given position (x, y) and direction (a, b), return (x+a, y+b)"
    return tuple(sum(x) for x in zip(direction, pos))

def make_grid():
    grid = defaultdict(lambda: '.')
    imported_map_lists = DATA.split('\n')
    y_length = len(imported_map_lists)
    y_offset = (y_length / 2)
    for y in range(y_length):
        x_length = len(imported_map_lists[y])
        x_offset = (x_length / 2)
        for x in range(x_length):
            if imported_map_lists[y][x] == INFECTED:
                coords = (x - x_offset, -y + y_offset)
                grid[coords] = INFECTED
    return grid


# Star 1
grid = make_grid()
pos = (0, 0)
direction = UP
total_infections = 0

# Go!
for iteration in xrange(10000):
    if grid[pos] == INFECTED:
        direction = turn_right(direction)
        grid[pos] = CLEANED
    else:
        direction = turn_left(direction)
        total_infections += 1
        grid[pos] = INFECTED
    pos = mesh(pos, direction)

print "Step 1 total infections:\n{0}".format(total_infections)

# Star 2
grid = make_grid()
pos = (0, 0)
direction = UP
total_step2_infections = 0

# Go!
for iteration in xrange(10000000):
    if grid[pos] == CLEANED:
        direction = turn_left(direction)
        grid[pos] = WEAKENED
    elif grid[pos] == WEAKENED:
        grid[pos] = INFECTED
        total_step2_infections += 1
    elif grid[pos] == INFECTED:
        direction = turn_right(direction)
        grid[pos] = FLAGGED
    elif grid[pos] == FLAGGED:
        direction = turn_around(direction)
        grid[pos] = CLEANED
    pos = mesh(pos, direction)

print "Step 2 total infections:\n{0}".format(total_step2_infections)

