# encoding: utf-8

from __future__ import division

def f (n):
    m = 0
    x = str(n)
    for y in x:
        m += int(y) ** 5
    return m
result = 0
for x in range(10, 1000001):
    if x == f(x):
        print x
        result += x
print result
