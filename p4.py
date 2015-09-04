import math
def digit_at_position(num, pos):
    return num/(10**(len(str(num)) - pos)) % 10

def is_palindromic(x):
    length = len(str(x))
    x_backward = ""
    for i in range(length, 0, -1):
        x_backward += str(digit_at_position(x, i))
    return int(x_backward) == x

products = {x*y for x in range(1000) for y in range(1000)}
palindromic_products = {x for x in products if is_palindromic(x)}
print max(palindromic_products)
