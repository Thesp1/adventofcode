GENERATOR_A_START = 591
GENERATOR_A_FACTOR = 16807
GENERATOR_B_START = 393
GENERATOR_B_FACTOR = 48271

# Star 1
def judge(input_a, input_b):
    hex_a = bin(input_a)[2:].zfill(16)
    hex_a_16 = hex_a[-16:]
    hex_b = bin(input_b)[2:].zfill(16)
    hex_b_16 = hex_b[-16:]
    return bool(hex_a_16 == hex_b_16)

def generate(val, factor):
    return (val * factor) % 2147483647


gen_a_value = GENERATOR_A_START
gen_b_value = GENERATOR_B_START
matches = 0

for i in xrange(40000000):
    if i % 1000000 == 0:
        print "Doing loop {0}, {1} matches so far...".format(i, matches)
    gen_a_value = generate(gen_a_value, GENERATOR_A_FACTOR)
    gen_b_value = generate(gen_b_value, GENERATOR_B_FACTOR)
    if judge(gen_a_value, gen_b_value):
        matches += 1

print "Answer 1:"
print matches


# Star 2
def generator_a():
    val = GENERATOR_A_START
    while True:
        val = generate(val, GENERATOR_A_FACTOR)
        if val % 4 == 0:
            yield val

def generator_b():
    val = GENERATOR_B_START
    while True:
        val = generate(val, GENERATOR_B_FACTOR)
        if val % 8 == 0:
            yield val

matches = 0
gen_a = generator_a()
gen_b = generator_b()
for i in range(5000000):
    if i % 100000 == 0:
        print "Doing loop {0}, {1} matches so far, gen_a_value={2} and gen_b_value={3}...".format(i, matches, gen_a_value, gen_b_value)
    gen_a_value = next(gen_a)
    gen_b_value = next(gen_b)
    if judge(gen_a_value, gen_b_value):
        matches += 1

print "Answer 2:"
print matches

