# PEP-8
def f(xx):
    for p in primes:
        if xx % p == 0:
            return False
    return True        
x = 2 
primes = []
while True:
    if f(x):
        primes.append(x)
    x += 1
    if len(primes) == 10001:
        break
print max(primes)
