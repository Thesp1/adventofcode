with open('input_data/01.txt') as f:
    data = f.read().strip()

# Star 1
data_wrap = data + data[0]
answer_1 = sum(int(data[x]) for x in range(len(data)) if data[x] == data_wrap[x+1])
print answer_1

# Star 2
data_wrap = data + data
answer_2 = sum(int(data[x]) for x in range(len(data)) if data[x] == data_wrap[x+(len(data)/2)])
print answer_2
