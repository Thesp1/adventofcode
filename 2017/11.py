with open('input_data/11.txt') as f:
    DATA = f.read().strip()

directions = DATA.split(',')

def total_distance_away(h, v):
    if abs(h) > abs(v):
        return abs(h) * 2
    else:
        return abs(v) + abs(h)

# Stars 1 & 2
horizontal_distance = 0
vertical_distance = 0
path = []
for direction in directions:
    if direction == 'n':
        vertical_distance += 1
    elif direction == 's':
        vertical_distance -= 1
    elif direction == 'nw':
        vertical_distance += 0.5
        horizontal_distance -= 0.5
    elif direction == 'ne':
        vertical_distance += 0.5
        horizontal_distance += 0.5
    elif direction == 'sw':
        vertical_distance -= 0.5
        horizontal_distance -= 0.5
    elif direction == 'se':
        vertical_distance -= 0.5
        horizontal_distance += 0.5
    else:
        raise Exception("I can't parse {}.".format(direction))
    path.append(total_distance_away(horizontal_distance, vertical_distance))
answer = total_distance_away(horizontal_distance, vertical_distance)

print "Answer 1:"
print answer
print "Answer 2:"
print max(path)
