with open('input_data/19.txt') as f:
    DATA = f.read()

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
ALL_DIRECTIONS = set([UP, DOWN, LEFT, RIGHT])

# Stars 1 & 2
imported_map = DATA[:-1].split('\n')
# I want to use xy_map[x][y] for coordinates - this magic does that.
xy_map = zip(*imported_map)
pos = (147, 0)
direction = DOWN
collected_letters = ''
total_steps = 0

def mesh(pos, direction):
    "Given position (x, y) and direction (a, b), return (x+a, y+b)"
    return tuple(sum(x) for x in zip(direction, pos))

def get_char(x_y):
    "Gracefully get the character at (x, y), returning a space if out of bounds."
    try:
        val = xy_map[x_y[0]][x_y[1]]
    except IndexError:
        val = ' '
    return val

def check_plus(pos, heading):
    "Given current position and heading, return new heading."
    # print "here"
    opposite_heading = tuple(-x for x in heading)
    directions_to_check = ALL_DIRECTIONS - set([heading, opposite_heading])
    for direction in directions_to_check:
        map_char = get_char(mesh(pos, direction))
        if direction in (UP, DOWN) and map_char == '|':
            return direction
        elif direction in (LEFT, RIGHT) and map_char == '-':
            return direction
    raise Exception('Nowhere to go from + at {0} with heading {1}.'.format(pos, heading))

while True:
    pos = mesh(pos, direction)
    current_char = get_char(pos)
    total_steps += 1
    if current_char == ' ':
        print "Finished!"
        break
    if current_char not in '|-+':
        print "Got {0}!".format(current_char)
        collected_letters += current_char
    elif current_char == '+':
        direction = check_plus(pos, direction)

# Star 1
print "Collected characters:\n{0}".format(collected_letters)

# Star 2
print "Total steps:\n{0}".format(total_steps)
