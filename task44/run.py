# encoding: utf-8

from __future__ import division


def f(n):
    s = []
    for x in range(1, n):
        s.append((x*(3*x - 1))//2)
    return s

list_numbers = f(10000)
numbers_set = set(list_numbers)

for p in list_numbers:
    for q in list_numbers:
        if (p + q) in numbers_set and (p - q) in numbers_set:
            print 'First', p, 'Second', q, 'sum', q + p, 'difference', p - q
