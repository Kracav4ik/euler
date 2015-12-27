# encoding: utf-8

from __future__ import division


def fac(n):
    m = 1
    for x in range(m, n + m):
        m *= x
    return m


def f(n, letters):
    result = ''
    while len(letters) > 1:
        sub_permutations_count = fac(len(letters) - 1)
        remainder = n % sub_permutations_count
        quotient = n // sub_permutations_count
        result += letters[quotient]
        letters = letters[:quotient] + letters[quotient + 1:]
        n = remainder
    result += letters[0]

    return result

numletters = '0123456789'

print f(999999, numletters)
