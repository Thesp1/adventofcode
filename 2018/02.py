from collections import Counter

with open('input_data/02.txt') as f:
    boxes = [x.strip() for x in f.readlines()]

# Part 1
counters = [Counter(x) for x in boxes]
twos = [x.values().count(2) for x in counters]
threes = [x.values().count(3) for x in counters]
fours = [x.values().count(4) for x in counters]
print [x for x in fours if x]
print "Part 1:"
print len([x for x in twos if x]) * len([x for x in threes if x])


# Part 2
def compare_boxes(a, b):
    diffs = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diffs += 1
    return diffs

for box_a in boxes:
    for box_b in boxes:
        if compare_boxes(box_a, box_b) == 1:
            print box_a
            print box_b
            raise Exception("Done!")
