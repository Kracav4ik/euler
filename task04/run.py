for x in range(10, 100):
    for y in range(10, 100):
        z = str(x * y)
        if z == z[::-1]:
            print x * y
