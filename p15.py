import itertools

size = 20

# binary_lists = itertools.product(range(2), repeat = 2*size)

# lattice_paths = {lists for lists in binary_lists if sum(lists) == size}
# print len(lattice_paths)

def lattice_paths(size):
    for positions in itertools.combinations(range(2*size), size):
        liste = [0]*(2*size)
        for pos in positions:
            liste[pos] = 1
        print liste
        yield liste

# print sum(1 for x in lattice_paths(20))
