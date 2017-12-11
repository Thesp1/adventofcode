DATA = '70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41'

lon = range(256)
current_position = 0
skip_size = 0
sequence_of_lengths = [int(x) for x in DATA.split(',')]

# Star 1
for leng in sequence_of_lengths:
    temp_list = lon[:] + lon[:]
    sub_list = temp_list[current_position:current_position+leng]
    sub_list.reverse()
    new_positions = [x % 256 for x in range(current_position, current_position+leng)]
    # Create tuples in list.
    write_list = zip(new_positions, sub_list)
    # Then, overwrite current list.
    for pos, val in write_list:
        lon[pos] = val
    # Move current_position.
    current_position = (current_position + leng + skip_size) % 256
    # Finally, increment skip_size.
    skip_size += 1

print "Answer 1:"
print lon[0] * lon[1]

# Star 2
sparse_hash = range(256)
current_position = 0
skip_size = 0
sequence_of_lengths = [ord(x) for x in DATA]
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
hex_rep = ''.join([hex(x)[2:] for x in dense_hash])

print "Answer 2:"
print hex_rep
