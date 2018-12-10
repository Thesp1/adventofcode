with open('input_data/23.txt') as f:
    DATA = f.read().strip()

from collections import defaultdict
registers = {0: defaultdict(int),}
# registers[0]['a'] = 1

def find_val(x, program_id=0):
    regs = registers[program_id]
    try:
        val = int(x)
    except ValueError:
        val = regs[x]
    return val

def set_register(x, y, program_id=0):
    "set X Y"
    regs = registers[program_id]
    regs[x] = find_val(y, program_id)

def sub_register(x, y, program_id=0):
    "sub X Y"
    regs = registers[program_id]
    regs[x] -= find_val(y, program_id)

def multiply_register(x, y, program_id=0):
    "mul X Y"
    regs = registers[program_id]
    regs[x] = regs[x] * find_val(y, program_id)

def jump(x, y, program_id=0):
    "jnz X Y"
    if find_val(x, program_id) != 0:
        return find_val(y, program_id)
    return 1

def print_regs(register):
    print ' | '.join(['{0}: {1}'.format(x, register[x]) for x in 'abcdefgh'])


# Star 1
instructions = [x for x in DATA.split('\n')]
instructions_length = len(instructions)
mul_invoked = 0
pos = 0
instructions_executed = [0 for x in range(instructions_length)]
while True:
    instructions_executed[pos] += 1
    instruction = instructions[pos]
    # print "Iteration #{0}, Pos {1} Instruction: {2}".format(iteration, pos, instruction)
    args = instruction.split()
    offset = 1
    if args[0] == 'set':
        set_register(args[1], args[2])
        # print_regs(registers[0])
    elif args[0] == 'sub':
        sub_register(args[1], args[2])
        # print_regs(registers[0])
    elif args[0] == 'mul':
        mul_invoked += 1
        multiply_register(args[1], args[2])
        # print_regs(registers[0])
    elif args[0] == 'jnz':
        offset = jump(args[1], args[2])
    else:
        raise Exception('Could not parse instruction: {0}'.format(instruction))
    pos += offset
    if (pos < 0) or (pos >= instructions_length):
        print "Exceeded bounds - pos is: {0}".format(pos)
        break

print "mul has been invoked:\n{0}".format(mul_invoked)

# Star 2
# print "Register h:\n{0}".format(registers[0]['h'])
# print instructions_executed
# print registers[0]

# is_prime function shamefully stolen from SO:
# https://stackoverflow.com/questions/18833759/python-prime-number-checker
import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

composites_found = 0
for x in xrange(105700, 122701, 17):
    if not is_prime(x):
        composites_found += 1
print "Composites found:\n{0}".format(composites_found)
