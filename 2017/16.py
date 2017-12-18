import datetime

with open('input_data/16.txt') as f:
    DATA = f.read().strip()

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

def spin(programs, x):
    for i in xrange(x):
        programs = programs[-1:] + programs[:-1]
    return programs

def exchange(programs, a, b):
    programs[a], programs[b] = programs[b], programs[a]
    return programs

def partner(programs, a, b):
    index_a = programs.index(a)
    index_b = programs.index(b)
    programs[index_a], programs[index_b] = programs[index_b], programs[index_a]
    return programs

# Star 1
instructions = [x for x in DATA.split(',')]
for instruction in instructions:
    # print programs
    if instruction[0] == 's':
        x = int(instruction[1:])
        programs = spin(programs, x)
    elif instruction[0] == 'x':
        positions = [int(x) for x in instruction[1:].split('/')]
        programs = exchange(programs, *positions)
    elif instruction[0] == 'p':
        names = instruction[1:].split('/')
        programs = partner(programs, *names)
    else:
        raise Exception('Could not parse instruction: {0}'.format(instruction))

print "Answer 1:"
print ''.join(programs)


# Star 2
programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
seen_programs = [''.join(programs)]
for cycle in xrange(1000000000):
    for instruction in instructions:
        # print programs
        if instruction[0] == 's':
            x = int(instruction[1:])
            programs = spin(programs, x)
        elif instruction[0] == 'x':
            positions = [int(x) for x in instruction[1:].split('/')]
            programs = exchange(programs, *positions)
        elif instruction[0] == 'p':
            names = instruction[1:].split('/')
            programs = partner(programs, *names)
        else:
            raise Exception('Could not parse instruction: {0}'.format(instruction))
    if ''.join(programs) in seen_programs:
        # print "Found loop"
        # print len(seen_programs)
        # print seen_programs
        reverted_cycle_num = cycle + 1
        # print reverted_cycle_num
        print "Answer 2:"
        print ''.join(seen_programs[1000000000 % reverted_cycle_num])
        break
    else:
        seen_programs.append(''.join(programs))
