from re import compile
from itertools import permutations


with open('input_21.txt') as f:
    data = f.read().strip()
s = 'abcdefgh'

# with open('input_21b.txt') as f:
#     data = f.read().strip()
# s = 'abcde'

instructions = data.split('\n')

swap_position_pattern = compile(r'^swap position (?P<x>\d+) with position (?P<y>\d+)$')
swap_letter_pattern = compile(r'^swap letter (?P<a>[a-z]+) with letter (?P<b>[a-z]+)$')
rotate_pattern = compile(r'^rotate (?P<direction>left|right) (?P<z>\d+) steps?$')
rotate_based_pattern = compile(r'^rotate based on position of letter (?P<a>[a-z]+)$')
reverse_positions_pattern = compile(r'^reverse positions (?P<x>\d+) through (?P<y>\d+)$')
move_position_pattern = compile(r'^move position (?P<x>\d+) to position (?P<y>\d+)$')


def swap_position(s, x, y):
    s_list = list(s)
    s_list[x], s_list[y] = s_list[y], s_list[x]
    return ''.join(s_list)

def swap_letter(s, a, b):
    s_list = list(s)
    x, y = s_list.index(a), s_list.index(b)
    s_list[x], s_list[y] = s_list[y], s_list[x]
    return ''.join(s_list)

def rotate(s, direction, z):
    z = z % len(s)
    if direction == 'right':
        return s[-z:] + s[:-z]
    if direction == 'left':
        return s[z:] + s[:z]
    raise Exception('Failed to pass in left/right. Instead, passed: {0}'.format(direction))

def rotate_based(s, a):
    z = s.index(a)
    if z >= 4:
        z += 1
    z += 1
    return rotate(s, 'right', z)

def reverse_positions(s, x, y):
    x, y = sorted([x, y])
    if x != 0:
        return s[:x] + s[y:x-1:-1] + s[y+1:]
    return s[y::-1] + s[y+1:]

def move_position(s, x, y):
    s_list = list(s)
    popped_letter = s_list.pop(x)
    s_list.insert(y, popped_letter)
    return ''.join(s_list)


for perm in permutations('fbgdceah'):
    s = ''.join(perm)
    for instruction in instructions:
        swap_position_match = swap_position_pattern.search(instruction)
        swap_letter_match = swap_letter_pattern.search(instruction)
        rotate_match = rotate_pattern.search(instruction)
        rotate_based_match = rotate_based_pattern.search(instruction)
        reverse_positions_match = reverse_positions_pattern.search(instruction)
        move_position_match = move_position_pattern.search(instruction)
        if swap_position_match:
            m = swap_position_match
            s = swap_position(s, int(m.group('x')), int(m.group('y')))
        elif swap_letter_match:
            m = swap_letter_match
            s = swap_letter(s, m.group('a'), m.group('b'))
        elif rotate_match:
            m = rotate_match
            s = rotate(s, m.group('direction'), int(m.group('z')))
        elif rotate_based_match:
            m = rotate_based_match
            s = rotate_based(s, m.group('a'))
        elif reverse_positions_match:
            m = reverse_positions_match
            s = reverse_positions(s, int(m.group('x')), int(m.group('y')))
        elif move_position_match:
            m = move_position_match
            s = move_position(s, int(m.group('x')), int(m.group('y')))
        else:
            raise Exception('Unknown instruction: {0}'.format(instruction))
    if s == 'fbgdceah':
        print "Found it! Start with: {0}".format(''.join(perm))
        break

# print "Complete!"
# print s
