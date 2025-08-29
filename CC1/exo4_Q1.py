# Créé par GENERAL STORES, le 08/12/2023 en Python 3.7

A=int(input("Entrer un nombre: "))
p=True
for i in range(2,A-1):
    if A%i==0:
        p=False
if p==True:
    print("est Premier")
else:
    print("n est pas premier")



