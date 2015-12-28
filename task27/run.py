# encoding: utf-8

from __future__ import division


def generate_primes():
    primes = [2]
    for p in range(2, 2 * 10 ** 6):
        is_prime = True
        for divisor in primes:
            if p < divisor * divisor:
                break
            if p % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(p)
    return primes

print 'calculating primes...'
primes_list = generate_primes()
primes_set = set(primes_list)
print '  done!'


def f(a, b):
    result = []
    for n in range(1000):
        abs_f = abs(n ** 2 + a * n + b)
        if abs_f in primes_set:
            result.append(abs_f)
        else:
            return result
    return result

max_a = 0
max_b = 0
max_len = 0
print 'trying a and b...'
for a in range(-999, 1000):
    print 'a ==', a
    for b in range(-999, 1000):
        if max_len < len(f(a, b)):
            max_len = len(f(a, b))
            max_a = a
            max_b = b
print max_len, max_a, max_b, max_a * max_b
print '  done!'
