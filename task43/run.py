# encoding: utf-8

from __future__ import division


def sub_divisible(s):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    return all(int(s[i+1:i+4]) % p == 0 for i, p in enumerate(divisors))


def all_numbers(letters):
    result = []
    if len(letters) == 1:
        return letters
    for i, head in enumerate(letters):
        reduced_letters = letters[:i] + letters[i+1:]
        reduced_numbers = all_numbers(reduced_letters)
        for tail in reduced_numbers:
            result.append(head + tail)
    return result

result = 0

for x in all_numbers('0123456789'):
    if sub_divisible(x):
        result += int(x)
print result
