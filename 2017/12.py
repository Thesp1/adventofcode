with open('input_data/12.txt') as f:
    DATA = f.read().strip()

import re
PATTERN = re.compile(r'(?P<init_program>\d+) <-> (?P<list_of_programs>.*)')

def parse_line(line):
    match = PATTERN.search(line)
    if not match:
        raise Exception("Parser didn't parse correctly this instruction: {0}".format(line))
    program_name = int(match.group('init_program'))
    list_of_programs = match.group('list_of_programs')
    if list_of_programs:
        list_of_programs = [int(x) for x in list_of_programs.split(', ')]
    return program_name, list_of_programs


# Star 1
instructions = [parse_line(x) for x in DATA.split('\n')]
programs_dict = {key: val for key, val in instructions}
def find_linked_programs(val, seen=set()):
    seen.add(val)
    linked_programs = programs_dict[val]
    for prog in linked_programs:
        if prog not in seen:
            seen = find_linked_programs(prog, seen)
    return seen
total_linked_to_0 = find_linked_programs(0)
print "Answer 1:"
print len(total_linked_to_0)

# Star 2
groups_ever_seen = 0
progs_ever_seen = set()
for x in range(2000):
    # If we've seen this one, don't run it again, just move on.
    if x in progs_ever_seen:
        continue
    # Must be a new group!
    groups_ever_seen += 1
    progs_ever_seen = progs_ever_seen | find_linked_programs(x)
print "Answer 2:"
print groups_ever_seen
