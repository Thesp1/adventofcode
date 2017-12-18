from datetime import datetime

spinlock = [0]
# steps = 377
steps = 3
pos = 0

# Star 1
for x in xrange(2017):
    pos = ((pos + steps) % len(spinlock)) + 1
    insertion_point = pos
    spinlock = spinlock[:insertion_point] + [x+1] + spinlock[insertion_point:]

print spinlock
print "Answer 1:"
print spinlock[spinlock.index(2017) + 1]



# Star 2
spinlock = [0]
steps = 377
pos = 0
last_in_one_spot = 0
for x in xrange(1, 50000000):
    # if (x > 0) and (last_in_one_spot != spinlock[1]):
    #     last_in_one_spot = spinlock[1]
    #     print "On cycle {0}, {1} is in the 1 spot.".format(x, spinlock[1])
    pos = (pos + steps) % x
    # print pos
    if pos == 0:
        print "found one! {0}".format(x)
        last_in_one_spot = x
    pos += 1

print "Answer 2:"
print last_in_one_spot
