import math

def is_prime(candidate):
    bound = int(math.sqrt(candidate))
    for i in [j for j in xrange(2, bound + 1) if j == 2 or j % 2 != 0]:
        if not candidate % i:
            return False
    return True

#primes = [n for n in xrange(2,2000000) if is_prime(n)]

#def sum(list):
#    sum = 0
#    while len(list) > 0:
#        sum += list.pop()
#    return sum

def sum_to_limit(limit):
    the_sum = 2
    n = 3
    while n <= limit:
        if is_prime(n):
            the_sum += n
        n += 2
    return the_sum

#print sum(primes)
#print sum_to_limit(2000000)
