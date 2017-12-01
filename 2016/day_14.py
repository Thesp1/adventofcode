from re import finditer
from hashlib import md5

SALT = 'ihaygndm'
# SALT = 'abc'
MATCH3 = '(?P<repeated>.)(?P=repeated){2}'
MATCH5 = '(?P<repeated>.)(?P=repeated){4}'



def threes_and_fives(i):
    # Part 1
    # h = md5(SALT + str(i)).hexdigest()
    # Part 2
    h = md5(SALT + str(i)).hexdigest()
    for x in range(2016):
        h = md5(h).hexdigest()
    match3_list = [x.group('repeated') for x in finditer(MATCH3, h)]
    match5_list = [x.group('repeated') for x in finditer(MATCH5, h)]
    match_3 = match3_list[0] if match3_list else ''
    match_5 = match5_list[0] if match5_list else ''
    return match_3, match_5
    # return ''.join(set(match3_list)), ''.join(set(match5_list))

numbered_pad = 0
marker = 0
start_list = [threes_and_fives(x) for x in range(1000)]
three_list = [x[0] for x in start_list]
five_list = [x[1] for x in start_list]


while numbered_pad < 64:
    if marker % 10000 == 0:
        print "Checking marker {0}...".format(marker)
    threes, fives = threes_and_fives(marker+1000)
    three_list.append(threes)
    five_list.append(fives)
    five_list.pop(0) # Axe this, no longer needed
    current_three_hash = three_list.pop(0)
    for letter in current_three_hash:
        if len([x for x in five_list if letter in x]) >= 1:
            numbered_pad += 1
            print "Found #{0} match at marker {1}!".format(numbered_pad, marker)
            print "Matched letter: {0}".format(letter)
            # print md5(SALT + str(marker)).hexdigest()
            # print '|'.join([x for x in three_list if x])
            print '|'.join([x for x in five_list if x])
            break
    marker += 1
