# from time import sleep

data = '11110010111001001'
# Part 1
# disk_length = 272
# Part 2
disk_length = 35651584

# Test data
# data = '10000'
# disk_length = 20


def reverse_ones(s):
    return ''.join(['1' if x == '0' else '0' for x in s])

def fill_more(s):
    # print '-----'
    # print s
    s2 = reverse_ones(s[::-1])
    # print s2
    return s + '0' + s2

def checksum(s):
    # print "Checksumming {0}...".format(s)
    c = ''
    for i in range(len(s))[::2]:
        # print i
        if s[i] == s[i+1]:
            c += '1'
        else:
            c += '0'
    return c



while len(data) < disk_length:
    data = fill_more(data)
    print "New data..."
    # print data
    # sleep(1)

data = data[:disk_length]

checksum_value = checksum(data)

while len(checksum_value) % 2 == 0:
    print "checksumming length of {}".format(len(checksum_value))
    checksum_value = checksum(checksum_value)
    # sleep(1)

print checksum_value
