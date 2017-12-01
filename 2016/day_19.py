from time import sleep

# raise Exception

CIRCLE_LENGTH = 3014603

gift_circle = list(enumerate([1 for x in range(CIRCLE_LENGTH)], start=1))

# marker = 0
# counter = 0
# while len(gift_circle) > 1:
#     if marker > len(gift_circle) - 1:
#         marker = 0
#         counter += 1
#         print "Made it through the whole loop! Times: {}".format(counter)
#     getting_elf = gift_circle[marker]
#     if marker + 1 == len(gift_circle):
#         giving_elf_index = 0
#     else:
#         giving_elf_index = marker + 1
#     giving_elf = gift_circle[giving_elf_index]
#     getting_elf = (getting_elf[0], getting_elf[1] + giving_elf[1])
#     gift_circle[marker] = getting_elf
#     gift_circle.pop(giving_elf_index)
#     if len(gift_circle) % 100000 == 0:
#         print "Length of gift_circle now: {0}".format(len(gift_circle))
#     marker += 1


# print gift_circle

marker = 0
counter = 0
gift_circle_length = len(gift_circle)
while gift_circle_length > 1:
    half = gift_circle_length / 2
    if marker > gift_circle_length - 1:
        marker = 0
        counter += 1
        print "Made it through the whole loop! Times: {}".format(counter)
    getting_elf = gift_circle[marker]
    if marker + half >= gift_circle_length:
        giving_elf_index = marker + half - gift_circle_length
    else:
        giving_elf_index = marker + half
    giving_elf = gift_circle[giving_elf_index]
    getting_elf = (getting_elf[0], getting_elf[1] + giving_elf[1])
    gift_circle[marker] = getting_elf
    gift_circle.pop(giving_elf_index)
    gift_circle_length = len(gift_circle)
    if gift_circle_length % 10000 == 0:
        print "Length of gift_circle now: {0}".format(gift_circle_length)
    # Add conditional here
    if giving_elf_index > marker:
        marker += 1


print gift_circle
