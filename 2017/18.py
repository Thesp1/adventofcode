with open('input_data/18.txt') as f:
    DATA = f.read().strip()

from collections import defaultdict
registers = {0: defaultdict(int),
             1: defaultdict(int)}
registers[0]['p'] = 0
registers[1]['p'] = 1

def find_val(x, program_id=0):
    regs = registers[program_id]
    try:
        val = int(x)
    except ValueError:
        val = regs[x]
    return val

def play_sound(x):
    "snd X (1st star)"
    sound_played = find_val(x)
    print "Playing sound - {0}".format(sound_played)
    return sound_played

def recover_sound(x):
    "rcv X (1st star)"
    if find_val(x):
        return True
    return False

def set_register(x, y, program_id=0):
    "set X Y"
    regs = registers[program_id]
    regs[x] = find_val(y, program_id)

def add_register(x, y, program_id=0):
    "add X Y"
    regs = registers[program_id]
    regs[x] += find_val(y, program_id)

def multiply_register(x, y, program_id=0):
    "mul X Y"
    regs = registers[program_id]
    regs[x] = regs[x] * find_val(y, program_id)

def modulus_register(x, y, program_id=0):
    "mod X Y"
    regs = registers[program_id]
    regs[x] = regs[x] % find_val(y, program_id)

def jump(x, y, program_id=0):
    "jgz X Y"
    if find_val(x, program_id) > 0:
        return find_val(y, program_id)
    return 1

def send(x, program_id):
    "snd X (2nd star)"
    return find_val(x, program_id)

def receive(x, val, program_id):
    "rcv X (2nd star)"
    registers[program_id][x] = val


# Star 1
# instructions = [x for x in DATA.split('\n')]
# instructions_length = len(instructions)
# last_sound_played = None
# last_sound_recovered = None
# pos = 0
# while True:
#     instruction = instructions[pos]
#     args = instruction.split()
#     offset = 1
#     if args[0] == 'snd':
#         last_sound_played = play_sound(args[1])
#     elif args[0] == 'set':
#         set_register(args[1], args[2])
#     elif args[0] == 'add':
#         add_register(args[1], args[2])
#     elif args[0] == 'mul':
#         multiply_register(args[1], args[2])
#     elif args[0] == 'mod':
#         modulus_register(args[1], args[2])
#     elif args[0] == 'rcv':
#         if recover_sound(args[1]):
#             last_sound_recovered = last_sound_played
#             print "Sound Answer 1:"
#             print last_sound_recovered
#             break
#     elif args[0] == 'jgz':
#         offset = jump(args[1], args[2])
#     else:
#         raise Exception('Could not parse instruction: {0}'.format(instruction))
#     pos += offset
#     if (pos < 0) or (pos > instructions_length):
#         print "Exceeded bounds - pos is: {0}".format(pos)
#         break


# Star 2
instructions = [x for x in DATA.split('\n')]
instructions_length = len(instructions)
pos = {0: 0, 1: 0}
offset = {0: 0, 1: 0}
queues = {0: [],
          1: []}
prog_1_sends = 0
while True:
    for program_id in range(2):
        if (pos[program_id] < 0) or (pos[program_id] > instructions_length):
            print "Program {0} stalled at pos {1}.".format(program_id, pos[program_id])
            offset[program_id] = 0
            continue
        offset[program_id] = 1
        instruction = instructions[pos[program_id]]
        args = instruction.split()
        # print programs
        if args[0] == 'snd':
            if program_id == 1:
                prog_1_sends += 1
            val_to_send = send(args[1], program_id)
            queue_prog_id = 0 if program_id == 1 else 1
            queues[queue_prog_id].append(val_to_send)
        elif args[0] == 'set':
            set_register(args[1], args[2], program_id)
        elif args[0] == 'add':
            add_register(args[1], args[2], program_id)
        elif args[0] == 'mul':
            multiply_register(args[1], args[2], program_id)
        elif args[0] == 'mod':
            modulus_register(args[1], args[2], program_id)
        elif args[0] == 'rcv':
            if queues[program_id]:
                receive_val = queues[program_id].pop(0)
                receive(args[1], receive_val, program_id)
            else:
                # print "Program {0} waiting...".format(program_id)
                offset[program_id] = 0
        elif args[0] == 'jgz':
            offset[program_id] = jump(args[1], args[2], program_id)
        else:
            raise Exception('Could not parse instruction: {0}'.format(instruction))
        pos[program_id] += offset[program_id]
    if offset[0] == 0 and offset[1] == 0:
        print "Answer 2:"
        print prog_1_sends
        print pos
        raise Exception

