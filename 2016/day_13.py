DATA = 1364


class MyDict(dict):
    def __init__(self, factory):
        self.factory = factory

    def __missing__(self, key):
        self[key] = self.factory(*key)
        return self[key]

def is_wall(x, y):
    if x < 0 or y < y:
        return True
    val = x*x + 3*x + 2*x*y + y + y*y + 1364
    # If odd number of 1's, return True for "is wall".
    if len([x for x in bin(val) if x == '1']) % 2 == 1:
        return True
    return False

def next_door(x, y):
    return [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]

destination = (31, 39)
wall_map = MyDict(is_wall)

# Part 1
visited_locations = set([(1, 1),])
possible_positions = [(1,1),]
steps = 0
found = False
while not found:
    new_possible_positions = []
    steps += 1
    print "On step {0} now. Total possible positions: {1}".format(steps, len(possible_positions))
    for pos in possible_positions:
        adjacent_positions = next_door(*pos)
        for adj_pos in adjacent_positions:
            if adj_pos == destination:
                print '>>>>> Part 1: Got here in {0} steps!'.format(steps)
                found = True
            if not wall_map[adj_pos] and adj_pos not in visited_locations:
                visited_locations.add(adj_pos)
                new_possible_positions.append(adj_pos)
    possible_positions = new_possible_positions

# Part 2
visited_locations = set([(1, 1),])
possible_positions = [(1,1),]
steps = 0

while steps < 50:
    new_possible_positions = []
    steps += 1
    print "On step {0} now. Total possible positions: {1}".format(steps, len(possible_positions))
    for pos in possible_positions:
        adjacent_positions = next_door(*pos)
        for adj_pos in adjacent_positions:
            if adj_pos == destination:
                raise Exception('Got here in {0} steps!'.format(steps))
            if not wall_map[adj_pos]:
                visited_locations.add(adj_pos)
                new_possible_positions.append(adj_pos)
    possible_positions = list(set(new_possible_positions))

print ">>>>> Part 2 - Final possibilities: {0}".format(len(visited_locations))

