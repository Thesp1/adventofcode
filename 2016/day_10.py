import re

with open('input_10.txt') as f:
    data = f.read().strip()

instructions = data.split('\n')

INSTRUCTION_PATTERN = re.compile(r'^bot (?P<bot_number>\d+) gives low to (?P<low_type>\w+) (?P<low_number>\d+) and high to (?P<high_type>\w+) (?P<high_number>\d+)$')
SETUP_PATTERN = re.compile(r'^value (?P<val>\d+) goes to bot (?P<target_bot>\d+)$')

setup_instructions = [x for x in instructions if x[0] == 'v']
bot_instructions = [x for x in instructions if x[0] == 'b']

class Bot:
    def __init__(self, instruction):
        match = INSTRUCTION_PATTERN.search(instruction)
        if not match:
            raise Exception('Failed to match for instruction: {0}'.format(instruction))
        d = match.groupdict()
        self.bot_number = int(d['bot_number'])
        self.low_type = d['low_type']
        self.low_number = int(d['low_number'])
        self.high_type = d['high_type']
        self.high_number = int(d['high_number'])
        self.slots = []

    def set_low_bucket(self, recipient):
        self.low_bucket = recipient

    def set_high_bucket(self, recipient):
        self.high_bucket = recipient

    def process_slots(self):
        if len(self.slots) < 2:
            return False
        if len(self.slots) > 2:
            raise Exception('Too many slots for this bot: {0}'.format(self))
        low_val, high_val = sorted(self.slots)
        # Part 1
        # if low_val == 17 and high_val == 61:
        #     raise Exception("Found the answer! It's this bot: {0}".format(self))
        # if self.low_type == 'bot' and self.low_bucket.slots == 2:
        #     self.low_bucket.process_slots()
        self.low_bucket.slots.append(low_val)
        # if self.high_type == 'bot' and self.high_bucket.slots == 2:
        #     self.high_bucket.process_slots()
        self.high_bucket.slots.append(high_val)
        self.slots = []
        print "# {0} gave {1} to {2} and {3} to {4}.".format(self.bot_number, low_val, self.low_bucket, high_val, self.high_bucket)
        return True

    def __repr__(self):
        return u'<Bot {0}: {1} {2}/{3} {4} | Slots: {5}>'.format(self.bot_number, self.low_type, self.low_number,
                                                                 self.high_type, self.high_number, self.slots)

class OutputBin:
    def __init__(self, number):
        self.number = number
        self.slots = []

    @property
    def label(self):
        return "Bin {0}".format(self.number)

    def __repr__(self):
        return u'<Bin {0} | Slots: {1}>'.format(self.number, self.slots)


thing_map = {}

print "Setting up bots..."
# Set up bots
for instruction in bot_instructions:
    bot = Bot(instruction)
    thing_map['bot {0}'.format(bot.bot_number)] = bot

print "Giving values to bots..."
# Then, give values to bots
for instruction in setup_instructions:
    match = SETUP_PATTERN.search(instruction)
    d = match.groupdict()
    val = int(d['val'])
    target_bot_number = d['target_bot']
    thing_map['bot {0}'.format(target_bot_number)].slots.append(val)


print "Linking bots..."
# Link them.
list_of_bots = thing_map.values()[:]
for bot in list_of_bots:
    low_bucket_label = '{0} {1}'.format(bot.low_type, bot.low_number)
    high_bucket_label = '{0} {1}'.format(bot.high_type, bot.high_number)
    try:
        bot.set_low_bucket(thing_map[low_bucket_label])
    except:
        print "Creating {0} {1}...".format(bot.low_type, bot.low_number)
        thing_map[low_bucket_label] = OutputBin(bot.low_number)
        bot.set_low_bucket(thing_map[low_bucket_label])
    try:
        bot.set_high_bucket(thing_map[high_bucket_label])
    except:
        print "Creating {0} {1}...".format(bot.high_type, bot.high_number)
        thing_map[high_bucket_label] = OutputBin(bot.high_number)
        bot.set_high_bucket(thing_map[high_bucket_label])

while True:
    found_one = False
    for bot in list_of_bots:
        res = bot.process_slots()
        found_one = res or found_one
    if not found_one:
        break

print "Final result:"
print thing_map['output 0']
print thing_map['output 1']
print thing_map['output 2']
