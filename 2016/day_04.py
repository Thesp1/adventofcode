from collections import Counter

with open('input_04.txt') as f:
    data = f.read().strip()

rooms = data.split('\n')
sector_id_sum = 0
for room in rooms:
    first_part, checksum = room[:-7], room[-6:-1]
    last_dash_index = first_part.rfind('-')
    letters_orig = first_part[:last_dash_index]
    letters = letters_orig.replace('-', '')
    sector_id = int(first_part[last_dash_index+1:])
    lc = Counter(letters)
    lc_list = sorted(lc.items(), key=lambda x: (-x[1], x[0]))
    lc_checksum = ''.join([x[0] for x in lc_list][:5])
    if checksum == lc_checksum:
        # Part 1
        # sector_id_sum += sector_id
        # Part 2
        jump_forward = sector_id % 26
        message = ''
        for character in letters_orig:
            if character == '-':
                message += ' '
            else:
                new_char_ord = ord(character) + jump_forward
                if new_char_ord > 122:
                    new_char_ord -= 26
                message += chr(new_char_ord)
        print "{0} | Sector {1}".format(message, sector_id)
        if 'northpole' in message:
            print "========================================"
            break



# Part 1
# print sector_id_sum
