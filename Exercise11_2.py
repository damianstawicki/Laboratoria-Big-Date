import random

numbers = []
for i in range(100):
    random_number = random.randint(1, 100)
    numbers.append(random_number)
    
count = 0   
for number in numbers:
    if number < 23:
        count += 1
        
print("Liczb mniejszych od 23 było", count)
