# encoding: utf-8

from __future__ import division


def fac(n):
    v = 1
    for x in range(v, n + v):
        v *= x
    return v


def sum_fac(n):
    b = 0
    for x in str(n):
        b += fac(int(x))
    if b == n:
        return True
    return False

list_fac = []

v = 0

for x in range(10, 10 ** 7):
    if sum_fac(x):
        list_fac.append(x)
for x in list_fac:
    v += x
print v
