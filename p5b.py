temp = []
def find_factors(n, primes):
    if n == 1:
        global temp
        print "Now n == 1. Current temp = ", temp
        primes += temp
        temp = []
        return primes
    for i in range(2, n+1):
        print "** For loop, n = %i and i = %i" % (n,i)
        if not n % i:
            if i in primes:
                primes.remove(i)
            temp.append(i)
            print "temp = ", temp
            return(find_factors(int(n / i), primes))

#print find_factors(9,[2,2,2,3,5,7])

def factors(n):
    if n == 2:
        return [2]
    else:
        return find_factors(n, factors(n - 1))

print factors(10)

def product(n):
    list = factors(n)
    product = 1
    while len(list) > 0:
        product *= list.pop()
    return product

print product(20)