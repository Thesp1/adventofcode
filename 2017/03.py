DATA = 289326

counter = 1
while True:
    counter_squared = counter * counter
    if counter_squared >= DATA:
        print "It's less than or equal to the square for {0}, which is {1}...".format(counter, counter_squared)
        min_distance = (counter - 1) / 2
        corner_difference = counter - 1
        midpoints = [counter_squared - (i * corner_difference) - min_distance for i in range(4)]
        print "midpoints"
        print midpoints
        diffs = [abs(midpoint - DATA) for midpoint in midpoints]
        answer_1 = min(diffs) + min_distance
        break
    else:
        counter += 2

print "Answer 1:"
print answer_1

def next_direction(direction):
    if direction == 'RIGHT':
        return 'UP'
    if direction == 'UP':
        return 'LEFT'
    if direction == 'LEFT':
        return 'DOWN'
    if direction == 'DOWN':
        return 'RIGHT'

horizontal_limit = 1
vertical_limit = 1
horizontal_tracker = 0
vertical_tracker = 0
direction = 'RIGHT'
matrix = dict()
x, y = 0, 0
matrix[(x,y)] = 1
last_written = 1
while last_written < DATA:
    if direction == 'RIGHT':
        x += 1
        horizontal_tracker += 1
    elif direction == 'UP':
        y -= 1
        vertical_tracker += 1
    elif direction == 'LEFT':
        x -= 1
        horizontal_tracker += 1
    elif direction == 'DOWN':
        y += 1
        vertical_tracker += 1
    new_val = matrix.get((x-1,y-1), 0) + matrix.get((x-1,y), 0) + \
              matrix.get((x-1,y+1), 0) + matrix.get((x,y-1), 0) + \
              matrix.get((x,y+1), 0) + matrix.get((x+1,y-1), 0) + \
              matrix.get((x+1,y), 0) + matrix.get((x+1,y+1), 0)
    last_written = new_val
    matrix[(x, y)] = new_val
    print "At ({0}, {1}): {2}".format(x, y, last_written)
    if last_written > DATA:
        print "Answer 2:"
        print last_written
        break
    if horizontal_tracker == horizontal_limit:
        horizontal_tracker = 0
        horizontal_limit += 1
        direction = next_direction(direction)
    elif vertical_tracker == vertical_limit:
        vertical_tracker = 0
        vertical_limit += 1
        direction = next_direction(direction)
    print "Direction now: {0}".format(direction)
