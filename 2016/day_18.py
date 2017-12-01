data = ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"
# data = '..^^.'
# data = '.^^.^.^^^^'
row = [False if x == '.' else True for x in data]
rows = [row]


def is_trap(left, center, right):
    if left and center and not right:
        return True
    if center and right and not left:
        return True
    if left and not center and not right:
        return True
    if right and not center and not left:
        return True
    return False


# for row_number in range(39):
for row_number in range(399999):
    temp_row = [False] + rows[row_number] + [False]
    new_row = [is_trap(temp_row[x-1], temp_row[x], temp_row[x+1]) for x in range(1, len(data)+1)]
    rows.append(new_row)

pretty_data = '\n'.join([''.join(['^' if x else '.' for x in row]) for row in rows])
# print pretty_data
print "Total safe squares:"
print pretty_data.count('.')
