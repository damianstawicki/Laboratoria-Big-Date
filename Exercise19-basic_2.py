import random
import time

print("Podaj rozmiary macierzy")
print("M:")
m = int(input())
print("N:")
n = int(input())

start_time = time.time()

A = []
B = []
A_and_B = []

for i in range(m):
    A_row = []
    B_row = []
    for j in range(n):
        A_row.append(random.randint(1, 14))
        B_row.append(random.randint(1, 14))
    A.append(A_row) 
    B.append(B_row)
    
for i in range(m):
    A_and_B_row = []
    for j in range(n):
        A_and_B_row.append(A[i][j]+B[i][j])
    A_and_B.append(A_and_B_row)
    
end_time = time.time()

full_time = end_time - start_time
        
print(A)
print(B)
print(A_and_B)
print("Czas wykonania: ", full_time)


