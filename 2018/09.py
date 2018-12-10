from collections import defaultdict, deque

elf_scores = defaultdict(int)

num_players = 404
# last_marble_value = 71852
last_marble_value = 7185200
marble_circle = deque([0])

for marble_value in xrange(1, last_marble_value + 1):
    if marble_value % 23 == 0:
        player_num = marble_value % num_players
        elf_scores[player_num] += marble_value
        marble_circle.rotate(7)
        grabbed_marble = marble_circle.popleft()
        elf_scores[player_num] += grabbed_marble
        # print "Got {}!".format(grabbed_marble)
    else:
        marble_circle.rotate(-2)
        marble_circle.appendleft(marble_value)
    # print marble_circle

print "Complete!"
print max(elf_scores.values())

