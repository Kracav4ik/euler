def collatz(x):
    """Generate Collatz sequence
    """
    R = []
    while x > 1:
        R.append(x)
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
    R.append(1)
    return R


v = 1
d_max = 1
for x in range(1000000):
    coll_len = len(collatz(x))
    if coll_len > d_max:
        d_max = coll_len
        v = x
print v
