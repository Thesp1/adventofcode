with open('input_data/02.txt') as f:
    data = f.read().strip()

# Star 1
lines = data.split('\n')
checksum = 0
for line in lines:
    vals = [int(x) for x in line.split()]
    checksum += max(vals) - min(vals)
print "Answer 1:"
print checksum

# Star 2
from itertools import combinations
checksum = 0
for line in lines:
    vals = sorted([int(x) for x in line.split()])
    for x, y in combinations(vals, 2):
        if y % x == 0:
            # print "Found one! {0} and {1}.".format(y, x)
            checksum += y / x
            break
print "Answer 2:"
print checksum
