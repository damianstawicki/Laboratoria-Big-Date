import random
import time
import numpy

print("Podaj rozmiary macierzy")
print("M:")
M = int(input())
print("N:") 
N = int(input())

start_time = time.time()

A = numpy.random.randint(1, 14, (M,N))
B = numpy.random.randint(1, 14, (M,N))
A_and_B = A + B

end_time = time.time()

full_time = end_time - start_time

print(A)
print(B)
print(A_and_B)
print("Czas działania programu: ", full_time)


