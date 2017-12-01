# raise Exception
from hashlib import md5

DATA = 'mmsxrhfx'
# DATA = 'ihgpwlah'


class Location:
    def __init__(self, x, y, path_string):
        self.x = x
        self.y = y
        self.path_string = path_string

    def possible_doors(self):
        keys = md5(DATA + self.path_string).hexdigest()[:4]
        doors = []
        if keys[0] in 'bcdef' and self.y > 0:
            doors.append('U')
        if keys[1] in 'bcdef' and self.y < 3:
            doors.append('D')
        if keys[2] in 'bcdef' and self.x > 0:
            doors.append('L')
        if keys[3] in 'bcdef' and self.x < 3:
            doors.append('R')
        return doors

    def copy_add_path(self, path_letter):
        x, y = self.x, self.y
        path_string = self.path_string + path_letter
        if path_letter == 'U':
            y -= 1
        elif path_letter == 'D':
            y += 1
        elif path_letter == 'L':
            x -= 1
        elif path_letter == 'R':
            x += 1
        return Location(x, y, path_string)

    def found_vault(self):
        if self.x == 3 and self.y == 3:
            return True
        return False

    def __str__(self):
        return u"<Location ({0}, {1}) - {2}>".format(self.x, self.y, self.path_string)


possible_positions = [Location(0, 0, '')]
steps = 0
max_steps = 0

# Part 1
found = False
while not found:
    new_possible_positions = []
    steps += 1
    print "On step {0} now. Total possible positions: {1}".format(steps, len(possible_positions))
    for pos in possible_positions:
        possible_directions = pos.possible_doors()
        for direction in possible_directions:
            new_possible_positions.append(pos.copy_add_path(direction))
    possible_positions = new_possible_positions
    not_found_positions = [x for x in possible_positions if not x.found_vault()]
    found_positions = [x for x in possible_positions if x.found_vault()]
    if found_positions:
        max_steps = steps
    if not not_found_positions:
        found = True
        print "Out of positions!"
        print "Final steps: {0}".format(max_steps)
        break
    possible_positions = not_found_positions

# # Part 2
# visited_locations = set([(1, 1),])
# possible_positions = [(1,1),]
# steps = 0

# while steps < 50:
#     new_possible_positions = []
#     steps += 1
#     print "On step {0} now. Total possible positions: {1}".format(steps, len(possible_positions))
#     for pos in possible_positions:
#         adjacent_positions = next_door(*pos)
#         for adj_pos in adjacent_positions:
#             if adj_pos == destination:
#                 raise Exception('Got here in {0} steps!'.format(steps))
#             if not wall_map[adj_pos]:
#                 visited_locations.add(adj_pos)
#                 new_possible_positions.append(adj_pos)
#     possible_positions = list(set(new_possible_positions))

# print ">>>>> Part 2 - Final possibilities: {0}".format(len(visited_locations))

