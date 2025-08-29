# Créé par GENERAL STORES, le 08/12/2023 en Python 3.7
A=int(input("Entrer un nombre: "))
i=2
while A%i !=0 and i<A:
    i+=1
if i==A:
    print("est Premier")
else:
    print("n est pas premier")
