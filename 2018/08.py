with open('input_data/08.txt') as f:
    DATA = [int(x) for x in f.read().strip().split(' ')]


class Node:
    def __init__(self, line_input):
        self.line_input = line_input
        self.num_children = line_input[0]
        self.num_metadata = line_input[1]
        self.children = []
        self.remaining_data = line_input[2:]
        for child_number in range(self.num_children):
            # do something
            new_node = Node(self.remaining_data)
            self.remaining_data = new_node.remaining_data
            self.children.append(new_node)
        self.metadata = self.remaining_data[0:self.num_metadata]
        self.remaining_data = self.remaining_data[self.num_metadata:]

    def metadata_sum(self):
        return sum(self.metadata) + sum([x.metadata_sum() for x in self.children])

    def value(self):
        if not self.children:
            return self.metadata_sum()
        v = 0
        for entry in self.metadata:
            if entry == 0 or entry > self.num_children:
                continue
            v += self.children[entry-1].value()
        return v

    def __repr__(self):
        return u'<Node {} children, {} metadata>'.format(self.num_children, self.num_metadata)


all_nodes = []
line_data = DATA
while line_data:
    print "Length of remaining data: {}".format(len(line_data))
    new_node = Node(line_data)
    line_data = new_node.remaining_data
    all_nodes.append(new_node)

print "Nodes complete!"
print "Part 1:"
print sum([x.metadata_sum() for x in all_nodes])
print "Part 2:"
print sum([x.value() for x in all_nodes])
