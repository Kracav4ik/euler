palindromes = []
for x in range(100, 1000):
    for y in range(100, 1000):
        z = str(x * y)
        if z == z[::-1]:
            palindromes.append(x * y) 
print max(palindromes)
