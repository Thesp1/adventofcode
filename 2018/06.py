with open('input_data/06.txt') as f:
    DATA = [x.strip() for x in f.readlines()]

chronal_points = [tuple([int(y) for y in x.split(', ')]) for x in DATA]

def manhattan_distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

# Parts 1 & 2
tally = [0 for x in range(len(chronal_points))]
infinite_outliers = [False for x in range(len(chronal_points))]
safe_region_points = 0

# Find point data for stuff
for x in range(400):
    if x % 25 == 0:
        print "x is: {}".format(x)
    for y in range(400):
        # Do stuff
        this_point = (x, y)
        mds = [manhattan_distance(this_point, cp) for cp in chronal_points]
        # Part 1
        min_md = min(mds)
        if mds.count(min_md) == 1:
            closest_point_index = mds.index(min_md)
            tally[closest_point_index] += 1
            if x == 0 or x == 399 or y == 0 or y == 399:
                infinite_outliers[closest_point_index] = True
        # Part 2
        if sum(mds) < 10000:
            safe_region_points += 1

# Now, eliminate outliers for Part 1.
possible_results = [x for x, y in zip(tally, infinite_outliers) if y is False]

print "Complete!"
print "Part 1:"
print max(possible_results)
print "Part 2:"
print safe_region_points
