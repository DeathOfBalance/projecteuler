pairs = {(a,b) for a in xrange(1,101) for b in xrange(1,101) if a < b}

def sum(pairs):
    the_sum = 0
    for (a,b) in pairs:
        the_sum += a*b
    return the_sum

print 2*sum(pairs)
