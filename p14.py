def collatz_length(n, l):
    if n == 1:
        return l
    else:
        if n % 2 == 0:
            return collatz_length(int(n / 2), l + 1)
        else:
            return collatz_length(3*n + 1, l + 1)

def longest(n = 1000000):
    max_length = 0
    max_i = 0
    for i in range(1,n):
        length = collatz_length(i, 1)
        if length > max_length:
            max_i = i
            max_length = length
    return (max_i, max_length)
