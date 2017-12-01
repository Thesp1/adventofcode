
class Disc:
    def __init__(self, num_positions, initial_pos):
        self.num_positions = num_positions
        self.initial_pos = initial_pos

    def pos_at_time(self, time):
        return (self.initial_pos + time) % self.num_positions

DISCS = [Disc(5, 2),
         Disc(13, 7),
         Disc(17, 10),
         Disc(3, 2),
         Disc(19, 9),
         Disc(7, 0),
         # Part 2
         Disc(11, 0),
         ]

time = 0

while True:
    dropped = True
    for disc_time, disc in enumerate(DISCS, start=time+1):
        if disc.pos_at_time(disc_time) != 0:
            dropped = False
            break
    if dropped:
        print "Made it through at time: {0}".format(time)
        break
    else:
        time += 1
