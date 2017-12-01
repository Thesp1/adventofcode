import re

with open('input_12.txt') as f:
    data = f.read().strip()

instructions = [x.split() for x in data.split('\n')]
# Part 1
# registers = dict(a=0, b=0, c=1, d=0)
# Part 2
# registers = dict(a=0, b=0, c=0, d=0)


marker = 0
while marker < len(instructions):
    # print "At marker {0}...".format(marker)
    instruction = instructions[marker]
    # print instruction
    command = instruction[0]
    if command == 'jnz':
        # print registers
        x, y = instruction[1], instruction[2]
        check_val = int(registers.get(x, x))
        if check_val != 0:
            marker += int(y)
        else:
            marker += 1
        continue
    elif command == 'inc':
        x = instruction[1]
        registers[x] += 1
    elif command == 'dec':
        x = instruction[1]
        registers[x] -= 1
    elif command == 'cpy':
        x, y = instruction[1], instruction[2]
        val = int(registers.get(x, x))
        registers[y] = val
    marker += 1

print registers
