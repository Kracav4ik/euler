# encoding: utf-8

from __future__ import division


def to_bin(n):
    s = ''
    while n > 1:
        s = str(n % 2) + s
        n //= 2
    s = str(n) + s
    return s


def is_palindrome(s):
        return s == s[::-1]

result_list = []
result = 0
for x in range(10**6):
    if is_palindrome(str(x)) and is_palindrome(to_bin(x)):
        result += x
        result_list.append(x)
print 'sum =>', result
print 'list =>', result_list
