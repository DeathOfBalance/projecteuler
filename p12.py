# def primes_below(n):
#     primes = []
#     for i in range(2, n + 1):
#         if p10.is_prime(i):
#             primes.append(i)
#     return primes
# 
# def primes_era(n):
#     A = [0,0]
#     for i in xrange(2, n + 1):
#         A.append(True)
#     for i in xrange(2, int(math.sqrt(n))):
#         if A[i]:
#             for j in [i**2 + k*i for k in xrange(n + 1) if i**2 + k*i <= n]:
#                 A[j] = False
#     primes = [i for i in xrange(2, n + 1) if A[i]]
#     return primes

# prime_list = primes_below(1000000)
# prime_list = primes_era(2000000)

def factors(n):
    factors = []
    for i in range(1, n + 1):
    # for i in prime_list:
        if not n % i:
            factors.append(i)
    return factors
# print factors(28)

def triangle(n):
    return int(n*(n + 1)/2)
# print triangle(6)

def factors_triangle(n):
    if not n % 2:
        fact_1 = factors(int(n/2))
        fact_2 = factors(n + 1)
    else:
        fact_1 = factors(n)
        fact_2 = factors(int((n + 1)/2))
    fact = [x*y for x in fact_1 for y in fact_2]
    return set(fact)


# def factors_recur(n):
#     factors = set()
#     if n == 1:
#         return {1}
#     for i in xrange(2, n + 1):
#         if not n % i:
#             factors = factors.union({i})
#             factors = factors.union(factors_recur(int(n/i)))
#     return factors

# print factors(1000000)
# print factors_recur(1000000)


n = 1
fac = factors_triangle(n)
while len(fac) <= 501:
    n += 1
    fac = factors_triangle(n)
    print n, len(fac)
    if len(fac) > 500:
        print triangle(n), fac
        break
