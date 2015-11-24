summ = 0
fibon1 = 1
fibon2 = 1
while True:
    fibon = fibon1 + fibon2
    fibon1 = fibon2
    fibon2 = fibon
    if fibon>=4000000:
        break
    if fibon % 2 == 0: 
        summ += fibon
    
      
print summ     
