import string
from time import sleep

with open('input_data/07.txt') as f:
    DATA = [x.strip() for x in f.readlines()]

rules = []
for instr in DATA:
    rules.append(instr[5] + instr[36])

all_letters = sorted(list(set(''.join(rules))))
prerequisites = {}
for letter in all_letters:
    prerequisites[letter] = [x[0] for x in rules if x[1] == letter]


def can_complete(letter, completed):
    for prereq in prerequisites[letter]:
        if prereq not in completed:
            return False
    return True


completed_route = ''
remaining_letters = ''.join(all_letters)
completed = set()

while True:
    for letter in remaining_letters[:]:
        if can_complete(letter, completed):
            completed_route += letter
            completed.add(letter)
            print "Route: {}".format(completed_route)
            remaining_letters = remaining_letters.replace(letter, '')
            break
    if not remaining_letters:
        break

print "Part 1 Complete!"
print "Route: {}".format(completed_route)

# Part 2, copy-pasting some stuff.

completed_route = ''
remaining_letters = ''.join(all_letters)
completed = set()
workers = []
seconds_elapsed = 0

while True:
    # Check for completed workers
    completed_workers = [x for x in workers if x[1] == 0]
    incomplete_workers = [x for x in workers if x[1] != 0]
    for cw in completed_workers:
        completed_route += cw[0]
        completed.add(cw[0])
        print "Route at {}: {}".format(completed_route, seconds_elapsed)
    workers = incomplete_workers

    # Check to see if steps can be started
    if len(workers) != 5:
        for letter in remaining_letters[:]:
            if can_complete(letter, completed):
                workers.append((letter, 61 + string.ascii_uppercase.index(letter)),)
                print "Beginning {} at {}...".format(letter, seconds_elapsed)
                remaining_letters = remaining_letters.replace(letter, '')
                if len(workers) == 5:
                    break

    if not remaining_letters and not workers:
        break

    # Time passes
    seconds_elapsed += 1
    workers = [(x, y-1) for x, y in workers]

print "Part 2 complete!"
print "Time elapsed: {}".format(seconds_elapsed)
