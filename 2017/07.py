with open('input_data/07.txt') as f:
    DATA = f.read().strip()

import re
PATTERN = re.compile(r'(?P<prog>\w+) \((?P<weight>\d+)\)( -> )?(?P<held_progs>.+)?')

def parse_line(line):
    match = PATTERN.search(line)
    if not match:
        raise Exception("Parser didn't parse correctly this instruction: {0}".format(line))
    program_name = match.group('prog')
    program_weight = int(match.group('weight'))
    held_programs = match.group('held_progs')
    if held_programs:
        held_programs = held_programs.split(', ')
    else:
        held_programs = []
    return program_name, program_weight, held_programs


# Star 1
import itertools
programs = [parse_line(line) for line in DATA.split('\n')]
program_names = set([x[0] for x in programs])
programs_held = set(list(itertools.chain.from_iterable([x[2] for x in programs])))
print "Answer 1:"
print program_names - programs_held

# Star 2
programs = [parse_line(line) for line in DATA.split('\n')]
program_names = [x[0] for x in programs]
weights = {x[0]: x[1] for x in programs}
program_holders = {x[0]: x[2] for x in programs}

def held_weight(program_name):
    base_weight = weights[program_name]
    held_programs = program_holders[program_name]
    extra_weight = sum([held_weight(x) for x in held_programs])
    return base_weight + extra_weight

total_weights = {x: held_weight(x) for x in program_names}
print "Clues for Answer 2:"
for program in program_names:
    held_programs = program_holders[program]
    if held_programs:
        hpw = [total_weights[x] for x in held_programs]
        if len(set(hpw)) > 1:
            hpw = [(x, total_weights[x]) for x in held_programs]
            print "Program {0} ({1}) -> {2}".format(program, total_weights[program], hpw)

print "Finished!"
