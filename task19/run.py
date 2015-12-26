# encoding: utf-8

from __future__ import division

days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}


def is_leap(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

days_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i = 0
s_count = 0
for year in range(1900, 2001):
    for count in days_count:
        if is_leap(year) and count == 28:
            count = 29
        i = (i + count) % 7
        if year != 1900 and i == 6:
            s_count += 1
print s_count



