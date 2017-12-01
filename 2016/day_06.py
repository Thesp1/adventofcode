from collections import Counter

with open('input_06.txt') as f:
    data = f.read().strip()

codes = data.split('\n')
message_list = []
for _ in range(len(codes[0])):
    message_list.append([])
for code in codes:
    for slot, letter in enumerate(code):
        message_list[slot].append(letter)

message_counters = [Counter(x) for x in message_list]
# Part 1
# common_list = [x.most_common(1)[0][0] for x in message_counters]
# Part 2
common_list = [x.most_common()[-1][0] for x in message_counters]

print "Secret message:"
print ''.join(common_list)
