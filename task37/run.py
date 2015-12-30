# encoding: utf-8

from __future__ import division


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


def is_truncatable(n):
    s = str(n)
    if len(s) < 2:
        return False
    for _ in range(len(s) - 1):
        s = s[:-1]
        if int(s) not in primes_set:
            return False
    s = str(n)
    for _ in range(len(s) - 1):
        s = s[1:]
        if int(s) not in primes_set:
            return False
    return True

result = 0

for x in primes_list:
    if is_truncatable(x):
        result += x
print result
