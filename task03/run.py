big_number = 600851475143 
number = 2
numbers = []
while True:
    while big_number % number == 0:
        numbers.append(number)
        big_number /= number
    number += 1        
    if big_number == 1:
        break
print numbers 


               
    
     