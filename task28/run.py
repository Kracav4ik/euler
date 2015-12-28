# encoding: utf-8

from __future__ import division

list_v = [1]
v = 1
b = 2
n = 0
while n < 500:
    for x in range(4):
        v += b
        list_v.append(v)
    b += 2
    n += 1

y = 0
print list_v
for m in list_v:
    y += m
print y
