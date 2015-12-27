# encoding: utf-8

from __future__ import division


def f(n):
    numbers = []
    saw_remainders = []
    remainder = 10
    while 1:
        if remainder in saw_remainders:
            repeat_index = saw_remainders.index(remainder)
            divided_str = ''.join(numbers[:repeat_index])
            repeat_str = ''.join(numbers[repeat_index:])
            return divided_str, repeat_str

        numbers.append(str(remainder // n))
        if remainder % n == 0:
            divided_str = ''.join(numbers)
            return divided_str, ''
        saw_remainders.append(remainder)
        remainder = remainder % n * 10

max_i_repeat = 0
for i in range(2, 1000):
    divided, repeat = f(i)
    if repeat:
        s = '0.%s(%s)' % (divided, repeat)
    else:
        s = '0.%s' % divided
    print i, '->', s
    if len(repeat) > max_i_repeat:
        max_i_repeat = len(repeat)
        i2 = i
print max_i_repeat, i2
