# encoding: utf-8

from __future__ import division


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

s = 0
max_seq = 0
for i, p in enumerate(primes_list):
    s += p
    if s > limit:
        print 'limit', i
        max_seq = i
        break

seq_sums = primes_list[:]
max_result = []
max_l = 0
for seq_l in range(2, max_seq):
    result = []

    for x in range(len(primes_list) + 1 - seq_l):
        seq_sums[x] += primes_list[x+seq_l-1]
        if seq_sums[x] in primes_set:
            result.append([seq_sums[x], primes_list[x:x+seq_l]])

    if result:
        max_result = result
        max_l = seq_l

print max_l, max_result
