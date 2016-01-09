# encoding: utf-8

from __future__ import division
import os.path


def is_pandigital(s):
    if '0' in s or len(s) != len(set(s)):
        return False
    m = 1
    while m <= len(s):
        if str(m) in s:
            m += 1
            continue
        return False
    return True


def generate_primes(limit):
    print 'calculating primes below %s...' % limit
    primes = [2]
    for p in range(3, limit, 2):
        is_prime = True
        for divisor in primes:
            if p < divisor * divisor:
                break
            if p % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(p)
    print '  done!'
    return primes

m = []
if not os.path.exists('primes_10M.py'):
    generated = generate_primes(10**7)
    with open('primes_10M.py', 'w') as f:
        f.write('primes_list = %s\n' % generated)
else:
    print 'no need to calculate ever again :D'
from primes_10M import primes_list
print len(primes_list), 'primes found'

for x in primes_list[::-1]:
    if is_pandigital(str(x)):
        print x

