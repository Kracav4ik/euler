# encoding: utf-8

from __future__ import division

parts = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'one hundred',
    200: 'two hundred',
    300: 'three hundred',
    400: 'four hundred',
    500: 'five hundred',
    600: 'six hundred',
    700: 'seven hundred',
    800: 'eight hundred',
    900: 'nine hundred',
    1000: 'one thousand',
}


def to_string_99(n):
    if n in parts:
        return [parts[n]]
    ten = (n // 10) * 10
    digit = n % 10
    return [parts[ten], parts[digit]]


def to_string_999(n):
    if n in parts:
        return [parts[n]]
    hundreds = (n // 100) * 100
    if not hundreds:
        return to_string_99(n)
    m = n - hundreds
    return [parts[hundreds], 'and'] + to_string_99(m)

result = 0

for i in range(1, 1001):
    line = ' '.join(to_string_999(i))
    print line
    line = line.replace(' ', '')
    result += len(line)

print result
