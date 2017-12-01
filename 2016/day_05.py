from hashlib import md5

DATA = 'wtnhxymk'

door_id = DATA
password = [None, None, None, None, None, None, None, None]
index = 0
while True:
    hash_this = door_id + str(index)
    hd = md5(hash_this).hexdigest()
    if hd[:5] == '00000':
        print "Success with {0}: {1}".format(hash_this, hd)
        # Part 1
        # print "Appending {0}...".format(hd[5])
        # password.append(hd[5])
        # Part 2
        if hd[5] in '01234567':
            pos = int(hd[5])
            val = hd[6]
            if password[pos] is None:
                password[pos] = val
                print "Added {0} in slot {1}.".format(val, pos)
                print "Current password is: {0}".format(''.join('_' if not x else x for x in password))
            else:
                print "Discarding, already have value..."
        else:
            print "Not a valid position, continuing..."
        if None not in password:
            break
    index += 1

print "Final password is:"
print ''.join(password)
