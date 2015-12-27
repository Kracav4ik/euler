# encoding: utf-8

from __future__ import division
from math import sqrt

MAX_NUMBER = 28124


def is_abundant(n):
    result = 1
    upper = int(sqrt(n))
    if upper * upper == n:
        result += upper
    else:
        upper += 1
    for r in range(2, upper):
        if n % r == 0:
            result += r
            result += n//r
            if result > y:
                return True
    return False

abundant_numbers = []

print 'counting abundant numbers...'
for y in range(MAX_NUMBER):
    if is_abundant(y):
        abundant_numbers.append(y)
print 'done! found', len(abundant_numbers), 'numbers o_O'

abundant_set = set(abundant_numbers)


def can_be_sum(n):
    for x in abundant_numbers:
        if n < 2 * x:
            break
        if n - x in abundant_set:
            return True
    return False

result = 0

print 'counting sums...'
for x in range(MAX_NUMBER):
    if x % 10 == 0:
        print '  %.4f%%...\r' % (100 * x / MAX_NUMBER),
    if not can_be_sum(x):
        result += x
print '\ndone!'
print result
