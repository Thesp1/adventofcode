with open('input_03.txt') as f:
    data = f.read().strip()

# Day 1
# triangles = [sorted(map(int, x.split())) for x in data.split('\n')]
# print len([x for x in triangles if x[0] + x[1] > x[2]])

# Day 2
base_triangles = [map(int, x.split()) for x in data.split('\n')]
tri1, tri2, tri3, triangles = [], [], [], []
for triangle in base_triangles:
    tri1.append(triangle[0])
    tri2.append(triangle[1])
    tri3.append(triangle[2])
    if len(tri1) == 3:
        triangles += [tri1, tri2, tri3]
        tri1, tri2, tri3 = [], [], []
triangles = [sorted(x) for x in triangles]
print len([x for x in triangles if x[0] + x[1] > x[2]])
