summ = 0
summ2 = 0
for x in range(101):
    summ += x * x
    summ2 += x
m = summ2 * summ2
print m - summ
