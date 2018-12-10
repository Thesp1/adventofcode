import re
import string

with open('input_data/05.txt') as f:
    DATA = f.read().strip()

pattern_list = []
for c in string.ascii_lowercase:
    pattern_list.append(c + c.upper())
    pattern_list.append(c.upper() + c)

# Part 1
current_string = DATA
PATTERN = re.compile('|'.join(pattern_list))

while True:
    new_string = PATTERN.sub('', current_string)
    if current_string == new_string:
        break
    current_string = new_string

print "Complete!"
print new_string
print len(new_string)


# Part 2
main_string = DATA
results = []
for c in string.ascii_lowercase:
    lettered_string = main_string.replace(c, '').replace(c.upper(), '')
    print "Removing {} and {}...".format(c, c.upper())
    while True:
        new_string = PATTERN.sub('', lettered_string)
        if lettered_string == new_string:
            print "Got {}.".format(len(lettered_string))
            results.append(len(lettered_string))
            break
        lettered_string = new_string

print "Complete!"
print min(results)
