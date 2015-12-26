# encoding: utf-8

from __future__ import division


def d(n):
    summ = 0
    for x in range(1, n):
        if n % x == 0:
            summ += x
    return summ

result = []
for x in range(10001):
    if x == d(d(x)) and x != d(x):
        result.append(x)
print sum(result)
