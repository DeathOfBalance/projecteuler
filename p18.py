import numpy as np

class Triangle(object):

    def __init__(self, source = '', content = []):
        if source == '':
            self.content = content
        else:
            lines_string = [line.rstrip('\r\n') for line in open(source)]
            self.content = map(lambda x: map(int, x), map(str.split,
                lines_string))

    def left_triangle(self):
        content = map(lambda x: x[:(len(x) - 1)], self.content)[1:]
        return Triangle('',content)

    def right_triangle(self):
        content = map(lambda x: x[1:len(x)], self.content)[1:]
        return Triangle('',content)

    def total(self):
        return sum(map(sum, self.content))

    def weighted_total(self, weight): # weight = 1.0, .., 2.0, ...
        return sum(map(sum, [map(lambda x: x/(weight ** self.content.index(i)), i)
            for i in self.content]))

    def average(self):
        return sum(map(sum, self.content)) / self.size()

    def size(self):
        return int(len(self.content)*(len(self.content) + 1)/2)

    def apex(self):
        return self.content[0][0]

class Tree(object):

    def __init__(self, base_nodes = [], source = ''):
        if source == '':
            self.base_nodes = base_nodes
        else:
            self.base_nodes = read_nodes(source)
        # size = self.size()

    def l_tree(self, position):
        node = self.base_nodes[position]
        if node.l_node == None:
            return Tree()
        else:
            return Tree([node.l_node])

    def r_tree(self, position):
        node = self.base_nodes[position]
        if node.r_node == None:
            return Tree()
        else:
            return Tree([node.r_node])

#     def size(self):
#         size = 0
#         l_node = 

class Node(object):

    def __init__(self, content = 0, l_node = None, r_node = None):
        self.content = content
        self.l_node = l_node
        self.r_node = r_node

    def set_l_node(self, node):
        self.l_node = node

    def set_r_node(self, node):
        self.r_node = node

def read_nodes(source):
    triangle = map(lambda x: map(int, x), map(str.split, [line.rstrip('\r\n')
        for line in open(source)]))
    for i in range(len(triangle)):
        nodes_this_line = []
        for j in range(len(triangle[i])):
            l_node = None
            r_node = None
            if not i < 1:
                if not j < 1:
                    l_node = triangle[i - 1][j - 1]
                if not j > len(triangle[i - 1]) - 1:
                    r_node = triangle[i - 1][j]
            nodes_this_line.append(Node(triangle[i][j], l_node, r_node))
        # if i != 0:
        for k in range(len(triangle[i])):
            if k == 0:
                nodes_this_line[k].set_l_node(None)
                if i != 0:
                    nodes_this_line[k].set_r_node(nodes_past_line[k])
            elif k == len(triangle[i]) - 1:
                if i != 0:
                    nodes_this_line[k].set_l_node(nodes_past_line[k - 1])
                nodes_this_line[k].set_r_node(None)
            else:
                nodes_this_line[k].set_l_node(nodes_past_line[k - 1])
                nodes_this_line[k].set_r_node(nodes_past_line[k])
        if i == len(triangle) - 1:
            return nodes_this_line
        nodes_past_line = nodes_this_line

class InvertedTriangle(object):

    def __init__(self, source = '', content = []):
        if source == '':
            self.content = content
        else:
            lines_string = [line.rstrip('\r\n') for line in open(source)]
            self.content = map(lambda x: map(int, x), map(str.split,
                lines_string))

    def left_triangle(self, position):
        content = self.content[:len(self.content) - 1]
        # for i in range(len(content)):
        content = [content[len(content) - 1 - i][max(0, position - 1 -
            i):min(position, len(content[len(content) - 1 - i]))] for i in
            range(len(content))][::-1]
        return InvertedTriangle('',content)

    def right_triangle(self, position):
        content = self.content[:len(self.content) - 1]
        # for i in range(len(content)):
        content = [content[len(content) - 1 - i][max(0, position + 1 -
            2*i):min(position + 2, len(content[len(content) - 1 - i]))] for i in
            range(len(content))][::-1]
        return InvertedTriangle('',content)

    def total(self):
        return sum(map(sum, self.content))

    def weighted_total(self, weight): # weight = 1.0, .., 2.0, ...
        return sum(map(sum, [map(lambda x: x/(weight ** self.content.index(i)), i)
            for i in self.content]))

    def average(self):
        return sum(map(sum, self.content)) / self.size()

    def size(self):
        return int(len(self.content)*(len(self.content) + 1)/2)

    def apex(self):
        if len(self.content[len(self.content) - 1]) != 1:
            print "Apex ill-defined"
        else:
            return self.content[len(self.content) - 1][0]

t = Tree([],"t18.txt")
# t1 = t.left_triangle()
# t2 = t.right_triangle()

def maximal_path(triangle, weight):
    while True:
        yield triangle.apex()
        if triangle.size() == 1:
            return
        left = triangle.left_triangle()
        right = triangle.right_triangle()
        left_t = left.weighted_total(weight)
        right_t = right.weighted_total(weight)
        if left_t < right_t:
            # print "Left < right:", left_t, right_t, triangle.apex()
            triangle = right
        elif left_t > right_t:
            # print "Left > right:", left_t, right_t, triangle.apex()
            triangle = left
        else:
            print "We fucked up son."
            return

def test_paths(triangle, weight_range):
    results = []
    gens = []
    for weight in weight_range:
        gens.append([maximal_path(triangle, weight), weight])
    for gen in gens:
        sequence = [_ for _ in gen[0]]
        # print sequence, gen[1], sum(sequence)
        results.append((gen[1], sum(sequence)))
    print results

s = Triangle("t67.txt")
