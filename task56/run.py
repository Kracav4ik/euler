# encoding: utf-8

from __future__ import division


def f(n):
    sum_x = 0
    for x in str(n):
        sum_x += int(x)
    return sum_x

list_numbers = []

for a in range(101):
    for b in range(101):
        list_numbers.append(f(a**b))
print max(list_numbers)
