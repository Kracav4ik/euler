# encoding: utf-8

from __future__ import division


def checker(n):
    print 'check', n
    for x in range(50):
        string = str(n + int(str(n)[::-1]))
        print '  ', n, '->', string
        if string == string[::-1]:
            return False
        n = int(string)
    return True

list_lychrel = []

for k in range(10000):
    if checker(k):
        list_lychrel.append(k)
print len(list_lychrel), list_lychrel
