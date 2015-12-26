# encoding: utf-8

from __future__ import division


def fac(n):
    y = 1
    for x in range(1, n + 1):
        y *= x
    return y


def C_n_k(n, k):
    return fac(n) / (fac(k) * fac(n - k))

print C_n_k(1, 5)