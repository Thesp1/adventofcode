with open('input_data/08.txt') as f:
    DATA = f.read().strip()

import re
PATTERN = re.compile(r'(?P<affected_register>\w+) (?P<inc_or_dec>(inc|dec)) (?P<amount>\-?\d+) if (?P<conditional_register>\w+) (?P<operator>[><=!]+) (?P<conditional_amount>\-?\d+)')

def parse_line(line):
    match = PATTERN.search(line)
    if not match:
        raise Exception("Parser didn't parse correctly this instruction: {0}".format(line))
    affected_register = match.group('affected_register')
    multiplier = 1 if match.group('inc_or_dec') == 'inc' else -1
    amount = int(match.group('amount'))
    adjustment = multiplier * amount
    conditional_register = match.group('conditional_register')
    operator = match.group('operator')
    conditional_amount = int(match.group('conditional_amount'))
    return affected_register, adjustment, conditional_register, operator, conditional_amount


# Stars 1 & 2
from collections import defaultdict
registers = defaultdict(int)
instructions = [parse_line(line) for line in DATA.split('\n')]
max_held = 0
for affected_register, adjustment, conditional_register, operator, conditional_amount in instructions:
    if operator == '<':
        if registers[conditional_register] < conditional_amount:
            registers[affected_register] += adjustment
    elif operator == '>':
        if registers[conditional_register] > conditional_amount:
            registers[affected_register] += adjustment
    elif operator == '<=':
        if registers[conditional_register] <= conditional_amount:
            registers[affected_register] += adjustment
    elif operator == '>=':
        if registers[conditional_register] >= conditional_amount:
            registers[affected_register] += adjustment
    elif operator == '==':
        if registers[conditional_register] == conditional_amount:
            registers[affected_register] += adjustment
    elif operator == '!=':
        if registers[conditional_register] != conditional_amount:
            registers[affected_register] += adjustment
    else:
        raise Exception('Unknown operator found: {0}'.format(operator))
    max_held = max([max_held, max(registers.values())])
print "Answer 1:"
print max(registers.values())
print "Answer 2:"
print max_held
