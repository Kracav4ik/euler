from math import sqrt


def factors(x):
    """Return count of factors of x"""
    divisors = []
    x2 = sqrt(x)
    for y in range(1, int(x2) + 1):
        if x % y == 0:
            divisors.append(y)
    return 2 * len(divisors)
n = 1
while True:
    t = (n*n + n)/2
    factors_count = factors(t)
    if factors_count > 500:
        print t
        break
    n += 1
