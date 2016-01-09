# encoding: utf-8

from __future__ import division


def mass_multiply(number, count):
    l = ''
    for m in range(1, count + 1):
        l += str(m * number)
    return l


def is_pandigital_9(s):
    return '0' not in s and len(s) == 9 and len(s) == len(set(s))

pandigital_list = []

for p in range(1, 10000):
    for q in range(2, 9):
        number_str = mass_multiply(p, q)
        if is_pandigital_9(number_str):
            pandigital_list.append(int(number_str))
print 'Pandigital =>', pandigital_list
print max(pandigital_list)
