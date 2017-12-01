from advent_input import *

# Day 1
def find_first_basement(s):
    floor = 0
    for pos, c in enumerate(s, start=1):
        if c == '(':
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            print "First basement hit at step: {}".format(pos)
            break

# Day 2
def find_sq_feet(l, w, h):
    l, w, h = int(l), int(w), int(h)
    ss_dims = sorted([l, w, h])[:2]
    ss_area = ss_dims[0] * ss_dims[1]
    return 2 * (l * w) + 2 * (w * h) + 2 * (l * h) + ss_area

def total_square_feet(s):
    present_dims = [x.split('x') for x in s.split()]
    return sum(find_sq_feet(*x) for x in present_dims)

def find_ribbon_length(l, w, h):
    l, w, h = int(l), int(w), int(h)
    ss_dims = sorted([l, w, h])[:2]
    ss_perim = 2 * ss_dims[0] + 2 * ss_dims[1]
    return l * w * h + ss_perim

def total_ribbon_length(s):
    present_dims = [x.split('x') for x in s.split()]
    return sum(find_ribbon_length(*x) for x in present_dims)

# Day 3
from collections import Counter

def generate_present_map(s, size=None):
    if not size:
        size = (2 * max(Counter(s).values())) + 1
    house_map = [[0 for x in xrange(size)] for x in xrange(size)]
    center_val = (size / 2)
    location = [center_val, center_val]
    house_map[location[0]][location[1]] += 1
    for c in s:
        if c == '>':
            location[0] += 1
        elif c == '<':
            location[0] -= 1
        elif c == '^':
            location[1] += 1
        elif c == 'v':
            location[1] -= 1
        house_map[location[0]][location[1]] += 1
    return house_map

def find_total_houses(s):
    house_map = generate_present_map(s)
    total = sum([len(list([x for x in y if x > 0])) for y in house_map])
    return total

def find_robo_santa_houses(s):
    size = (2 * max(Counter(s).values())) + 1
    first_santa_string = s[::2]
    second_santa_string = s[1::2]
    first_map = generate_present_map(first_santa_string, size=size)
    second_map = generate_present_map(second_santa_string, size=size)
    for x in range(size):
        for y in range(size):
            first_map[x][y] += second_map[x][y]
    total = sum([len(list([x for x in y if x > 0])) for y in first_map])
    return total

# Day 4
from hashlib import md5

def find_lowest_hash(s):
    c = 1
    while True:
        h = md5(s + str(c)).hexdigest()
        if h[:6] == '000000':
            print "Found it! Integer is {0} and hash is {1}.".format(c, h)
            break
        if c % 10000 == 0:
            print "Number {0} failed with hash of {1}...".format(c, h)
        c += 1

# Day 5
def min_three_vowels(s):
    return bool(len([x for x in s if x in 'aeiou']) >= 3)

def repeated_letter(s):
    for x in range(len(s)):
        try:
            if s[x] == s[x + 1]:
                return True
        except IndexError:
            return False

def has_bad_string(s):
    return ('ab' in s) or ('cd' in s) or ('pq' in s) or ('xy' in s)

def repeated_pair(s):
    for x in range(len(s)):
        try:
            pair = s[x] + s[x + 1]
        except IndexError:
            return False
        if pair in s[x + 2:]:
            return True

def split_pair(s):
    for x in range(len(s)):
        try:
            if s[x] == s[x + 2]:
                return True
        except IndexError:
            return False

def check_list_first(l):
    total = 0
    for s in l.split():
        if min_three_vowels(s) and repeated_letter(s) and not has_bad_string(s):
            print "{0} is nice!".format(s)
            total += 1
        else:
            print "{0} is naughty!".format(s)
    print "Total nice: {0}".format(total)

def check_list_second(l):
    total = 0
    for s in l.split():
        if repeated_pair(s) and split_pair(s):
            print "{0} is nice!".format(s)
            total += 1
        else:
            print "{0} is naughty!".format(s)
    print "Total nice: {0}".format(total)

# Day 6
def flip_lights(instruction, first_coord, second_coord, matrix):
    for x in range(first_coord[0], second_coord[0] + 1):
        for y in range(first_coord[1], second_coord[1] + 1):
            if instruction == 'turnon':
                matrix[x][y] = True
            elif instruction == 'turnoff':
                matrix[x][y] = False
            else:
                matrix[x][y] = not matrix[x][y]
    return matrix

def interpret_instruction(s):
    l = s.replace('n o', 'no').replace('through ', '').split(' ')
    instruction = l[0]
    first_coord = tuple([int(x) for x in l[1].split(',')])
    second_coord = tuple([int(x) for x in l[2].split(',')])
    return instruction, first_coord, second_coord

def count_lights(matrix):
    total = sum([len(list([x for x in y if x])) for y in matrix])
    return total

def flip_lights_2(instruction, first_coord, second_coord, matrix):
    for x in range(first_coord[0], second_coord[0] + 1):
        for y in range(first_coord[1], second_coord[1] + 1):
            if instruction == 'turnon':
                matrix[x][y] += 1
            elif instruction == 'turnoff':
                if matrix[x][y] > 0:
                    matrix[x][y] -= 1
            else:
                matrix[x][y] += 2
    return matrix

def count_lights_2(matrix):
    total = sum([sum(x) for x in matrix])
    return total

def count_flipped_lights(s):
    matrix = [[False for x in range(1000)] for y in range(1000)]
    for op in s.split('\n'):
        instruction, first_coord, second_coord = interpret_instruction(op)
        matrix = flip_lights(instruction, first_coord, second_coord, matrix)
    total = count_lights(matrix)
    print "There are {0} lights on.".format(total)

def count_flipped_lights_2(s):
    matrix = [[0 for x in range(1000)] for y in range(1000)]
    for op in s.split('\n'):
        instruction, first_coord, second_coord = interpret_instruction(op)
        matrix = flip_lights_2(instruction, first_coord, second_coord, matrix)
    total = count_lights_2(matrix)
    print "The total brightness is {0}.".format(total)

# Day 7 (largely cribbed from another answer)
def find_gate_value(s):
    results = {}
    calc = {}
    for command in s.split('\n'):
        ops, res = command.split('->')
        calc[res.strip()] = ops.strip().split(' ')

    # For step 2...
    calc['b'] = ['3176']

    def calculate(name):
        try:
            return int(name)
        except ValueError:
            pass

        if name not in results:
            ops = calc[name]
            if len(ops) == 1:
                res = calculate(ops[0])
            else:
                op = ops[-2]
                if op == 'AND':
                  res = calculate(ops[0]) & calculate(ops[2])
                elif op == 'OR':
                  res = calculate(ops[0]) | calculate(ops[2])
                elif op == 'NOT':
                  res = ~calculate(ops[1]) & 0xffff
                elif op == 'RSHIFT':
                  res = calculate(ops[0]) >> calculate(ops[2])
                elif op == 'LSHIFT':
                  res = calculate(ops[0]) << calculate(ops[2])
            results[name] = res
        return results[name]

    val = calculate('a')
    print val

# Day 8 (also largely cribbed)
def find_length_differences():
    total = sum(len(s[:-1]) - len(eval(s)) for s in open('advent_day_8.txt'))
    print "Difference is: {0}.".format(total)
    total2 = sum(2+s.count('\\')+s.count('"') for s in open('advent_day_8.txt'))
    print "Second difference is: {0}.".format(total2)

# Day 9
def find_path():
    from itertools import permutations, chain
    lines = [x.strip() for x in open('advent_day_9.txt')]
    sets = [x.split(' = ') for x in lines]
    length_dict = {tuple(sorted(x[0].split(' to '))): int(x[1]) for x in sets}
    cities = sorted(list(set(chain.from_iterable(length_dict.keys()))))
    num_cities = len(cities)
    possibilities = permutations(cities)
    max_path = 0
    for poss in possibilities:
        path_sum = 0
        for x in range(num_cities - 1):
            path_sum += length_dict[tuple(sorted([poss[x], poss[x + 1]]))]
        max_path = max(max_path, path_sum)
    print "The longest route is: {0}.".format(max_path)

# Day 10
def look_and_say(s):
    final_s = ''
    while s:
        first_char = s[0]
        new_s = s.lstrip(first_char)
        occurrences = len(s) - len(new_s)
        final_s += str(occurrences) + first_char
        s = new_s
    return final_s

def look_say_times(s, t):
    for i in range(t):
        s = look_and_say(s)
        print "Cycle {0} complete!".format(i)
    print "Final string length is: {}".format(len(s))

# Day 11
next_letter_mapping = {'a': 'b', 'c': 'd', 'b': 'c', 'e': 'f', 'd': 'e', 'g': 'h', 'f': 'g', 'h': 'j', 'k': 'm', 'j': 'k', 'm': 'n', 'n': 'p', 'q': 'r', 'p': 'q', 's': 't', 'r': 's', 'u': 'v', 't': 'u', 'w': 'x', 'v': 'w', 'y': 'z', 'x': 'y', 'z': 'a'}
required_strings = ('abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz')

def increment_letter(c):
    return next_letter_mapping[c]

def increment_string(s):
    i = -1
    l = len(s)
    s_list = list(s)
    while True:
        s_list[i] = increment_letter(s_list[i])
        if s_list[i] != 'a':
            return ''.join(s_list)
        i -= 1

def includes_raising_string(s):
    for req in required_strings:
        if req in s:
            return True
    return False

def repeated_different_pair(s):
    for x in range(len(s)):
        try:
            first_pair_match = bool(s[x] == s[x + 1])
        except IndexError:
            return False
        if first_pair_match:
            for y in range(x, len(s)):
                try:
                    second_pair_match = bool(s[y] == s[y + 1] != s[x])
                except IndexError:
                    continue
                if second_pair_match:
                    return True
    return False

def find_next_password(s):
    while True:
        print "Trying {}...".format(s)
        if includes_raising_string(s) and repeated_different_pair(s):
            print "Found it! This works: {0}".format(s)
            return
        s = increment_string(s)

# Day 12
import json
import re
def find_numbers_part_one(s):
    patt = re.compile(r'[-0123456789]+')
    print "Sum of all numbers in string: {0}".format(sum([int(x) for x in re.findall(patt, s)]))

def return_non_dict_non_red(obj):
    if type(obj) == dict:
        if 'red' in obj.values():
            return []
        return [return_non_dict_non_red(x) for x in obj.keys()] + \
               [return_non_dict_non_red(x) for x in obj.values()]
    if type(obj) == list:
        return [return_non_dict_non_red(x) for x in obj]
    return obj

def find_nonred_numbers(s):
    s = json.loads(s)
    flattened_s = return_non_dict_non_red(s)
    find_numbers_part_one(repr(flattened_s))

# Day 13
def find_sits_by_dict(include_me=False):
    lines = [x.strip().rstrip('.') for x in open('advent_day_13.txt')]
    lines = [x.replace('would ', '').replace('happiness units by sitting next to ', '') for x in lines]
    lines = [x.replace('gain ', '').replace('lose ', '-') for x in lines]
    lines = [x.split(' ') for x in lines]
    people = set([x[0] for x in lines])
    sb = {x: dict() for x in people}
    for line in lines:
        sb[line[0]][line[2]] = int(line[1])
    if include_me:
        sb['Me'] = dict()
        for person in people:
            sb['Me'][person] = 0
            sb[person]['Me'] = 0
    return sb

def find_max_happy(include_me=False):
    sb = find_sits_by_dict(include_me)
    people = sb.keys()
    def find_double_happy(a, b):
        return sb[a][b] + sb[b][a]
    from itertools import permutations
    max_happy = -999999999
    people_count = len(people)
    for seating in permutations(people):
        happy = find_double_happy(seating[0], seating[-1])
        for i in range(people_count - 1):
            happy += find_double_happy(seating[i], seating[i+1])
        if happy > max_happy:
            max_happy = happy
            final_arrangement = seating
    print "Max happiness is: {0} with seating arrangement {1}.".format(max_happy, final_arrangement)

# Day 14
def find_speeds():
    lines = [x.strip().rstrip(' seconds.') for x in open('advent_day_14.txt')]
    lines = [x.replace('can fly ', '').replace('km/s for ', '').replace('seconds, but then must rest for ', '') for x in lines]
    lines = [x.split(' ') for x in lines]
    speeds = {x[0]: {'distance': int(x[1]), 'duration': int(x[2]), 'rest': int(x[3])} for x in lines}
    return speeds

def find_distance(distance, duration, rest, total_time):
    full_cycle_time = duration + rest
    full_cycle_distance = distance * duration
    total_distance = full_cycle_distance * (total_time / full_cycle_time)
    extra_time = total_time % full_cycle_time
    total_distance += distance * min(duration, extra_time)
    return total_distance

def find_winning_reindeer(total_time):
    speeds = find_speeds()
    max_dist = max([find_distance(x['distance'], x['duration'], x['rest'], total_time) for x in speeds.values()])
    print "Fastest reindeer goes: {0}".format(max_dist)

def find_points_winner(total_time):
    speeds = find_speeds()
    reindeer = speeds.keys()
    scores = {r: 0 for r in reindeer}
    distances = {r: 0 for r in reindeer}
    for l in range(1, total_time + 1):
        distances = {r: find_distance(x['distance'], x['duration'], x['rest'], l) for r, x in speeds.items()}
        furthest = max(distances.values())
        for r in reindeer:
            if distances[r] == furthest:
                scores[r] += 1
    print "The highest score is: {0}".format(max(scores.values()))

# Day 15
def find_ingredient_dict():
    lines = [x.strip() for x in open('advent_day_15.txt')]
    ingreds_draft = {x.split(': ')[0]: x.split(': ')[1] for x in lines}
    ingreds = {}
    for ingred, val in ingreds_draft.items():
        ingreds[ingred] = {x.split(' ')[0]: int(x.split(' ')[1]) for x in val.split(', ')}
    return ingreds

def find_best_cookie():
    raise Exception("Don't use this method, it's terrible.")
    from itertools import product
    import operator
    import functools
    from collections import Counter
    labels = find_ingredient_dict()
    ingredients_list = labels.keys()
    qualities_list = labels.itervalues().next().keys()
    max_total = 0
    loops = 0
    for recipe in product(ingredients_list, repeat=100):
        loops += 1
        current_val = {x: 0 for x in qualities_list}
        for ingredient in recipe:
            for quality in qualities_list:
                current_val[quality] += labels[ingredient][quality]
        total_list = [x if x > 0 else 0 for x in current_val.values()]
        total = functools.reduce(operator.mul, total_list, 1)
        if total > max_total:
            print "New max total: {0}".format(total)
            max_total = total
            best_recipe = recipe
        if loops % 100000 == 0:
            print "Just finished loop {0}.".format(loops)
            print "Recipe was: {0}.".format(Counter(recipe))
    print "Final total is: {0}".format(max_total)
    print "Best recipe is: {0}".format(Counter(best_recipe))

def find_best_cookie_2(calorie_checking=False):
    import operator
    import functools
    labels = find_ingredient_dict()
    print labels
    ingredients_list = labels.keys()
    qualities_list = labels.itervalues().next().keys()
    qualities_list.pop(qualities_list.index('calories'))
    max_total = 0
    for frosting in range(0, 101):
        for candy in range(0, 101 - frosting):
            for butterscotch in range(0, 101 - frosting - candy):
                sugar = 100 - frosting - candy - butterscotch
                quant_dict = dict(Frosting=frosting, Candy=candy,
                                  Butterscotch=butterscotch, Sugar=sugar)
                total_list = []
                # Calorie checking
                if calorie_checking:
                    cal_list = [labels[ingredient]['calories'] * quant_dict[ingredient] for ingredient in ingredients_list]
                    if sum(cal_list) != 500:
                        continue
                for quality in qualities_list:
                    val_list = [labels[ingredient][quality] * quant_dict[ingredient] for ingredient in ingredients_list]
                    total_list.append(max(sum(val_list), 0))
                total = functools.reduce(operator.mul, total_list, 1)
                if total > max_total:
                    print "New max total: {0}".format(total)
                    max_total = total
                    best_recipe = quant_dict
    print "Final total is: {0}".format(max_total)
    print "Best recipe is: {0}".format(quant_dict)

# Day 16
def find_sue_data():
    lines = [x.strip().lstrip('Sue ') for x in open('advent_day_16.txt')]
    parts_draft = {int(x.split(': ', 1)[0]): x.split(': ', 1)[1] for x in lines}
    parts = {}
    for part, val in parts_draft.items():
        parts[part] = {x.split(': ')[0]: int(x.split(': ')[1]) for x in val.split(', ')}
    return parts

def find_possible_sues(second_part=False):
    sue_data = find_sue_data()
    good_data = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,
                 "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3,
                 "cars": 2, "perfumes": 1,}
    for sue_number, data in sue_data.items():
        potential_match = True
        for quality, quantity in data.items():
            if not second_part:
                if (quality in good_data) and quantity != good_data[quality]:
                    potential_match = False
            else:
                if quality in good_data:
                    if (quality in ('cats', 'trees')):
                        if quantity <= good_data[quality]:
                            potential_match = False
                    elif (quality in ('pomeranians', 'goldfish')):
                        if quantity >= good_data[quality]:
                            potential_match = False
                    else:
                        if quantity != good_data[quality]:
                            potential_match = False
        if potential_match:
            print "Sue #{0} is a potential match: {1}.".format(sue_number, data)

# Day 17
def get_containers():
    lines = [int(x.strip()) for x in open('advent_day_17.txt')]
    return sorted(lines, reverse=True)

def masked_sum(cont_list, mask):
    l = zip(cont_list, mask)
    return sum([x[0] for x in l if x[1]])

def find_possibilities(storage_total=150, find_minimum=False):
    total = 0
    min_containers = 9999
    containers = get_containers()
    from itertools import product
    for mask in product([True, False], repeat=len(containers)):
        if masked_sum(containers, mask) == storage_total:
            total += 1
            if find_minimum:
                cont_used = len([x for x in mask if x])
                if cont_used < min_containers:
                    min_containers = cont_used
    print "There were {} possibilities.".format(total)
    if find_minimum:
        print "Minimum container usage was {0}. Let's do this again!".format(min_containers)
        total = 0
        for mask in product([True, False], repeat=len(containers)):
            if len([x for x in mask if x]) != min_containers:
                continue
            if masked_sum(containers, mask) == storage_total:
                total += 1
        print "There were {0} possibilities with {1} containers.".format(total, min_containers)

# Day 18
def get_preset_lights():
    lines = [x.strip() for x in open('advent_day_18.txt')]
    matrix = [[False for x in range(100)] for y in range(100)]
    for x in range(100):
        for y in range(100):
            if lines[x][y] == '#':
                matrix[x][y] = True
    return matrix

def flip_switch(x, y, matrix, current_state):
    if x not in (0, 99) and y not in (0, 99):
        lights = [matrix[x-1][y-1], matrix[x][y-1], matrix[x+1][y-1],
                  matrix[x-1][y],                   matrix[x+1][y],
                  matrix[x-1][y+1], matrix[x][y+1], matrix[x+1][y+1]]
    elif x == 0 and y == 0:
        return True
        #lights = [                matrix[x+1][y],
        #          matrix[x][y+1], matrix[x+1][y+1]]
    elif x == 0 and y == 99:
        return True
        #lights = [                  matrix[x][y-1], matrix[x+1][y-1],
        #                                            matrix[x+1][y]]
    elif x == 99 and y == 0:
        return True
        #lights = [matrix[x-1][y],
        #          matrix[x-1][y+1], matrix[x][y+1]]
    elif x == 99 and y == 99:
        return True
        #lights = [matrix[x-1][y-1], matrix[x][y-1],
        #          matrix[x-1][y]]
    elif x == 0:
        lights = [                  matrix[x][y-1], matrix[x+1][y-1],
                                                    matrix[x+1][y],
                                    matrix[x][y+1], matrix[x+1][y+1]]
    elif x == 99:
        lights = [matrix[x-1][y-1], matrix[x][y-1],
                  matrix[x-1][y],
                  matrix[x-1][y+1], matrix[x][y+1]]
    elif y == 0:
        lights = [matrix[x-1][y],                   matrix[x+1][y],
                  matrix[x-1][y+1], matrix[x][y+1], matrix[x+1][y+1]]
    elif y == 99:
        lights = [matrix[x-1][y-1], matrix[x][y-1], matrix[x+1][y-1],
                  matrix[x-1][y],                   matrix[x+1][y]]
    else:
        raise Exception("This shouldn't have happened. {0}, {1} are coords.".format(x, y))
    count = len([x for x in lights if x])
    if current_state and count not in (2, 3):
        return False
    if (not current_state) and count == 3:
        return True
    return current_state

def count_lights(matrix):
    total = sum([len(list([x for x in y if x])) for y in matrix])
    return total

def cycle_lights(steps=100):
    matrix = get_preset_lights()
    matrix[0][0], matrix[0][99], matrix[99][0], matrix[99][99] = True, True, True, True
    for cycle in range(steps):
        new_matrix = [[None for x in range(100)] for y in range(100)]
        for x in range(100):
            for y in range(100):
                new_matrix[x][y] = flip_switch(x, y, matrix, matrix[x][y])
        matrix = new_matrix
        print "Cycle complete!"
    total = count_lights(matrix)
    print "The final tally of lights on is: {0}.".format(total)
    return matrix

# Day 19
def get_molecule_with_replacements():
    lines = [x.strip() for x in open('advent_day_19.txt') if '=>' in x]
    molecule = [x.strip() for x in open('advent_day_19.txt') if 'CRnSiRnCaPTiMgYCaPTiRnF' in x][0]
    from collections import defaultdict
    d = defaultdict(list)
    for line in lines:
        vals = line.split(' => ')
        key, val = vals[0], vals[1]
        d[key].append(val)
    return d, molecule

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def find_possible_replacements():
    rep, molecule = get_molecule_with_replacements()
    poss_strings = []
    for key1 in rep.keys():
        for key2 in rep[key1]:
            for x in range(molecule.count(key1)):
                xth_index = find_nth(molecule, key1, x+1)
                poss_strings.append(molecule[:xth_index] + molecule[xth_index:].replace(key1, key2, 1))
    pss = set(poss_strings)
    print "Possibles: {0}.".format(len(pss))

def get_molecule_with_replacements2():
    lines = [x.strip() for x in open('advent_day_19.txt') if '=>' in x]
    molecule = [x.strip() for x in open('advent_day_19.txt') if 'CRnSiRnCaPTiMgYCaPTiRnF' in x][0]
    d = dict()
    for line in lines:
        vals = line.split(' => ')
        key, val = vals[1], vals[0]
        d[key] = val
    return d, molecule


def hunt_for_e():
    from random import shuffle
    rep, molecule = get_molecule_with_replacements2()
    cycle = 0
    while True:
        cycle += 1
        found_one = False
        l = rep.keys()
        shuffle(l)
        for s in l:
            if s in molecule:
                molecule = molecule.replace(s, rep[s], 1)
                found_one = True
                print "At step {0}, molecule is now: {1}".format(cycle, molecule)
                break
        if not found_one:
            print "Didn't find a replacement for string {0}.".format(molecule)
            print "Retrying..."
            cycle = 0
        if molecule == 'e':
            print "Molecule is now 'e' at cycle {0}.".format(cycle)
            break

# Day 20
def factors(n):
    return list(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def house_presents(h):
    try:
        return sum([x * 11 for x in factors(h) if h <= x * 50])
    except:
        raise Exception('Problem with {0}.'.format(h))

def find_min_presents(val=36000000):
    for x in range(1, val):
        presents = house_presents(x)
        if presents >= val:
            print "{0} presents at house {1}.".format(presents, x)
            break

# Day 21
def combat(player_hp, player_dmg, player_armor, boss_hp, boss_dmg, boss_armor):
    while player_hp > 0 and boss_hp > 0:
        # Player hits
        boss_hp -= max(1, player_dmg - boss_armor)
        if boss_hp <= 0:
            return True
        player_hp -= max(1, boss_dmg - player_armor)
        if player_hp <= 0:
            return False

def find_cheapest_equipment(player_hp=100, gold=100):
    from itertools import combinations
    boss_hp = 104
    boss_dmg = 8
    boss_armor = 1
    WEAPONS = [
        ['Dagger', 8, 4, 0],
        ['Shortsword', 10, 5, 0],
        ['Warhammer', 25, 6, 0],
        ['Longsword', 40, 7, 0],
        ['Greataxe', 74, 8, 0],
    ]
    ARMORS = [
        ['No Armor', 0, 0, 0],
        ['Leather', 13, 0, 1],
        ['Chainmail', 31, 0, 2],
        ['Splintmail', 53, 0, 3],
        ['Bandedmail', 75, 0, 4],
        ['Platemail', 102, 0, 5],
    ]
    ACCESSORIES = [
        ['None 1', 0, 0, 0],
        ['None 2', 0, 0, 0],
        ['Damage +1', 25, 1, 0],
        ['Damage +2', 50, 2, 0],
        ['Damage +3', 100, 3, 0],
        ['Defense +1', 20, 0, 1],
        ['Defense +2', 40, 0, 2],
        ['Defense +3', 80, 0, 3],
    ]
    # least_gold_spent = 99999
    most_gold_spent = 0
    for weapon in WEAPONS:
        for armor in ARMORS:
            for acc1, acc2 in combinations(ACCESSORIES, 2):
                player_dmg = weapon[2] + acc1[2] + acc2[2]
                player_armor = armor[3] + acc1[3] + acc2[3]
                # if combat(player_hp, player_dmg, player_armor, boss_hp, boss_dmg, boss_armor):
                if not combat(player_hp, player_dmg, player_armor, boss_hp, boss_dmg, boss_armor):
                    gold_spent = weapon[1] + armor[1] + acc1[1] + acc2[1]
                    # if gold_spent < least_gold_spent:
                    if gold_spent > most_gold_spent:
                        # print "Least gold record set for {0}gp on {1}, {2}, {3}, {4}.".format(gold_spent, weapon[0], armor[0], acc1[0], acc2[0])
                        print "Most gold record set for {0}gp on {1}, {2}, {3}, {4}.".format(gold_spent, weapon[0], armor[0], acc1[0], acc2[0])
                        most_gold_spent = gold_spent

# Day 22
class OutOfSpells(Exception):
    pass

class PlayerLoss(Exception):
    pass

class GameState:
    def __init__(self, spell_order):
        self.player_hp = 50
        self.player_armor = 0
        self.player_mana = 500
        self.boss_hp = 51
        self.boss_dmg = 9
        self.mana_spent = 0
        self.shield_timer = 0
        self.poison_timer = 0
        self.recharge_timer = 0
        self.spell_order = spell_order
        self.SPELLS = {
            'Magic Missile': 53,
            'Drain': 73,
            'Shield': 113,
            'Poison': 173,
            'Recharge': 229,
        }

    def check_valid_spell_selection(self, spell):
        if (self.poison_timer and spell == 'Poison') \
               or (self.shield_timer and spell == 'Shield') \
               or (self.recharge_timer and spell == 'Recharge'):
            return False
        if self.SPELLS[spell] > self.player_mana:
            return False
        return True

    def run_poison(self):
        if self.poison_timer:
            self.boss_hp -= 3
            self.poison_timer -= 1

    def run_shield(self):
        if self.shield_timer:
            self.player_armor = 7
            self.shield_timer -= 1
        else:
            self.player_armor = 0

    def run_recharge(self):
        if self.recharge_timer:
            self.recharge_timer -= 1
            self.player_mana += 101

    def run_turn_start_things(self):
        self.run_poison()
        self.run_shield()
        self.run_recharge()

    def cast_spell(self, spell):
        if spell == 'Magic Missile':
            self.boss_hp -= 4
        elif spell == 'Drain':
            self.boss_hp -= 2
            self.player_hp += 2
        elif spell == 'Shield':
            self.shield_timer = 6
        elif spell == 'Poison':
            self.poison_timer = 6
        elif spell == 'Recharge':
            self.recharge_timer = 5
        else:
            raise Exception('Bad spell!')
        spell_mana_spent = self.SPELLS[spell]
        self.player_mana -= spell_mana_spent
        self.mana_spent += spell_mana_spent

    def check_victory(self):
        if self.boss_hp <= 0:
            return True
        if self.player_hp <= 0:
            raise PlayerLoss
        return False

    def run_combat(self):
        for spell in self.spell_order:
            # Player's Turn
            # Hard mode here!
            self.player_hp -= 1
            if self.check_victory():
                return self.mana_spent
            self.run_turn_start_things()
            if self.check_victory():
                return self.mana_spent
            if not self.check_valid_spell_selection(spell):
                raise PlayerLoss
            self.cast_spell(spell)
            if self.check_victory():
                return self.mana_spent
            # Boss Turn
            self.run_turn_start_things()
            if self.check_victory():
                return self.mana_spent
            self.player_hp -= max(1, self.boss_dmg - self.player_armor)
            if self.check_victory():
                return self.mana_spent
        raise OutOfSpells

def find_least_mana():
    valid_spell_paths = [['Magic Missile',], ['Drain',], ['Shield',], ['Poison',], ['Recharge',],]
    least_mana_spent = 9999999
    while valid_spell_paths:
        spell_path = valid_spell_paths.pop()
        gs = GameState(spell_path)
        try:
            mana_spent = gs.run_combat()
        except PlayerLoss:
            continue
        except OutOfSpells:
            last_spell = spell_path[-1]
            valid_spell_paths.append(spell_path + ['Magic Missile'])
            valid_spell_paths.append(spell_path + ['Drain'])
            if last_spell != 'Shield':
                valid_spell_paths.append(spell_path + ['Shield'])
            if last_spell != 'Poison':
                valid_spell_paths.append(spell_path + ['Poison'])
            if last_spell != 'Recharge':
                valid_spell_paths.append(spell_path + ['Recharge'])
            continue
        # Made it here? We won!
        if mana_spent < least_mana_spent:
            print "{0} mana spent on spells: {1}".format(mana_spent, ', '.join(spell_path))
            least_mana_spent = mana_spent
    print "Victory at {0} mana spent.".format(least_mana_spent)


# Day 23
def find_reg_vals():
    lines = [x.strip() for x in open('advent_day_23.txt')]
    pos = 0
    a = 1
    b = 0
    while True:
        inst, val = lines[pos].split(' ', 1)
        if inst == 'hlf':
            if val == 'a':
                a = a / 2
            else:
                b = b / 2
            pos += 1
        elif inst == 'tpl':
            if val == 'a':
                a = a * 3
            else:
                b = b * 3
            pos += 1
        elif inst == 'inc':
            if val == 'a':
                a += 1
            else:
                b += 1
            pos += 1
        elif inst == 'jmp':
            pos += int(val)
        elif inst == 'jie':
            val, pos_shift = val.split(', ')
            if val == 'a':
                if a % 2 == 0:
                    pos += int(pos_shift)
                else:
                    pos += 1
            else:
                if b % 2 == 0:
                    pos += int(pos_shift)
                else:
                    pos += 1
        elif inst == 'jio':
            val, pos_shift = val.split(', ')
            if val == 'a':
                if a == 1:
                    pos += int(pos_shift)
                else:
                    pos += 1
            else:
                if b == 1:
                    pos += int(pos_shift)
                else:
                    pos += 1
        else:
            raise Exception('Something went wrong.')
        print pos, a, b
        if pos >= len(lines) or pos < 0:
            break
    print "Value of b is: {}.".format(b)

find_reg_vals()
