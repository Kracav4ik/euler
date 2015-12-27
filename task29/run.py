# encoding: utf-8

from __future__ import division

numbers = []
for a in range(2, 101):
    for b in range(2, 101):
        x = a ** b
        if x not in numbers:
            numbers.append(x)
print len(numbers)
