# encoding: utf-8

from __future__ import division


def f(p):
    m = []
    for c in range(1, p//2):
        for a in range(5*c // 7, c):
            b = p - c - a
            if b < 1:
                continue
            if c * c == a * a + b * b:
                m.append([c, a, b])
    return m


max_len_list = 0
for p in range(1, 1001):
    print p
    t_list = f(p)
    if t_list:
        if max_len_list < len(f(p)):
            max_len_list = len(f(p))
            m = p

print max_len_list, m
