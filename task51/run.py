# encoding: utf-8

from __future__ import division
from itertools import combinations


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

limit = 10 ** 6
primes_list = generate_primes(limit)
primes_set = set(primes_list)
print len(primes_list), 'generated'


def counts(s):
    m = {}
    for i, c in enumerate(s):
        m.setdefault(c, []).append(i)
    result = {}
    for k, v in m.items():
        if len(v) > 1:
            result[k] = v
    return result


def f(s):
    result = []
    c_map = counts(s)
    for digit, pos_list in c_map.items():
        for star_count in range(2, len(pos_list) + 1):
            if star_count == len(s):
                break
            for index_list in combinations(pos_list, star_count):
                result.append(''.join(c if i not in index_list else '*' for i, c in enumerate(s)))
    return result


m = {}

for v in primes_list:
    if v < 10:
        continue
    for k in f(str(v)):
        m.setdefault(k, []).append(v)

max_v = 0
n = 0

for k, v in m.items():
    if max_v < len(v):
        max_v = len(v)
        n = k
print max_v

for k, v in m.items():
    if max_v == len(v):
        print k, v



