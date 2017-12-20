with open('input_data/20.txt') as f:
    DATA = f.read().strip()


import re
PATTERN = re.compile(r'p=<(?P<pos>[^>]+)>, v=<(?P<vel>[^>]+)>, a=<(?P<accel>[^>]+)>')

class Particle:
    def __init__(self, line_input):
        match = PATTERN.search(line_input)
        if not match:
            raise Exception("Parser didn't parse correctly this instruction: {0}".format(line))
        pos_input = match.group('pos')
        self.position = tuple([int(x) for x in pos_input.split(',')])
        vel_input = match.group('vel')
        self.velocity = tuple([int(x) for x in vel_input.split(',')])
        accel_input = match.group('accel')
        self.acceleration = tuple([int(x) for x in accel_input.split(',')])
        self.destroyed = False

    @property
    def manhattan_distance(self):
        if not self.destroyed:
            return sum([abs(x) for x in self.position])
        else:
            return 9999999999999

    def move(self):
        self.velocity = tuple(sum(x) for x in zip(self.velocity, self.acceleration))
        self.position = tuple(sum(x) for x in zip(self.position, self.velocity))


# Star 1
particles = [Particle(line) for line in DATA.split('\n')]

# 1000 times should be enough, right?
for x in range(1000):
    for particle in particles:
        particle.move()

mds = [x.manhattan_distance for x in particles]
smallest_distance = min(mds)
particle_index = mds.index(smallest_distance)
print "Closest to 0,0,0:\n{0}".format(particle_index)

# Star 2
particles = [Particle(line) for line in DATA.split('\n')]
for x in range(1000):
    if x % 100 == 0:
        print "Beginning loop {0}...".format(x)
    for particle in particles:
        if not particle.destroyed:
            particle.move()
    positions = list([x.position for x in particles if not x.destroyed])
    for position in positions:
        if positions.count(position) > 1:
            for particle in particles:
                if particle.position == position:
                    particle.destroyed = True

print "Star 2"
print "Surving Particles:\n{0}".format(len([x for x in particles if not x.destroyed]))
