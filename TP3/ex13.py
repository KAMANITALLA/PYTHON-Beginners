#Exercice 13
t=float(input("Entrer la valeur de temperature de l eau: "))
if t<=0:
    print("Etat: Glace.")
elif t in range(101):
    print("Etat: Liquide.")
else:
    print("Etat: Vapeur.")
