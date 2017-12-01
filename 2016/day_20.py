from re import compile
from pprint import pprint as P
from time import sleep

pattern = compile(r'^(?P<start>\d+)-(?P<end>\d+)$')

with open('input_20.txt') as f:
    data = f.read().strip()

exclusion_matches = [pattern.search(x) for x in data.split('\n')]
exclusions = [(int(x.group('start')), int(x.group('end'))) for x in exclusion_matches]
exclusions = sorted(exclusions, key=lambda x: x[0])
# P(exclusions)

# exclude_up_to = 0


# Part 1
# for i in range(len(exclusions)):
#     if exclusions[i][1] + 1 < exclusions[i+1][0] and exclusions[i][1] + 1 > exclude_up_to:
#         print "Found it! Lowest number is: {0}".format(exclusions[i][1] + 1)
#         break
#     else:
#         exclude_up_to = max(exclude_up_to, exclusions[i][1])


def is_subset(exc1, exc2):
    if exc1[0] >= exc2[0] and exc1[1] <= exc2[1]:
        return True
    return False

def is_superset(exc1, exc2):
    if exc1[0] <= exc2[0] and exc1[1] >= exc2[1]:
        return True
    return False

def has_overlap(exc1, exc2):
    e1, e2 = sorted([exc1, exc2])
    if e1[1] + 1 >= e2[0]:
        return (e1[0], e2[1])
    return False


grouped_exclusions = []
previous_length_grouped_exclusions = -1

# Part 2
while len(grouped_exclusions) != previous_length_grouped_exclusions:
    previous_length_grouped_exclusions = len(grouped_exclusions)
    grouped_exclusions = []
    for exc in exclusions:
        subsumed = False
        for i in range(len(grouped_exclusions)):
            if is_subset(exc, grouped_exclusions[i]):
                subsumed = True
                break
            if is_superset(exc, grouped_exclusions[i]):
                grouped_exclusions[i] = exc
                subsumed = True
                break
            overlap = has_overlap(exc, grouped_exclusions[i])
            if overlap:
                grouped_exclusions[i] = overlap
                subsumed = True
                break
        if not subsumed:
            grouped_exclusions.append(exc)
    exclusions = grouped_exclusions[:]
    print "Made it through the loop! We now have {0} grouped exclusions.".format(len(grouped_exclusions))
    sleep(2)

print "Complete! Here are the exclusions:"
P(sorted(grouped_exclusions))

total = 0
for i in range(len(grouped_exclusions) - 1):
    total += grouped_exclusions[i+1][0] - grouped_exclusions[i][1] - 1

print "Available IPs:"
print total
