import re


with open('input_07.txt') as f:
    data = f.read().strip()

addresses = data.split('\n')

bracket_matcher = re.compile(r'\[\w*]')

# Part 1
def find_abba(s):
    while True:
        if len(s) < 4:
            return False
        if s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
            return True
        s = s[1:]

def fail_hypernet_check(s):
    "Return True if abba found in brackets."
    hypernets = []
    pos = 0
    while True:
        start_bracket = s.find('[', pos)
        if start_bracket == -1:
            break
        end_bracket = s.find(']', start_bracket)
        hypernets.append(s[start_bracket+1:end_bracket])
        pos = end_bracket
    for hypernet in hypernets:
        if find_abba(hypernet):
            return True
    return False


# Part 2
def find_abas(s):
    "Return all string ABA patterns."
    patterns = []
    while True:
        if len(s) < 3:
            return patterns
        if s[0] == s[2] and s[0] != s[1]:
            patterns.append(s[:3])
        s = s[1:]

def aba_hypernet_check(s):
    "Return ABA patterns found in brackets."
    hypernets = []
    pos = 0
    while True:
        start_bracket = s.find('[', pos)
        if start_bracket == -1:
            break
        end_bracket = s.find(']', start_bracket)
        hypernets.append(s[start_bracket+1:end_bracket])
        pos = end_bracket
    patterns = []
    for hypernet in hypernets:
        patterns += find_abas(hypernet)
    return patterns


counter = 0
for address in addresses:
    inner_patterns = aba_hypernet_check(address)
    ipf_set = set(['{0}{1}{0}'.format(x[1], x[0]) for x in inner_patterns])
    stripped_address = bracket_matcher.sub('[]', address)
    outer_patterns = find_abas(stripped_address)
    op_set = set(outer_patterns)
    intersection = ipf_set & op_set
    if intersection:
        counter += 1

print "Final tally:"
print counter
