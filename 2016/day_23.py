from collections import defaultdict

with open('input_23.txt') as f:
    data = f.read().strip()

instructions = [x.split() for x in data.split('\n')]



# Star 1
registers = dict(a=7, b=0, c=0, d=0)
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
        try:
            registers[y] = val
        except KeyError:
            pass
    elif command == 'tgl':
        try:
            x = instruction[1]
            val = int(registers.get(x, x))
            command_to_modify = instructions[marker+val]
        except IndexError:
            marker += 1
            continue
        if command_to_modify[:3] == 'cpy': # 2
            command_to_modify = 'jnz' + command_to_modify[3:]
        elif command_to_modify == 'inc': # 1
            command_to_modify = 'dec' + command_to_modify[3:]
        elif command_to_modify == 'dec': # 1
            command_to_modify = 'inc' + command_to_modify[3:]
        elif command_to_modify == 'jnz': # 2
            command_to_modify = 'cpy' + command_to_modify[3:]
        elif command_to_modify == 'tgl': # 2
            command_to_modify = 'jnz' + command_to_modify[3:]
        instructions[marker+val] = command_to_modify
    else:
        raise Exception('Unhandled instruction: {0}'.format(instruction))
    marker += 1

print registers
