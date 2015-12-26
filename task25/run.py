# encoding: utf-8

from __future__ import division

def fib(n):
    n1 = 1
    n2 = 1
    n3 = 1
    for x in range(n - 2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n3
x = 1
while 1:
    y = str(fib(x))
    if len(y) == 1000:
        print x
        break
    x += 1
