a = 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19
print a

def f(ss):
    for x in range(11, 21):
        if ss % x != 0:
            return False
    return True

s = 2520
while True:
    if f(s):
        break
    else:
        s += 2520

print s                    
