with open('input_data/01.txt') as f:
    instructions = [int(x.strip()) for x in f.readlines()]


# Day 1
frequency = 0

for instr in instructions:
    frequency += instr

print "Day 1:"
print frequency


# Day 2
frequency = 0
seen_frequencies = set([0])
while True:
    for instr in instructions:
        frequency += instr
        if frequency in seen_frequencies:
            print "Found it!"
            print frequency
            raise
        seen_frequencies.add(frequency)
