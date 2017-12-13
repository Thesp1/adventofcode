with open('input_data/13.txt') as f:
    DATA = f.read().strip()

def parse_line(line):
    return [int(x) for x in line.split(': ')]


# Star 1
firewall = [parse_line(x) for x in DATA.split('\n')]
severity = 0
for layer, depth in firewall:
    if layer % ((depth - 1) * 2) == 0:
        severity += layer * depth
print "Answer 1:"
print severity

# Star 2
delay = 0
while True:
    delay += 1
    caught = False
    for layer, depth in firewall:
        if (layer + delay) % ((depth - 1) * 2) == 0:
            caught = True
            break
    if not caught:
        print "Escaped!"
        break
print "Answer 2:"
print delay
