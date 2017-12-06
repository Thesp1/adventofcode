with open('input_data/05.txt') as f:
    DATA = f.read().strip()

# Star 1
instructions = [int(x) for x in DATA.split('\n')]
steps = 0
index = 0
while index < len(instructions):
    instruction = instructions[index]
    instructions[index] += 1
    index += instruction
    steps += 1
print "Answer 1:"
print steps

# Star 2
instructions = [int(x) for x in DATA.split('\n')]
steps = 0
index = 0
while index < len(instructions):
    instruction = instructions[index]
    if instruction >= 3:
        instructions[index] -= 1
    else:
        instructions[index] += 1
    index += instruction
    steps += 1
print "Answer 2:"
print steps
