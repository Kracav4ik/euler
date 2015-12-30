# encoding: utf-8

from __future__ import division


def rot(s):
    if not s:
        return s
    return s[1:] + s[0]


def generate_primes(limit):
    primes = [2]
    for p in range(2, limit):
        is_prime = True
        for divisor in primes:
            if p < divisor * divisor:
                break
            if p % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(p)
    return primes

print 'calculating primes...'
primes_list = generate_primes(10**6)
primes_set = set(primes_list)
print '  done!'


def is_circular(p):
    str_p = str(p)
    for _ in range(len(str_p) - 1):
        str_p = rot(str_p)
        if int(str_p) not in primes_set:
            return False
    return True

circular_numbers = []
for x in primes_set:
    if is_circular(x):
        circular_numbers.append(x)
print len(circular_numbers), '|', circular_numbers
