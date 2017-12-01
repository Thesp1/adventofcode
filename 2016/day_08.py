with open('input_08.txt') as f:
    data = f.read().strip()

instructions = data.split('\n')




class LCD():
    def __init__(self, x=50, y=6):
        # This construction allows lcd[x][y] formatting.
        self.lcd = [[False for a in range(y)] for b in range(x)]
        self.width = x
        self.height = y

    def rect(self, a, b):
        for x in range(a):
            for y in range(b):
                self.lcd[x][y] = True
        print "Drew a rectangle of {0} by {1}.".format(a, b)

    def rotate_column(self, x, dist):
        old_vals = [self.lcd[x][y] for y in range(self.height)]
        new_vals = old_vals[-dist:] + old_vals[:-dist]
        print "rc New vals:"
        print new_vals
        for y, val in enumerate(new_vals):
            self.lcd[x][y] = val
        print "Rotated column {0} by {1}.".format(x, dist)

    def rotate_row(self, y, dist):
        old_vals = [self.lcd[x][y] for x in range(self.width)]
        new_vals = old_vals[-dist:] + old_vals[:-dist]
        print "rr New vals:"
        print new_vals
        for x, val in enumerate(new_vals):
            self.lcd[x][y] = val
        print "Rotated row {0} by {1}.".format(y, dist)

    def parse_instruction(self, instruction):
        if instruction[:5] == 'rect ':
            vals = instruction[5:]
            x, y = (int(n) for n in vals.split('x'))
            self.rect(x, y)
        elif instruction[:16] == 'rotate column x=':
            vals = instruction[16:]
            x, dist = (int(n) for n in vals.split(' by '))
            self.rotate_column(x, dist)
        elif instruction[:13] == 'rotate row y=':
            vals = instruction[13:]
            y, dist = (int(n) for n in vals.split(' by '))
            self.rotate_row(y, dist)
        else:
            raise Exception("Couldn't parse instruction: {0}".format(instruction))
        print "New LCD readout:"
        print self.lcd

lcd = LCD()
for instruction in instructions:
    lcd.parse_instruction(instruction)

total = sum([len([a for a in b if a]) for b in lcd.lcd])
print "Complete! Total on: {0}".format(total)
print lcd.lcd

