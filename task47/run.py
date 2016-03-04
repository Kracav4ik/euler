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

if not os.path.exists('primes_10M.py'):
    generated = generate_primes(10**7)
    with open('primes_10M.py', 'w') as f:
        f.write('primes_list = %s\n' % generated)
else:
    print 'no need to calculate ever again :D'
from primes_10M import primes_list
print len(primes_list), 'primes found'


def checker(n):
    l = []
    while 1:
        for f in primes_list:
            if f > n:
                break
            if n % f == 0:
                n //= f
                if not f in l:
                    l.append(f)
            if n == 1:
                return len(l)

m = 1
while 1:
    m += 1
    if checker(m) == checker(m + 1) == checker(m + 2) == checker(m + 3) == 4:
        print "numbers", m , ',', m + 1, ',', m + 2, ',', m + 3
        print "Skoodish", checker(m)
        break


