def collatz(x):
    """Generate Collatz sequence
    """
    R = []
    while x > 1:
        R.append(x)
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x + 1
    R.append(1)
    return R
