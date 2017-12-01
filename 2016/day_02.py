moves = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
    }

"""
locs = [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]

allowable_locs = set([(0, 0), (0, 1), (0, 2),
                      (1, 0), (1, 1), (1, 2),
                      (2, 0), (2, 1), (2, 2)])
"""

locs = [[None, None, '5', None, None],
        [None, '2', '6', 'A', None],
        ['1', '3', '7', 'B', 'D'],
        [None, '4', '8', 'C', None],
        [None, None, '9', None, None]]

allowable_locs = set([(0, 2),
                      (1, 1), (1, 2), (1, 3),
                      (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                      (3, 1), (3, 2), (3, 3),
                      (4, 2)])

with open('input_02.txt') as f:
    data = f.read().strip()

instructions_list = data.split()
code = ''

for instructions in instructions_list:
    pos = (0,2)
    for instruction in instructions:
        move = moves[instruction]
        possible_pos = (pos[0] + move[0],
                        pos[1] + move[1])
        if possible_pos not in allowable_locs:
            continue
        pos = possible_pos
    code += locs[pos[0]][pos[1]]
print code
