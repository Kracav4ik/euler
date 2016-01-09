# encoding: utf-8

from __future__ import division

n = 1
s = ''
p = 0
while p < 100000:
    p = len(s)
    s += str(n)
    n += 1
    if n % 100 == 0:
        print p

print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999])
