from re import compile
from pprint import pprint as P
from time import sleep

with open('input_22.txt') as f:
    data = f.read().strip()

pattern = compile(r'/dev/grid/node-x(?P<x>\d+)-y(?P<y>\d+)\s+(?P<size>\d+)T\s+(?P<used>\d+)T\s+(?P<avail>\d+)T\s+(?P<use>\d+)%')

def reset():
    instructions = data.split('\n')[2:]
    node_dict = {}
    for instruction in instructions:
        m = pattern.search(instruction).groupdict()
        n = Node(m['x'], m['y'], m['used'], m['avail'])
        node_dict[(n.x, n.y)] = n
    return node_dict

class Node:
    def __init__(self, x, y, used, avail):
        self.x = int(x)
        self.y = int(y)
        self.used = int(used)
        self.avail = int(avail)
        self.size = int(used) + int(avail)
        if self.x == 29 and self.y == 34:
            self.target_data = True
        else:
            self.target_data = False

    def is_node_viable(self, target_node):
        if self.x == target_node.x and self.y == target_node.y:
            return False
        if self.used == 0:
            return False
        if self.used <= target_node.avail:
            return True
        return False

    def is_node_movable(self, target_node):
        if not self.is_node_viable(target_node):
            return False
        if abs(self.x - target_node.x) == 1 and self.y == target_node.y:
            return True
        if self.y == target_node.y and abs(self.y - target_node.y):
            return True
        return False

    def move_data(self, target_node):
        data_size = self.used
        target_node.used += data_size
        target_node.avail -= data_size
        target_node.target_data = self.target_data
        self.avail += self.size
        self.used = 0
        self.target_data = False
        return True

    def __str__(self):
        return '<Node ({x}, {y}): {used}|{avail}|{size}>'.format(x=self.x, y=self.y, used=self.used, avail=self.avail, size=self.size)



node_dict = reset()

# Part 1
counter = 0
for node_a in node_dict.values():
    for node_b in node_dict.values():
        if node_a.is_node_viable(node_b):
            counter += 1

print "Done! Tally is: {0}".format(counter)


for y in range(35):
    print ''.join(['{0:>4}'.format(node_dict[(x, y)].used) for x in range(29)])



# Part 2
# counter = 0
# for node_a in node_dict.values():
#     for node_b in node_dict.values():
#         if node_a.is_node_movable(node_b):
#             print "Found one!"
#             print node_a
#             print node_b
#             counter += 1

# print "Done! Tally is: {0}".format(counter)

# 185 by hand (whew)
