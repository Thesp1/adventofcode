with open('input_data/06.txt') as f:
    DATA = f.read().strip()

# Star 1
memory_banks = [int(x) for x in DATA.split()]
print "start data"
print memory_banks
seen_banks = set()
cycles = 0
while tuple(memory_banks) not in seen_banks:
    cycles += 1
    seen_banks.add(tuple(memory_banks[:]))
    max_mem = max(memory_banks)
    take_from_index = memory_banks.index(max_mem)
    memory_banks[take_from_index] = 0
    for i in range(take_from_index+1, take_from_index+max_mem+1):
        memory_banks[i%16] += 1
    # print "Cycle {0}: {1}".format(cycles, memory_banks)
print "Answer 1:"
print cycles

# Star 2
memory_banks = [int(x) for x in DATA.split()]
print "start data"
print memory_banks
seen_banks = []
cycles = 0
while memory_banks not in seen_banks:
    cycles += 1
    seen_banks.append(memory_banks[:])
    max_mem = max(memory_banks)
    take_from_index = memory_banks.index(max_mem)
    memory_banks[take_from_index] = 0
    for i in range(take_from_index+1, take_from_index+max_mem+1):
        memory_banks[i%16] += 1
    # print "Cycle {0}: {1}".format(cycles, memory_banks)
print "Answer 2:"
print cycles - seen_banks.index(memory_banks)
