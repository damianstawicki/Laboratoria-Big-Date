import random

def get_triangle(x):
    return x ** 3
    
for i in range(50):
    number = random.randint(1, 1000)
    number_3 = get_triangle(number)
    print(number, "^ 3 =", number_3)
