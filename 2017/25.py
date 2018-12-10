from collections import defaultdict

# with open('input_data/25.txt') as f:
#     DATA = f.read().strip()

LEFT = -1
RIGHT = 1
A, B, C, D, E, F = 'A', 'B', 'C', 'D', 'E', 'F'


instructions = {A:
                    {0: dict(write=1, move=RIGHT, new_state=B),
                     1: dict(write=0, move=LEFT, new_state=E),},
                B:
                    {0: dict(write=1, move=LEFT, new_state=C),
                     1: dict(write=0, move=RIGHT, new_state=A),},
                C:
                    {0: dict(write=1, move=LEFT, new_state=D),
                     1: dict(write=0, move=RIGHT, new_state=C),},
                D:
                    {0: dict(write=1, move=LEFT, new_state=E),
                     1: dict(write=0, move=LEFT, new_state=F),},
                E:
                    {0: dict(write=1, move=LEFT, new_state=A),
                     1: dict(write=1, move=LEFT, new_state=C),},
                F:
                    {0: dict(write=1, move=LEFT, new_state=E),
                     1: dict(write=1, move=RIGHT, new_state=A),},
                }

tape = defaultdict(int)
pos = 0
current_state = A

for x in range(12386363):
    instruction = instructions[current_state][tape[pos]]
    tape[pos] = instruction['write']
    pos += instruction['move']
    current_state = instruction['new_state']

print "Part 1 Complete! Diagnostic Checksum:\n{0}".format(sum(tape.values()))
