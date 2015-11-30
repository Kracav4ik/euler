from math import sqrt


def is_prime(xx):
    """checks if the number is prime
    """
    x2 = sqrt(xx)
    for p in primes:
        if xx % p == 0:
            return False
        if p > x2:
            break
    return True

summ = 0
x = 2
primes = []
while True:
    if is_prime(x):
        primes.append(x)
        summ += x
    x += 1
    if x >= 2000000:
        break
print summ
