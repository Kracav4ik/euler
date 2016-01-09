# encoding: utf-8

from __future__ import division


def pentagonal(n):
    s = []
    for x in range(1, n):
        s.append((x*(3*x - 1))//2)
    return s


def triangle(n):
    s = []
    for x in range(1, n):
        s.append((x*(x + 1))//2)
    return s


def hexagonal(n):
    s = []
    for x in range(1, n):
        s.append((x*(2*x - 1)))
    return s


h_list_numbers = hexagonal(1000000)
t_list_numbers = triangle(1000000)
t_numbers_set = set(t_list_numbers)
p_list_numbers = pentagonal(1000000)
p_numbers_set = set(p_list_numbers)

for x in h_list_numbers:
    if x in p_numbers_set and x in t_numbers_set:
        print x
