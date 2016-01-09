# encoding: utf-8

from __future__ import division

letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def f(n):
    result = []
    for x in range(1, n):
        m = (x * (x + 1))//2
        result.append(m)
    return result

triangle_numbers_list = f(100)

f = open('p042_words.txt')
s = f.read()
s = s[1:-1]
names = s.split('","')

result = 0


def score(word):
    score = 0
    for letter in word:
        score += letters.find(letter)
    return score


for word in names:
    if score(word) in triangle_numbers_list:
        result += 1
print result

