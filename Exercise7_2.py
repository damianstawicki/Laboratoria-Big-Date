count = 0
print('Parzyste liczby:')
for n in range(1, 201):
    if (n%2) == 0:
        count+=1
        print(n)
print('Liczb parzystych było ', count)
