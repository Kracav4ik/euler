# encoding: utf-8

from __future__ import division

result = [' ']

for b in range(101):
    for c in range(41):
        for d in range(21):
            for e in range(11):
                for f in range(5):
                    for g in range(3):
                        a = 200 - (2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g)
                        if a < 0:
                            continue
                        if a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g == 200:
                            result.append(' ')
print len(result)
# 200 можно одной монетой
