with open('input_data/04.txt') as f:
    data = f.read().strip()

# Star 1
lines = data.split('\n')
valid_passphrases = 0
for line in lines:
    phrases = line.split()
    if len(phrases) == len(set(phrases)):
        valid_passphrases += 1
print "Answer 1:"
print valid_passphrases

# Star 2
valid_passphrases = 0
for line in lines:
    phrases = [''.join(sorted(phrase)) for phrase in line.split()]
    if len(phrases) == len(set(phrases)):
        valid_passphrases += 1
print "Answer 2:"
print valid_passphrases
