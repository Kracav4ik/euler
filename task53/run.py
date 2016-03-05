# encoding: utf-8

from __future__ import division


def fac(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result

m = 0

for n in range(101):
    for k in range(n + 1):
        if fac(n) // (fac(k) * fac(n - k)) > 1000000:
            m += 1
print m
