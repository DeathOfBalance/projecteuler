temp = []

def find_factors(n, primes):
#    to_add = []
    if n == 1:
        primes += temp
        temp = []
        return primes_final
    for i in range(2,n+1):
        print "**Currently at %i in (%i,%s)**" % (i,n,primes)
        if not (n % i):
            if i in primes:
                primes.remove(i)
                print "Removing", i
                temp.append(i)
                print "Appending", i, ", current to add = ", to_add
            return(find_factors(int(n/i),primes))
#            if n == i:
#                to_add.append(n)
#                print "Appending maximal", n, ", current to add = ", to_add
#            else:
#                to_add += find_factors(int(n / i), primes)
#                print "Finding smaller factors, to add = ", to_add
#            break
#    primes += to_add
#    print "The factors for %i are %s" % (n,primes)
#    return primes

#print find_factors(2,[3])
#print find_factors(2,[])
#print find_factors(3,[2])
#print find_factors(4,[2,3])
#
#print find_factors(4,find_factors(3,find_factors(2,[])))

def find_all_factors(n):
    if n == 2:
        return find_factors(2,[])
    else:
        return find_factors(n,find_all_factors(n - 1))

def smallest_multiple(n):
    product = 1
    factors = find_all_factors(n)
    while len(factors) > 0:
        product *= factors.pop()
    return product

print find_all_factors(6)
#print smallest_multiple(6)
#print smallest_multiple(20)
