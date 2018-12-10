from itertools import chain, combinations
from collections import Counter, defaultdict

with open('input_data/24.txt') as f:
    DATA = f.read().strip()


def bridge_score(part_list):
    "Returns 0 if invalid bridge."
    links = list(chain(*part_list))
    c = Counter(links)
    if c[0] == 0:
        raise Exception("This isn't a valid bridge: {0}".format(parts_list))
    c_values = c.values()
    if c[0] % 2 == 1:
        # If an odd number of zeroes, there should be exactly two odd counts.
        if len([x for x in c_values if x % 2 == 1]) == 2:
            return sum([x[0] * x[1] for x in c.iteritems()])
        else:
            raise Exception("This isn't a valid bridge: {0}".format(parts_list))
    else:
        # Even number of zeroes means it ends in a zero, so there should be no odd counts.
        if len([x for x in c_values if x % 2 == 1]) == 0:
            return sum([x[0] * x[1] for x in c.iteritems()])
        else:
            raise Exception("This isn't a valid bridge: {0}".format(parts_list))


def find_the_path(part_list, end_number, part_mapping):
    "Return the score for a given part list"
    possible_connectors = [x for x in part_mapping[end_number] if tuple(sorted([x, end_number])) not in part_list]
    if not possible_connectors:
        return len(part_list), bridge_score(part_list)
    else:
        max_len, max_score = 0, 0
        for connector in possible_connectors:
            this_len, this_score = find_the_path(part_list + [tuple(sorted([connector, end_number]))], connector, part_mapping)
            if this_len > max_len:
                max_len, max_score = this_len, this_score
            elif this_len == max_len and this_score > max_score:
                max_len, max_score = this_len, this_score
        return max_len, max_score


# Let's try this again, brute forcing obviously won't work.
# We have no duplicate parts, thank goodness.
parts = [tuple(int(y) for y in x.split('/')) for x in DATA.split('\n')]
max_len, max_score = 0, 0

part_mapping = defaultdict(list)
for part in parts:
    part_mapping[part[0]].append(part[1])
    part_mapping[part[1]].append(part[0])


# Alright, do it.
for zero_connector in part_mapping[0]:
    this_len, this_score = find_the_path([(0, zero_connector)], zero_connector, part_mapping)
    if this_len > max_len:
        max_len, max_score = this_len, this_score
    elif this_len == max_len and this_score > max_score:
        max_len, max_score = this_len, this_score

print "Part 2 Complete! Max Score:\n{0}".format(max_score)
