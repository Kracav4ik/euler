# encoding: utf-8

from __future__ import division


def perm(s):
    result = []
    if len(s) == 1:
        return [s]
    for x in range(len(s)):
        for p in perm(s[:x] + s[x + 1:]):
            new_s = s[x] + p
            result.append(new_s)
    return result


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

primes_list = generate_primes(10000)
det = 0
l = []
i = o = -1
for x in range(1000, 10000):
# for x in range(1487, 1488):
    for y in perm(str(x)):
        if not y.startswith('0') and int(y) in primes_list:
            det += 1
            l.append(int(y))
    if det >= 3:
        for k in l:
            i += 1
            for n in (l[:i] + l[i + 1:]):
                o += 1
                for m in (l[:o] + l[o + 1:]):
                    if k != n != m and k - n == n - m:
                        print k, n, m
    det = 0
    l = []
