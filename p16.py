N = 2 ** 1000
s = str(N)
l = len(s)

the_sum = 0
for i in range(l):
    the_sum += int(s[i])
print the_sum
