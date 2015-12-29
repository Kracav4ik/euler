# encoding: utf-8

from __future__ import division


def unique_numbers(b):
    b_list = []
    for x in b:
        if int(x) == 0:
            return False
        if x in b_list:
            return False
        else:
            b_list.append(x)
    return True

result_list = []


for y in range(1000, 10000):
    if not unique_numbers(str(y)):
        continue
    for p in range(1, 100):
        if not unique_numbers(str(p) + str(y)):
            continue
        if y % p == 0:
            if not unique_numbers(str(p)):
                continue
            b = y // p
            if not unique_numbers(str(b) + str(p) + str(y)):
                continue
            if len(str(b) + str(p) + str(y)) != 9:
                continue
            result_list.append([p, b, y])

print result_list

print sum(set(t[-1] for t in result_list))
