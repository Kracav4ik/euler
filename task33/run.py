# encoding: utf-8

from __future__ import division


def remove_letter(str_n, s):
    m = str_n.find(s)
    if s not in str_n:
        return str_n
    b = str_n[:m] + str_n[m + 1:]
    return b


def is_cancelling_fraction(n, m):
    ab = str(n)
    cd = str(m)
    a, b = ab
    if a not in cd and b not in cd or ab[-1] == cd[-1] == '0':
        return False
    if a in cd:
        not_a = remove_letter(cd, a)
        if n * int(not_a) == m * int(b):
            return True
    if b in cd:
        not_b = remove_letter(cd, b)
        if n * int(not_b) == m * int(a):
            return True
    return False

for x in range(10, 100):
    for y in range(10, x):
        if is_cancelling_fraction(y, x):
            print y, '/', x
