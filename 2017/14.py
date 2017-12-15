PUZZLE_INPUT = 'stpzcrnm'

# Star 1
def knot_hash(data):
    sparse_hash = range(256)
    current_position = 0
    skip_size = 0
    sequence_of_lengths = [ord(x) for x in data]
    sequence_of_lengths += [17, 31, 73, 47, 23]
    for loop in range(64):
        for leng in sequence_of_lengths:
            temp_list = sparse_hash[:] + sparse_hash[:]
            sub_list = temp_list[current_position:current_position+leng]
            sub_list.reverse()
            new_positions = [x % 256 for x in range(current_position, current_position+leng)]
            # Create tuples in list.
            write_list = zip(new_positions, sub_list)
            # Then, overwrite current list.
            for pos, val in write_list:
                sparse_hash[pos] = val
            # Move current_position.
            current_position = (current_position + leng + skip_size) % 256
            # Finally, increment skip_size.
            skip_size += 1
    dense_hash = []
    for i in range(16):
        new_hash = sparse_hash[i*16+0] ^ sparse_hash[i*16+1] ^ sparse_hash[i*16+2] ^ sparse_hash[i*16+3] ^ sparse_hash[i*16+4] ^ sparse_hash[i*16+5] ^ sparse_hash[i*16+6] ^ sparse_hash[i*16+7] ^ sparse_hash[i*16+8] ^ sparse_hash[i*16+9] ^ sparse_hash[i*16+10] ^ sparse_hash[i*16+11] ^ sparse_hash[i*16+12] ^ sparse_hash[i*16+13] ^ sparse_hash[i*16+14] ^ sparse_hash[i*16+15]
        dense_hash.append(new_hash)
    # print '---------------'
    # print dense_hash
    hex_rep = ''.join([hex(x)[2:].zfill(2) for x in dense_hash])
    # print hex_rep
    # print len(hex_rep)
    return hex_rep

def hex_to_binary(hex_val):
    "Takes a hex string and returns a string of 1's and 0's for the binary representation."
    num_of_bits = 4 * len(hex_val)
    return bin(int(hex_val, 16))[2:].zfill(num_of_bits)

# Star 1
rows = []
for i in range(128):
    row_seed = '{0}-{1}'.format(PUZZLE_INPUT, i)
    hex_rep = knot_hash(row_seed)
    # print hex_rep
    bin_string = hex_to_binary(hex_rep)
    # print len(bin_string)
    rows.append([True if x == '1' else False for x in bin_string])

print "Answer 1:"
print sum([x.count(True) for x in rows])

# Star 2
def print_regions():
    print '\n'
    for row in rows:
        print ''.join('#' if x else '.' for x in row)
    print '\n'

print_regions()

def nuke_group(x, y):
    rows[x][y] = False
    if x > 0 and rows[x-1][y]:
        nuke_group(x-1, y)
    if x < 127 and rows[x+1][y]:
        nuke_group(x+1, y)
    if y > 0 and rows[x][y-1]:
        nuke_group(x, y-1)
    if y < 127 and rows[x][y+1]:
        nuke_group(x, y+1)
    return None

group_count = 0
for x in range(128):
    for y in range(128):
        if rows[x][y]:
            group_count += 1
            nuke_group(x, y)

print "Answer 2:"
print group_count
# 1087 is too low
