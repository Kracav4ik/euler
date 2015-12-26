# encoding: utf-8

from __future__ import division


def fac(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result

n = str(fac(100))
m = 0
for x in n:
    m += int(x)
print m
