f = open("lista.txt", "a+")
add = True
print("Podaj studentów do wczytania:")
stud = []
while(add):
    print("Imie:")
    name = input()
    print("Nazwisko:")
    sname = input()
    print("Grupa:")
    group = input()
    stud.append((name, sname, group))
    print("Czy chcesz dodać kolejnego studenta? Wpisz tak/nie")
    d = input()
    if d == "nie":
        add = False
for s in stud:
    student = ", ".join(s)
    f.write(student)
    f.write("\n")
f.close()    

    
