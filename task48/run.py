# encoding: utf-8

from __future__ import division

m = 0
for x in range(1, 1001):
    m += x**x
print int(str(m)[-10:])

