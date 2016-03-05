# encoding: utf-8

from __future__ import division


def same_digits(p, q):
    string = str(p)
    if len(string) != len(str(q)):
        return False
    for x in str(q):
        if not string:
            return False
        m = -1
        for y in string:
            m += 1
            if x == y:
                string = string[:m] + string[m + 1:]
                break
    if not string:
        return True
    else:
        return False


def same_d2(p, q):
    def gen_map(n):
        m = {}
        for c in str(n):
            m[c] = m.get(c, 0) + 1
        return m

    return gen_map(p) == gen_map(q)


# print same_digits(1, 1), True
# print same_digits(11, 11), True
# print same_digits(121, 112), True
# print same_digits(1211, 1121), True
# print same_digits(125874, 251748), True
#
# print same_digits(1, 2), False
# print same_digits(112, 11), False
# print same_digits(1, 11), False
# print same_digits(11, 21), False
# print same_digits(1, 21), False

f = 1
while 1:
    if f % 10000 == 0:
        print f
    if same_digits(2*f, 3*f) and same_digits(3*f, 4*f) and same_digits(4*f, 5*f) and same_digits(5*f, 6*f):
        print 'DONE', f
        break
    f += 1
