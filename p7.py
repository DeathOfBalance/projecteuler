import math

#def prime(n): (recursive... too slow)
#    if n == 1:
#        return 2
#    elif n == 2:
#        return 3
#    else:
#        previous_prime = prime(n - 1)
#        while not is_prime(previous_prime + 2):
#            previous_prime += 2
#        return previous_prime + 2

def is_prime(candidate):
    bound = int(math.sqrt(candidate))
    for i in [j for j in xrange(2, bound + 1) if j == 2 or j % 2 != 0]:
        if not candidate % i:
            return False
    return True

primes = [n for n in xrange(2,200000) if is_prime(n)]
print len(primes)
print primes[10000]