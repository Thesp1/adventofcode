with open('input_data/09.txt') as f:
    DATA = f.read().strip()

import re
GARBAGE_PATTERN = re.compile(r'<(?P<caught>([^>!]|!.)*)>')


# Star 1
cleaned_data = GARBAGE_PATTERN.sub('', DATA)
total_left_braces = 0
score = 0
for letter in cleaned_data:
    if letter == '{':
        # print '{'
        # print score
        total_left_braces += 1
        score += total_left_braces
    if letter == '}':
        # print '}'
        total_left_braces -= 1


print "Answer 1:"
print score

# Star 2
ESCAPED_PATTERN = re.compile(r'!.')
matches = GARBAGE_PATTERN.findall(DATA)
score = 0
# print matches
for match in matches:
    caught = match[0]
    # print caught
    remainder = ESCAPED_PATTERN.sub('', caught)
    score += len(remainder)
print "Answer 2:"
print score
