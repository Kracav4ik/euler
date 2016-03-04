# encoding: utf-8

from __future__ import division
import os.path



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

primes_set = set(primes_list)

p = 9
while 1:
    found_bad = False
    if p not in primes_set:
        for r in range(1, 1000):
            k = p - 2 * r * r
            if k < 0:
                break
            if k in primes_set:
                print p, '=', k, '+ 2 *', r, '*', r
                found_bad = True
                break
        if not found_bad:
            print 'answer', p
            exit()

    p += 2
