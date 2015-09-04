pairs = {(a,b) for a in xrange(1000) for b in xrange(1000) if a < b}

def test_pairs():
    for (a,b) in pairs:
        if 1000**2 - 2000*(a+b) + 2*a*b == 0:
            print (a,b), (1000 - a - b)*a*b

test_pairs()