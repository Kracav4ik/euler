#big_number = 13195
#big_number = 18
big_number = 6
number = 2
numbers = []
while True:
    if big_number % number == 0:
        numbers.append(number)
    number += 1
    if number == big_number:
        break
print numbers 


               
    
     