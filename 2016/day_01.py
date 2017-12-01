NORTH, SOUTH, EAST, WEST, LEFT, RIGHT = 'N', 'S', 'E', 'W', 'L', 'R'

with open('input_01.txt') as f:
    data = f.read().strip()

def new_direction(current_direction, turn_direction):
    if current_direction == NORTH:
        return WEST if turn_direction == LEFT else EAST
    if current_direction == SOUTH:
        return EAST if turn_direction == LEFT else WEST
    if current_direction == WEST:
        return SOUTH if turn_direction == LEFT else NORTH
    if current_direction == EAST:
        return NORTH if turn_direction == LEFT else SOUTH

orders = data.split(', ')
direction = NORTH
x_displacement = 0
y_displacement = 0
visited = set(tuple([0,0]),)
found = False
for order in orders:
    turn = order[0]
    dist = int(order[1:])
    print "Turning {0}, moving {1}...".format(order[0], order[1:])
    direction = new_direction(direction, order[0])
    print "   Now facing {0}.".format(direction)
    if direction == NORTH:
        for _ in range(dist):
            y_displacement += 1
            loc = (x_displacement, y_displacement)
            if loc in visited:
                found = True
                break
            visited.add(loc)
    elif direction == SOUTH:
        for _ in range(dist):
            y_displacement -= 1
            loc = (x_displacement, y_displacement)
            if loc in visited:
                found = True
                break
            visited.add(loc)
    elif direction == EAST:
        for _ in range(dist):
            x_displacement += 1
            loc = (x_displacement, y_displacement)
            if loc in visited:
                found = True
                break
            visited.add(loc)
    elif direction == WEST:
        for _ in range(dist):
            x_displacement -= 1
            loc = (x_displacement, y_displacement)
            if loc in visited:
                found = True
                break
            visited.add(loc)
    print "   Displacements are: {0} / {1}".format(x_displacement, y_displacement)
    if found:
        break
print "Final result:"
print "x_displacement: {0}".format(x_displacement)
print "y_displacement: {0}".format(y_displacement)
print "Final tally: {0}".format(abs(x_displacement) + abs(y_displacement))
