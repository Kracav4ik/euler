# encoding: utf-8

from __future__ import division

# 1. прочитать файл в список слов
f = open('p022_names.txt')
s = f.read()
s = s[1:-1]
names = s.split('","')

# 2. отсортировать список слов в алфавитном порядке
names.sort()

# 3. для каждого слова посчитать количество очков
# COLIN = (3 + 15 + 12 + 9 + 14) * 938 == 49714

letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def scores(n):
    score = 0
    word = names[n]
    for letter in word:
        score += letters.find(letter)
    return score * (n + 1)

# 4. вывести сумму всех очков всех слов

result = 0

for x in range(len(names)):
    result += scores(x)
print result
